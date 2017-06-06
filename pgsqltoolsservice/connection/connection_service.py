# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""This module holds the connection service class, which allows for the user to connect and
disconnect and holds the current connection, if one is present"""

from __future__ import unicode_literals
import logging
import threading
import uuid

import psycopg2

from pgsqltoolsservice.connection.contracts import (
    CONNECT_REQUEST, ConnectRequestParams,
    DISCONNECT_REQUEST, DisconnectRequestParams,
    CONNECTION_COMPLETE_METHOD, ConnectionCompleteParams,
    ConnectionSummary
)
from pgsqltoolsservice.hosting import RequestContext, ServiceProvider


class ConnectionInfo(object):
    """Information pertaining to a unique connection instance"""

    def __init__(self, owner_uri, details, connection_type):
        self.owner_uri = owner_uri
        self.details = details
        self.connection_id = str(uuid.uuid4())
        self.connection_type = connection_type

    def get_connection(self, connection_type):
        """Get the connection associated with the given connection type, or return None"""
        return self.connection_map.get(connection_type)

    def get_all_connections(self):
        """Get all connections held by this object"""
        return self.connection_map.values()

    def add_connection(self, connection_type, connection):
        """Add a connection to the connection map, associated with the given connection type"""
        self.connection_map[connection_type] = connection

    def remove_connection(self, connection_type):
        """
        Remove the connection associated with the given connection type, or raise a KeyError if
        there is no such connection
        """
        self.connection_map.pop(connection_type)

    def remove_all_connections(self):
        """ Remove all connections held by this object"""
        self.connection_map = {}


class ConnectionService:
    """Manage a single connection, including the ability to connect/disconnect"""

    def __init__(self, server):
        self.connection = None
        self.owner_to_connection_map = {}
        self.owner_to_thread_map = {}
        self.server = server

    def register(self, service_provider: ServiceProvider):
        self._service_provider = service_provider

        # Register the handlers for the service
        self._service_provider.server.set_request_handler(CONNECT_REQUEST, self.handle_connect_request)
        self._service_provider.server.set_request_handler(DISCONNECT_REQUEST, self.handle_disconnect_request)

    # REQUEST HANDLERS #####################################################
    def handle_connect_request(self, request_context: RequestContext, params: ConnectRequestParams) -> None:
        """Kick off a connection in response to an incoming connection request"""
        thread = threading.Thread(
            target=self._connect_and_respond,
            args=(request_context, params)
        )
        thread.daemon = True
        thread.start()
        self.owner_to_thread_map[params.owner_uri] = thread

        request_context.send_response(True)


    def handle_disconnect_request(self, request_context: RequestContext, params: DisconnectRequestParams) -> None:
        """Close a connection in response to an incoming disconnection request"""
        connection_info = self.owner_to_connection_map.get(params.owner_uri)
        if connection_info is None:
            request_context.send_response(False)
        else
            request_context.send_response(self._close_connections(connection_info, params.type))

    # IMPLEMENTATION DETAILS ###############################################
    def _connect_and_respond(self, request_context: RequestContext, params: ConnectRequestParams) -> None:
        """Open a connection and fire the connection complete notification"""
        response = self._connect(params)
        request_context.send_notification(CONNECTION_COMPLETE_METHOD, response)

    def _connect(self, params):
        """
        Open a connection using the given connection information.

        If a connection was already open, disconnect first. Return whether the connection was
        successful
        """

        connection_info = self.owner_to_connection_map.get(params.owner_uri)

        # If there is no saved connection or the saved connections' options do not match, create a new one
        if connection_info is None or connection_info.details['options'] != connection_details

        connection_info = self.owner_to_connection_map.get(owner_uri)

        # If there is no saved connection or the saved connection's options do not match, create a new one
        if connection_info is None or connection_info.details['options'] != connection_details['options']:
            if connection_info is not None:
                close_connections(connection_info)
            connection_info = ConnectionInfo(owner_uri, connection_details)
            self.owner_to_connection_map[owner_uri] = connection_info

        # Get the connection for the given type and build a response if it is present, otherwise open the connection
        connection = connection_info.get_connection(connection_type)
        if connection is not None:
            return build_connection_response(connection_info, connection_type)

        # The connection doesn't exist yet. Build the connection string from the provided options
        connection_options = connection_details['options']
        connection_string = ''
        for option, value in connection_options.items():
            key = CONNECTION_OPTION_KEY_MAP[option] if option in CONNECTION_OPTION_KEY_MAP else option
            connection_string += "{}='{}' ".format(key, value)
        logging.debug(f'Connecting with connection string {connection_string}')

        # Connect using psycopg2
        if self.connection:
            self._disconnect()
        try:
            connection = psycopg2.connect(connection_string)
            connection_info.add_connection(connection_type, connection)
            return build_connection_response(connection_info, connection_type)
        except Exception as err:
            return build_connection_response_error(connection_info, err)

    def _disconnect(self):
        """Close a connection, if there is currently one open"""
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                return False
            self.connection = None
        return True


def build_connection_response(connection_info, connection):
    """Build a connection complete response object"""
    dsn_parameters = connection.get_dsn_parameters()

    connection_summary = ConnectionSummary()
    connection_summary.database_name = dsn_parameters['dbname']
    connection_summary.server_name = dsn_parameters['host']
    connection_summary.user_name = dsn_parameters['user']

    response = ConnectionCompleteParams()
    response.connection_id = connection_info.connection_id
    response.connection_summary = connection_summary
    response.owner_uri = connection_info.owner_uri
    response.type = connection_info.connection_type

    return response


def build_connection_response_error(connection_info, connection_type, err):
    """Build a connection complete response object"""
    response = ConnectionCompleteParams(
        ownerUri=connection_info.owner_uri,
        type=connection_type,
        messages=repr(err),
        errorMessage=str(err)
    )
    return response


def close_connections(connection_info, connection_type=None):
    """
    Close the connections in the given ConnectionInfo object matching the passed type, or
    close all of them if no type is given.

    Return False if no matching connections were found to close, otherwise return True.
    """
    connections_to_close = []
    if connection_type is None:
        connections_to_close = connection_info.get_all_connections()
        if not connections_to_close:
            return False
        connection_info.remove_all_connections()
    else:
        connection = connection_info.get_connection(connection_type)
        if connection is None:
            return False
        connections_to_close.append(connection)
        connection_info.remove_connection(connection_type)
    for connection in connections_to_close:
        try:
            connection.close()
        except Exception:
            # Ignore errors when disconnecting
            pass
    return True


# Dictionary mapping connection option names to their corresponding connection string keys.
# If a name is not present in this map, the name should be used as the key.
CONNECTION_OPTION_KEY_MAP = {
    'connectTimeout': 'connect_timeout',
    'clientEncoding': 'client_encoding',
    'applicationName': 'application_name'
}
