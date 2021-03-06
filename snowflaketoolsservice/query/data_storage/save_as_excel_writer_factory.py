# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import io

from snowflaketoolsservice.query.data_storage import FileStreamFactory, SaveAsExcelWriter


class SaveAsExcelFileStreamFactory(FileStreamFactory):

    def __init__(self, params) -> None:
        FileStreamFactory.__init__(self, params)

    def get_writer(self, file_name: str):
        return SaveAsExcelWriter(io.open(file_name, 'w'), self._params)
