# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server import util


class BusinessAddressResultsObjectSingle(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_address: object=None, metadata: Metadata=None):  # noqa: E501
        """BusinessAddressResultsObjectSingle - a model defined in Swagger

        :param business_address: The business_address of this BusinessAddressResultsObjectSingle.  # noqa: E501
        :type business_address: object
        :param metadata: The metadata of this BusinessAddressResultsObjectSingle.  # noqa: E501
        :type metadata: Metadata
        """
        self.swagger_types = {
            'business_address': object,
            'metadata': Metadata
        }

        self.attribute_map = {
            'business_address': 'businessAddress',
            'metadata': 'metadata'
        }

        self._business_address = business_address
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessAddressResultsObjectSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessAddressResultsObjectSingle of this BusinessAddressResultsObjectSingle.  # noqa: E501
        :rtype: BusinessAddressResultsObjectSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_address(self) -> object:
        """Gets the business_address of this BusinessAddressResultsObjectSingle.


        :return: The business_address of this BusinessAddressResultsObjectSingle.
        :rtype: object
        """
        return self._business_address

    @business_address.setter
    def business_address(self, business_address: object):
        """Sets the business_address of this BusinessAddressResultsObjectSingle.


        :param business_address: The business_address of this BusinessAddressResultsObjectSingle.
        :type business_address: object
        """

        self._business_address = business_address

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this BusinessAddressResultsObjectSingle.


        :return: The metadata of this BusinessAddressResultsObjectSingle.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this BusinessAddressResultsObjectSingle.


        :param metadata: The metadata of this BusinessAddressResultsObjectSingle.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata