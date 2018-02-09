# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_platform_details import BusinessPlatformDetails  # noqa: F401,E501
from swagger_server import util


class BusinessPlatformDetailsObjectArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_platform_details: List[BusinessPlatformDetails]=None):  # noqa: E501
        """BusinessPlatformDetailsObjectArray - a model defined in Swagger

        :param business_platform_details: The business_platform_details of this BusinessPlatformDetailsObjectArray.  # noqa: E501
        :type business_platform_details: List[BusinessPlatformDetails]
        """
        self.swagger_types = {
            'business_platform_details': List[BusinessPlatformDetails]
        }

        self.attribute_map = {
            'business_platform_details': 'businessPlatformDetails'
        }

        self._business_platform_details = business_platform_details

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessPlatformDetailsObjectArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessPlatformDetailsObjectArray of this BusinessPlatformDetailsObjectArray.  # noqa: E501
        :rtype: BusinessPlatformDetailsObjectArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_platform_details(self) -> List[BusinessPlatformDetails]:
        """Gets the business_platform_details of this BusinessPlatformDetailsObjectArray.


        :return: The business_platform_details of this BusinessPlatformDetailsObjectArray.
        :rtype: List[BusinessPlatformDetails]
        """
        return self._business_platform_details

    @business_platform_details.setter
    def business_platform_details(self, business_platform_details: List[BusinessPlatformDetails]):
        """Sets the business_platform_details of this BusinessPlatformDetailsObjectArray.


        :param business_platform_details: The business_platform_details of this BusinessPlatformDetailsObjectArray.
        :type business_platform_details: List[BusinessPlatformDetails]
        """

        self._business_platform_details = business_platform_details
