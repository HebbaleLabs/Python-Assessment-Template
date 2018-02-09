# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.documents_object import DocumentsObject  # noqa: E501
from swagger_server.models.documents_object_array import DocumentsObjectArray  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrganizationPlatformPurchaseSaleInfoController(BaseTestCase):
    """OrganizationPlatformPurchaseSaleInfoController integration test stubs"""

    def test_add_org_platform_documents(self):
        """Test case for add_org_platform_documents

        Upload a platform purchase/sale Info file
        """
        body = DocumentsObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//organization/{org_name}/PlatformFiles'.format(org_name='org_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_org_platform_documents(self):
        """Test case for find_org_platform_documents

        Get all uploaded documents
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//organization/{org_name}/PlatformFiles'.format(org_name='org_name_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
