# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BusinessType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, business_type_code: str=None, business_type_desc: str=None):  # noqa: E501
        """BusinessType - a model defined in Swagger

        :param id: The id of this BusinessType.  # noqa: E501
        :type id: str
        :param business_type_code: The business_type_code of this BusinessType.  # noqa: E501
        :type business_type_code: str
        :param business_type_desc: The business_type_desc of this BusinessType.  # noqa: E501
        :type business_type_desc: str
        """
        self.swagger_types = {
            'id': str,
            'business_type_code': str,
            'business_type_desc': str
        }

        self.attribute_map = {
            'id': '_id',
            'business_type_code': 'business_type_code',
            'business_type_desc': 'business_type_desc'
        }

        self._id = id
        self._business_type_code = business_type_code
        self._business_type_desc = business_type_desc

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessType of this BusinessType.  # noqa: E501
        :rtype: BusinessType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BusinessType.


        :return: The id of this BusinessType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BusinessType.


        :param id: The id of this BusinessType.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def business_type_code(self) -> str:
        """Gets the business_type_code of this BusinessType.


        :return: The business_type_code of this BusinessType.
        :rtype: str
        """
        return self._business_type_code

    @business_type_code.setter
    def business_type_code(self, business_type_code: str):
        """Sets the business_type_code of this BusinessType.


        :param business_type_code: The business_type_code of this BusinessType.
        :type business_type_code: str
        """
        if business_type_code is None:
            raise ValueError("Invalid value for `business_type_code`, must not be `None`")  # noqa: E501

        self._business_type_code = business_type_code

    @property
    def business_type_desc(self) -> str:
        """Gets the business_type_desc of this BusinessType.


        :return: The business_type_desc of this BusinessType.
        :rtype: str
        """
        return self._business_type_desc

    @business_type_desc.setter
    def business_type_desc(self, business_type_desc: str):
        """Sets the business_type_desc of this BusinessType.


        :param business_type_desc: The business_type_desc of this BusinessType.
        :type business_type_desc: str
        """
        if business_type_desc is None:
            raise ValueError("Invalid value for `business_type_desc`, must not be `None`")  # noqa: E501

        self._business_type_desc = business_type_desc
