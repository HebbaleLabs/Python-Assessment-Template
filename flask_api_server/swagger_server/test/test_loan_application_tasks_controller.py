# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_tasks_array import LoanApplicationTasksArray  # noqa: E501
from swagger_server.models.loan_application_tasks_object import LoanApplicationTasksObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoanApplicationTasksController(BaseTestCase):
    """LoanApplicationTasksController integration test stubs"""

    def test_add_loan_application_tasks(self):
        """Test case for add_loan_application_tasks

        Add a new Loan Application Task
        """
        body = LoanApplicationTasksObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanAppId}/loanAppTasks'.format(loanAppId='loanAppId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_loan_application_task(self):
        """Test case for edit_loan_application_task

        Edit a Loan Application Task
        """
        body = LoanApplicationTasksObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/loanAppTasks',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_loan_application_tasks(self):
        """Test case for find_loan_application_tasks

        Get all Loan Application Tasks
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanAppId}/loanAppTasks'.format(loanAppId='loanAppId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
