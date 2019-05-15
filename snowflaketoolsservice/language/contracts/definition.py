# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""This module holds contracts for the definition service calls"""

from snowflaketoolsservice.hosting import IncomingMessageConfiguration
from snowflaketoolsservice.serialization import Serializable
from snowflaketoolsservice.workspace.contracts import TextDocumentPosition, Position, TextDocumentIdentifier


class TextDocumentPositionParams(Serializable):
    def __init__(self, text_document: TextDocumentIdentifier, position: Position):
        self.text_document = text_document
        self.position = position


DEFINITION_REQUEST = IncomingMessageConfiguration('textDocument/definition', TextDocumentPosition)
