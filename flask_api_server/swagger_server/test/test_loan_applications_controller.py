# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLoanApplicationsController(BaseTestCase):
    """LoanApplicationsController integration test stubs"""

    def test_find_all_business_loan_applications(self):
        """Test case for find_all_business_loan_applications

        Get all Loan Applications for  business
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/loanApplications'.format(businessId='businessId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
