# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_notes_array import LoanApplicationNotesArray  # noqa: E501
from swagger_server.models.loan_application_notes_object import LoanApplicationNotesObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoanApplicationNotesController(BaseTestCase):
    """LoanApplicationNotesController integration test stubs"""

    def test_add_loan_application_notes(self):
        """Test case for add_loan_application_notes

        Add a new Loan Application Notes
        """
        body = LoanApplicationNotesObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanAppId}/loanAppNotes'.format(loanAppId='loanAppId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_loan_application_notes(self):
        """Test case for edit_loan_application_notes

        Add a new Loan Application Notes
        """
        body = LoanApplicationNotesObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/loanAppNotes/{loanAppId}/{noteId}/{version}'.format(loanAppId='loanAppId_example', noteId=56, version=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_loan_app_notes_by_id(self):
        """Test case for find_loan_app_notes_by_id

        Get all Loan Application Notes
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/loanAppNotes/{loanAppId}/{noteId}'.format(loanAppId='loanAppId_example', noteId=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_loan_application_notes(self):
        """Test case for find_loan_application_notes

        Get all Loan Application Notes
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanAppId}/loanAppNotes'.format(loanAppId='loanAppId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
