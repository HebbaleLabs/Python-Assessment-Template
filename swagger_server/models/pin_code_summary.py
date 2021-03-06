# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PinCodeSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, city_name: str=None, state_name: str=None, pin_code: str=None, tin_number: int=None):  # noqa: E501
        """PinCodeSummary - a model defined in Swagger

        :param id: The id of this PinCodeSummary.  # noqa: E501
        :type id: str
        :param city_name: The city_name of this PinCodeSummary.  # noqa: E501
        :type city_name: str
        :param state_name: The state_name of this PinCodeSummary.  # noqa: E501
        :type state_name: str
        :param pin_code: The pin_code of this PinCodeSummary.  # noqa: E501
        :type pin_code: str
        :param tin_number: The tin_number of this PinCodeSummary.  # noqa: E501
        :type tin_number: int
        """
        self.swagger_types = {
            'id': str,
            'city_name': str,
            'state_name': str,
            'pin_code': str,
            'tin_number': int
        }

        self.attribute_map = {
            'id': '_id',
            'city_name': 'city_name',
            'state_name': 'state_name',
            'pin_code': 'pin_code',
            'tin_number': 'tin_number'
        }

        self._id = id
        self._city_name = city_name
        self._state_name = state_name
        self._pin_code = pin_code
        self._tin_number = tin_number

    @classmethod
    def from_dict(cls, dikt) -> 'PinCodeSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PinCodeSummary of this PinCodeSummary.  # noqa: E501
        :rtype: PinCodeSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this PinCodeSummary.


        :return: The id of this PinCodeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this PinCodeSummary.


        :param id: The id of this PinCodeSummary.
        :type id: str
        """

        self._id = id

    @property
    def city_name(self) -> str:
        """Gets the city_name of this PinCodeSummary.


        :return: The city_name of this PinCodeSummary.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name: str):
        """Sets the city_name of this PinCodeSummary.


        :param city_name: The city_name of this PinCodeSummary.
        :type city_name: str
        """

        self._city_name = city_name

    @property
    def state_name(self) -> str:
        """Gets the state_name of this PinCodeSummary.


        :return: The state_name of this PinCodeSummary.
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name: str):
        """Sets the state_name of this PinCodeSummary.


        :param state_name: The state_name of this PinCodeSummary.
        :type state_name: str
        """

        self._state_name = state_name

    @property
    def pin_code(self) -> str:
        """Gets the pin_code of this PinCodeSummary.


        :return: The pin_code of this PinCodeSummary.
        :rtype: str
        """
        return self._pin_code

    @pin_code.setter
    def pin_code(self, pin_code: str):
        """Sets the pin_code of this PinCodeSummary.


        :param pin_code: The pin_code of this PinCodeSummary.
        :type pin_code: str
        """

        self._pin_code = pin_code

    @property
    def tin_number(self) -> int:
        """Gets the tin_number of this PinCodeSummary.


        :return: The tin_number of this PinCodeSummary.
        :rtype: int
        """
        return self._tin_number

    @tin_number.setter
    def tin_number(self, tin_number: int):
        """Sets the tin_number of this PinCodeSummary.


        :param tin_number: The tin_number of this PinCodeSummary.
        :type tin_number: int
        """

        self._tin_number = tin_number
