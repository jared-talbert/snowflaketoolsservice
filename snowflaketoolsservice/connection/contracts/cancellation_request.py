# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from snowflaketoolsservice.connection.contracts.common import ConnectionType
from snowflaketoolsservice.hosting import IncomingMessageConfiguration
from snowflaketoolsservice.serialization import Serializable


class CancelConnectParams(Serializable):
    """Parameters for the cancel connect request"""

    def __init__(self, owner_uri: str = None, connection_type: ConnectionType = ConnectionType.DEFAULT):
        self.owner_uri: str = owner_uri
        self.type: ConnectionType = connection_type


CANCEL_CONNECT_REQUEST = IncomingMessageConfiguration('connection/cancelconnect', CancelConnectParams)
