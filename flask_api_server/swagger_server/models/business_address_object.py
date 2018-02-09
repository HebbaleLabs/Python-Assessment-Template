# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_address import BusinessAddress  # noqa: F401,E501
from swagger_server import util


class BusinessAddressObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_address: List[BusinessAddress]=None):  # noqa: E501
        """BusinessAddressObject - a model defined in Swagger

        :param business_address: The business_address of this BusinessAddressObject.  # noqa: E501
        :type business_address: List[BusinessAddress]
        """
        self.swagger_types = {
            'business_address': List[BusinessAddress]
        }

        self.attribute_map = {
            'business_address': 'businessAddress'
        }

        self._business_address = business_address

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessAddressObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessAddressObject of this BusinessAddressObject.  # noqa: E501
        :rtype: BusinessAddressObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_address(self) -> List[BusinessAddress]:
        """Gets the business_address of this BusinessAddressObject.


        :return: The business_address of this BusinessAddressObject.
        :rtype: List[BusinessAddress]
        """
        return self._business_address

    @business_address.setter
    def business_address(self, business_address: List[BusinessAddress]):
        """Sets the business_address of this BusinessAddressObject.


        :param business_address: The business_address of this BusinessAddressObject.
        :type business_address: List[BusinessAddress]
        """
        if business_address is None:
            raise ValueError("Invalid value for `business_address`, must not be `None`")  # noqa: E501

        self._business_address = business_address
