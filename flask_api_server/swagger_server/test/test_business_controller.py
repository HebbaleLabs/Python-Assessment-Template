# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.business_object import BusinessObject  # noqa: E501
from swagger_server.models.business_object_update import BusinessObjectUpdate  # noqa: E501
from swagger_server.models.business_results_object import BusinessResultsObject  # noqa: E501
from swagger_server.models.business_summary_results_object import BusinessSummaryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessController(BaseTestCase):
    """BusinessController integration test stubs"""

    def test_add_business(self):
        """Test case for add_business

        Add a new Business
        """
        body = BusinessObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_business(self):
        """Test case for edit_business

        Modify an existing Business
        """
        body = BusinessObjectUpdate()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/{version}'.format(businessId='businessId_example', version=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_businesess(self):
        """Test case for find_businesess

        Get all Businessess
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_business_by_id(self):
        """Test case for get_business_by_id

        Find Business by Id
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}'.format(businessId='businessId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
