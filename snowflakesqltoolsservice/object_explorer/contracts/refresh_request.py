# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from snowflakesqltoolsservice.hosting import IncomingMessageConfiguration
from snowflakesqltoolsservice.object_explorer.contracts.expand_request import ExpandParameters

REFRESH_REQUEST = IncomingMessageConfiguration('objectexplorer/refresh', ExpandParameters)
