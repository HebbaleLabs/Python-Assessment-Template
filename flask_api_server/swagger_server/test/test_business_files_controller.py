# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.documents_object import DocumentsObject  # noqa: E501
from swagger_server.models.documents_object_array import DocumentsObjectArray  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessFilesController(BaseTestCase):
    """BusinessFilesController integration test stubs"""

    def test_add_business_documents(self):
        """Test case for add_business_documents

        Upload a business file
        """
        body = DocumentsObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/Files'.format(businessId='businessId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_business_partner_documents(self):
        """Test case for add_business_partner_documents

        Upload a business partner file
        """
        body = DocumentsObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessPartner/{businessId}/{partnerPan}/Files'.format(businessId='businessId_example', partnerPan='partnerPan_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_business_documents(self):
        """Test case for find_business_documents

        Get all uploaded documents
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/{businessId}/Files'.format(businessId='businessId_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_business_partner_documents(self):
        """Test case for find_business_partner_documents

        Get all uploaded documents
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//businesses/businessPartner/{businessId}/{partnerPan}/Files'.format(businessId='businessId_example', partnerPan='partnerPan_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
