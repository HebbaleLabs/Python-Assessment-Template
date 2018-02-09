# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_platform import BusinessPlatform  # noqa: F401,E501
from swagger_server import util


class BusinessPlatformObjectArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_platform: List[BusinessPlatform]=None):  # noqa: E501
        """BusinessPlatformObjectArray - a model defined in Swagger

        :param business_platform: The business_platform of this BusinessPlatformObjectArray.  # noqa: E501
        :type business_platform: List[BusinessPlatform]
        """
        self.swagger_types = {
            'business_platform': List[BusinessPlatform]
        }

        self.attribute_map = {
            'business_platform': 'businessPlatform'
        }

        self._business_platform = business_platform

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessPlatformObjectArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessPlatformObjectArray of this BusinessPlatformObjectArray.  # noqa: E501
        :rtype: BusinessPlatformObjectArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_platform(self) -> List[BusinessPlatform]:
        """Gets the business_platform of this BusinessPlatformObjectArray.


        :return: The business_platform of this BusinessPlatformObjectArray.
        :rtype: List[BusinessPlatform]
        """
        return self._business_platform

    @business_platform.setter
    def business_platform(self, business_platform: List[BusinessPlatform]):
        """Sets the business_platform of this BusinessPlatformObjectArray.


        :param business_platform: The business_platform of this BusinessPlatformObjectArray.
        :type business_platform: List[BusinessPlatform]
        """

        self._business_platform = business_platform