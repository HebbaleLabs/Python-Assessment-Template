# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.business_address_object import BusinessAddressObject  # noqa: E501
from swagger_server.models.business_address_object_update import BusinessAddressObjectUpdate  # noqa: E501
from swagger_server.models.business_address_results_object import BusinessAddressResultsObject  # noqa: E501
from swagger_server.models.business_address_results_object_single import BusinessAddressResultsObjectSingle  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessAddressController(BaseTestCase):
    """BusinessAddressController integration test stubs"""

    def test_add_business_address(self):
        """Test case for add_business_address

        Add a new Business Address
        """
        body = BusinessAddressObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/businessAddresses'.format(businessId='businessId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_business_address(self):
        """Test case for edit_business_address

        Modify an existing Business Address
        """
        body = BusinessAddressObjectUpdate()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessAddresses/{businessId}/{addressTag}/{version}'.format(businessId='businessId_example', addressTag='addressTag_example', version=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_addresses(self):
        """Test case for find_all_business_addresses

        Get all Business Addresses
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/businessAddresses'.format(businessId='businessId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_business_address_by_id(self):
        """Test case for get_business_address_by_id

        Find Business Address by ID
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessAddresses/{businessId}/{addressTag}'.format(businessId='businessId_example', addressTag='addressTag_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
