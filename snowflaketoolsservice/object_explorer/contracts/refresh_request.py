# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from snowflaketoolsservice.hosting import IncomingMessageConfiguration
from snowflaketoolsservice.object_explorer.contracts.expand_request import ExpandParameters

REFRESH_REQUEST = IncomingMessageConfiguration('objectexplorer/refresh', ExpandParameters)
