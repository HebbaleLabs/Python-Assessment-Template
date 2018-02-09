# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.loan_application_documents_array import LoanApplicationDocumentsArray  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLoanApplicationDocumentsController(BaseTestCase):
    """LoanApplicationDocumentsController integration test stubs"""

    def test_find_loan_application_docs(self):
        """Test case for find_loan_application_docs

        Get all Loan Application Documents
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//loanApplications/{loanAppId}/loanAppDocuments'.format(loanAppId='loanAppId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
