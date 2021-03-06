# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.business_platform_object_array import BusinessPlatformObjectArray  # noqa: E501
from swagger_server.models.business_platform_object_update import BusinessPlatformObjectUpdate  # noqa: E501
from swagger_server.models.business_platform_results_objects import BusinessPlatformResultsObjects  # noqa: E501
from swagger_server.models.business_platform_summary_results_object import BusinessPlatformSummaryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessPlatformController(BaseTestCase):
    """BusinessPlatformController integration test stubs"""

    def test_add_business_platforms(self):
        """Test case for add_business_platforms

        Add a new Business Platform for a Business
        """
        body = BusinessPlatformObjectArray()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/businessPlatform'.format(businessId='businessId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_business_platform(self):
        """Test case for edit_business_platform

        Modify an existing Business Platform
        """
        body = BusinessPlatformObjectUpdate()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessPlatform/{businessId}/{orgName}/{version}'.format(businessId='businessId_example', orgName='orgName_example', version=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_platforms(self):
        """Test case for find_all_business_platforms

        Get all Business Platforms
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/businessPlatform'.format(businessId='businessId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_business_platform_by_id(self):
        """Test case for get_business_platform_by_id

        Find Business Platform by ID
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessPlatform/{businessId}/{orgName}'.format(businessId='businessId_example', orgName='orgName_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
