# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPendingTasksController(BaseTestCase):
    """PendingTasksController integration test stubs"""

    def test_find_all_pending_tasks(self):
        """Test case for find_all_pending_tasks

        Get all pending tasks for the user
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//users/{userId}/PendingTasks'.format(userId='userId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
