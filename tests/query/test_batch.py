# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from unittest import mock

import tests.utils as utils
from pgsqltoolsservice.query.batch import (
    Batch, BatchEvents, create_batch, create_result_set, ResultSetStorageType, SelectBatch
)
from pgsqltoolsservice.query_execution.contracts.common import SelectionData
from pgsqltoolsservice.query.in_memory_result_set import InMemoryResultSet
from pgsqltoolsservice.query.file_storage_result_set import FileStorageResultSet


class TestBatch(unittest.TestCase):

    def setUp(self):
        self._cursor = utils.MockCursor(None)
        self._connection = utils.MockConnection(cursor=self._cursor)
        self._batch_text = 'Select * from t1'
        self._batch_id = 1
        self._batch_events = BatchEvents()
        self._selection_data = SelectionData()
        self._result_set = mock.MagicMock()

    def create_batch_with(self, batch, storage_type: ResultSetStorageType):
        return batch(self._batch_text, self._batch_id, self._selection_data, self._batch_events, storage_type)

    def create_and_execute_batch(self, batch):
        with mock.patch('pgsqltoolsservice.query.batch.create_result_set', new=mock.Mock(return_value=self._result_set)):
            batch = self.create_batch_with(batch, ResultSetStorageType.IN_MEMORY)
            batch.execute(self._connection)
            return batch

    def assert_properties(self, property_name: str, expected_value):
        batch = self.create_and_execute_batch(Batch)

        self.assertEqual(getattr(batch, property_name), expected_value)

    def test_execute_calls_execute_on_cursor(self):
        self.create_and_execute_batch(Batch)
        self._cursor.execute.assert_called_once_with(self._batch_text)

    def test_execute_calls_read_result_to_end_on_result_set(self):
        batch = self.create_and_execute_batch(Batch)

        self.assertEqual(batch._result_set, self._result_set)
        self._result_set.read_result_to_end.assert_called_once_with(self._cursor)

    def test_execute_sets_has_executed(self):
        batch = self.create_and_execute_batch(Batch)

        self.assertTrue(batch._has_executed)

    def test_select_batch_creates_server_side_cursor(self):
        cursor_name = 'Test'
        with mock.patch('uuid.uuid4', new=mock.Mock(return_value=cursor_name)):
            self.create_and_execute_batch(SelectBatch)

        self._connection.cursor.assert_called_once_with(cursor_name)

    def test_prop_batch_summary(self):
        batch_summary = mock.MagicMock()

        with mock.patch('pgsqltoolsservice.query.contracts.BatchSummary.from_batch', new=mock.Mock(return_value=batch_summary)):
            self.assert_properties('batch_summary', batch_summary)

    def test_prop_has_error(self):
        self.assert_properties('has_error', False)

    def test_prop_has_executed(self):
        self.assert_properties('has_executed', True)

    def test_create_result_set_with_type_in_memory(self):
        result_set = create_result_set(ResultSetStorageType.IN_MEMORY, 1, 1)

        self.assertTrue(isinstance(result_set, InMemoryResultSet))

    def test_create__result_set_with_type_file_storage(self):
        result_set = create_result_set(ResultSetStorageType.FILE_STORAGE, 1, 1)

        self.assertTrue(isinstance(result_set, FileStorageResultSet))

    def test_create_batch_for_select(self):

        batch_text = ''' Select
        * from t1 '''

        batch = create_batch(batch_text, 0, self._selection_data, self._batch_events, ResultSetStorageType.IN_MEMORY)

        self.assertTrue(isinstance(batch, SelectBatch))

    def test_create_batch_for_select_with_additional_spaces(self):

        batch_text = '    Select    *      from t1 '

        batch = create_batch(batch_text, 0, self._selection_data, self._batch_events, ResultSetStorageType.IN_MEMORY)

        self.assertTrue(isinstance(batch, SelectBatch))

    def test_create_batch_for_select_into(self):

        batch_text = '    Select   into  temptable  from t1 '

        batch = create_batch(batch_text, 0, self._selection_data, self._batch_events, ResultSetStorageType.IN_MEMORY)

        self.assertFalse(isinstance(batch, SelectBatch))
        self.assertTrue(isinstance(batch, Batch))

    def test_create_batch_for_non_select(self):

        batch_text = 'Insert into t1 values(1)'

        batch = create_batch(batch_text, 0, self._selection_data, self._batch_events, ResultSetStorageType.IN_MEMORY)

        self.assertFalse(isinstance(batch, SelectBatch))
        self.assertTrue(isinstance(batch, Batch))