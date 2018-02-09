# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.business_bank_ac_summary_results_object import BusinessBankAcSummaryResultsObject  # noqa: E501
from swagger_server.models.business_bank_account_object import BusinessBankAccountObject  # noqa: E501
from swagger_server.models.business_bank_account_object_single import BusinessBankAccountObjectSingle  # noqa: E501
from swagger_server.models.business_bank_account_object_update import BusinessBankAccountObjectUpdate  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessBankAccountController(BaseTestCase):
    """BusinessBankAccountController integration test stubs"""

    def test_add_business_bank_accounts(self):
        """Test case for add_business_bank_accounts

        Add a new Business Bank Account
        """
        body = BusinessBankAccountObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/bankAccounts'.format(businessId='businessId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_business_bank_account(self):
        """Test case for edit_business_bank_account

        Modify an existing Business Bank Account
        """
        body = BusinessBankAccountObjectUpdate()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/bankAccounts/{businessId}/{bankName}/{accountNumber}/{version}'.format(businessId='businessId_example', bankName='bankName_example', version=789, accountNumber=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_bank_accounts(self):
        """Test case for find_all_business_bank_accounts

        Get all Business Bank Accounts for  business
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/bankAccounts'.format(businessId='businessId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_business_bank_account_by_id(self):
        """Test case for get_business_bank_account_by_id

        Find Business Bank Account by ID
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/bankAccounts/{businessId}/{bankName}/{accountNumber}'.format(businessId='businessId_example', bankName='bankName_example', accountNumber=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
