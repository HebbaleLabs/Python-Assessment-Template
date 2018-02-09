# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.device_array import DeviceArray  # noqa: E501
from swagger_server.models.device_object import DeviceObject  # noqa: E501
from swagger_server.models.error_object import ErrorObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserDevicesController(BaseTestCase):
    """UserDevicesController integration test stubs"""

    def test_add_device(self):
        """Test case for add_device

        Add a new device to the user
        """
        body = DeviceObject()
        response = self.client.open(
            '/api_cas_fundscorner/v1//users/{userId}/Devices'.format(userId='userId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_all_devices(self):
        """Test case for find_all_devices

        Get all user registered devices
        """
        response = self.client.open(
            '/api_cas_fundscorner/v1//users/{userId}/Devices'.format(userId='userId_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
