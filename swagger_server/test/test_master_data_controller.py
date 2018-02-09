# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bank_results_object import BankResultsObject  # noqa: E501
from swagger_server.models.business_category_results_object import BusinessCategoryResultsObject  # noqa: E501
from swagger_server.models.business_file_type_code_results_object import BusinessFileTypeCodeResultsObject  # noqa: E501
from swagger_server.models.business_sub_category_results_object import BusinessSubCategoryResultsObject  # noqa: E501
from swagger_server.models.city_summary_results_object import CitySummaryResultsObject  # noqa: E501
from swagger_server.models.customer_category_results_object import CustomerCategoryResultsObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.models.operating_type_results_object import OperatingTypeResultsObject  # noqa: E501
from swagger_server.models.pin_code_summary_results_object import PinCodeSummaryResultsObject  # noqa: E501
from swagger_server.models.relationship_results_object import RelationshipResultsObject  # noqa: E501
from swagger_server.models.state_results_object import StateResultsObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMasterDataController(BaseTestCase):
    """MasterDataController integration test stubs"""

    def test_find_all_banks(self):
        """Test case for find_all_banks

        Get all Banks
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/banks',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_categories(self):
        """Test case for find_all_business_categories

        Get all BusinessCategories
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/businessCategories',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_file_types(self):
        """Test case for find_all_business_file_types

        Get all Business File Types
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/businessFileTypes',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_business_sub_categories(self):
        """Test case for find_all_business_sub_categories

        Get all BusinessSubCategories
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/businessSubCategories',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_cities(self):
        """Test case for find_all_cities

        Get all cities
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/cities',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_customer_categories(self):
        """Test case for find_all_customer_categories

        Get all CustomerCategories
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/customerCategories',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_operating_types(self):
        """Test case for find_all_operating_types

        Get all operatingTypes
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/operatingTypes',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_pin_codes(self):
        """Test case for find_all_pin_codes

        Get all pin codes
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/pinCodes',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_relationships(self):
        """Test case for find_all_relationships

        Get all Relationships
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/relationships',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_retailers(self):
        """Test case for find_all_retailers

        Get all retailers
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/retailers',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_states(self):
        """Test case for find_all_states

        Get all States
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('query', 'query_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/states',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pin_code_summary_by_city_id(self):
        """Test case for get_pin_code_summary_by_city_id

        Get all pin codes summary by cityId
        """
        query_string = [('offset', 100),
                        ('limit', 200),
                        ('cityId', 56),
                        ('stateId', 56),
                        ('cityName', 'cityName_example'),
                        ('stateName', 'stateName_example')]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/pinCodes/findByCityOrState',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pin_code_summary_by_pin_code(self):
        """Test case for get_pin_code_summary_by_pin_code

        Get all pin codes summary by pinCode
        """
        query_string = [('offset', 100),
                        ('limit', 200)]
        response = self.client.open(
            '/api_cas_fundscorner/v1//masterData/pinCodes/{pinCode}'.format(pinCode='pinCode_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
