# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_object import LoanApplicationObject  # noqa: E501
from swagger_server.models.loan_application_object_update import LoanApplicationObjectUpdate  # noqa: E501
from swagger_server.models.loan_application_results_object import LoanApplicationResultsObject  # noqa: E501
from swagger_server.models.loan_application_summary_results_object import LoanApplicationSummaryResultsObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoanApplicationController(BaseTestCase):
    """LoanApplicationController integration test stubs"""

    def test_add_loan_application(self):
        """Test case for add_loan_application

        Add a new Loan Application
        """
        body = LoanApplicationObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_loan_application(self):
        """Test case for edit_loan_application

        Modify an existing Loan Application
        """
        body = LoanApplicationObjectUpdate()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanApplicationId}/{version}'.format(version=789, loanApplicationId='loanApplicationId_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_loan_applications(self):
        """Test case for find_loan_applications

        Get all Loan Applications
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_loan_application_by_id(self):
        """Test case for get_loan_application_by_id

        Find Loan Application by ID
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanApplicationId}'.format(loanApplicationId='loanApplicationId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
