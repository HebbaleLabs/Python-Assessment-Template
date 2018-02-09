# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PinCode(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, city_name: str=None, pin_code: str=None):  # noqa: E501
        """PinCode - a model defined in Swagger

        :param id: The id of this PinCode.  # noqa: E501
        :type id: str
        :param city_name: The city_name of this PinCode.  # noqa: E501
        :type city_name: str
        :param pin_code: The pin_code of this PinCode.  # noqa: E501
        :type pin_code: str
        """
        self.swagger_types = {
            'id': str,
            'city_name': str,
            'pin_code': str
        }

        self.attribute_map = {
            'id': '_id',
            'city_name': 'city_name',
            'pin_code': 'pin_code'
        }

        self._id = id
        self._city_name = city_name
        self._pin_code = pin_code

    @classmethod
    def from_dict(cls, dikt) -> 'PinCode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PinCode of this PinCode.  # noqa: E501
        :rtype: PinCode
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this PinCode.


        :return: The id of this PinCode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this PinCode.


        :param id: The id of this PinCode.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def city_name(self) -> str:
        """Gets the city_name of this PinCode.


        :return: The city_name of this PinCode.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name: str):
        """Sets the city_name of this PinCode.


        :param city_name: The city_name of this PinCode.
        :type city_name: str
        """
        if city_name is None:
            raise ValueError("Invalid value for `city_name`, must not be `None`")  # noqa: E501

        self._city_name = city_name

    @property
    def pin_code(self) -> str:
        """Gets the pin_code of this PinCode.


        :return: The pin_code of this PinCode.
        :rtype: str
        """
        return self._pin_code

    @pin_code.setter
    def pin_code(self, pin_code: str):
        """Sets the pin_code of this PinCode.


        :param pin_code: The pin_code of this PinCode.
        :type pin_code: str
        """
        if pin_code is None:
            raise ValueError("Invalid value for `pin_code`, must not be `None`")  # noqa: E501

        self._pin_code = pin_code
