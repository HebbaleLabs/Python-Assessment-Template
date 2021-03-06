# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CustomerCategory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, customer_cat_code: str=None, customer_cat_desc: str=None):  # noqa: E501
        """CustomerCategory - a model defined in Swagger

        :param id: The id of this CustomerCategory.  # noqa: E501
        :type id: str
        :param customer_cat_code: The customer_cat_code of this CustomerCategory.  # noqa: E501
        :type customer_cat_code: str
        :param customer_cat_desc: The customer_cat_desc of this CustomerCategory.  # noqa: E501
        :type customer_cat_desc: str
        """
        self.swagger_types = {
            'id': str,
            'customer_cat_code': str,
            'customer_cat_desc': str
        }

        self.attribute_map = {
            'id': '_id',
            'customer_cat_code': 'customer_cat_code',
            'customer_cat_desc': 'customer_cat_desc'
        }

        self._id = id
        self._customer_cat_code = customer_cat_code
        self._customer_cat_desc = customer_cat_desc

    @classmethod
    def from_dict(cls, dikt) -> 'CustomerCategory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CustomerCategory of this CustomerCategory.  # noqa: E501
        :rtype: CustomerCategory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CustomerCategory.


        :return: The id of this CustomerCategory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CustomerCategory.


        :param id: The id of this CustomerCategory.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def customer_cat_code(self) -> str:
        """Gets the customer_cat_code of this CustomerCategory.


        :return: The customer_cat_code of this CustomerCategory.
        :rtype: str
        """
        return self._customer_cat_code

    @customer_cat_code.setter
    def customer_cat_code(self, customer_cat_code: str):
        """Sets the customer_cat_code of this CustomerCategory.


        :param customer_cat_code: The customer_cat_code of this CustomerCategory.
        :type customer_cat_code: str
        """
        if customer_cat_code is None:
            raise ValueError("Invalid value for `customer_cat_code`, must not be `None`")  # noqa: E501

        self._customer_cat_code = customer_cat_code

    @property
    def customer_cat_desc(self) -> str:
        """Gets the customer_cat_desc of this CustomerCategory.


        :return: The customer_cat_desc of this CustomerCategory.
        :rtype: str
        """
        return self._customer_cat_desc

    @customer_cat_desc.setter
    def customer_cat_desc(self, customer_cat_desc: str):
        """Sets the customer_cat_desc of this CustomerCategory.


        :param customer_cat_desc: The customer_cat_desc of this CustomerCategory.
        :type customer_cat_desc: str
        """
        if customer_cat_desc is None:
            raise ValueError("Invalid value for `customer_cat_desc`, must not be `None`")  # noqa: E501

        self._customer_cat_desc = customer_cat_desc
