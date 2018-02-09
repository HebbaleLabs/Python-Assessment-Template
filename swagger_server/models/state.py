# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class State(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, state_code: str=None, state_name: str=None, tin_number: int=None):  # noqa: E501
        """State - a model defined in Swagger

        :param id: The id of this State.  # noqa: E501
        :type id: str
        :param state_code: The state_code of this State.  # noqa: E501
        :type state_code: str
        :param state_name: The state_name of this State.  # noqa: E501
        :type state_name: str
        :param tin_number: The tin_number of this State.  # noqa: E501
        :type tin_number: int
        """
        self.swagger_types = {
            'id': str,
            'state_code': str,
            'state_name': str,
            'tin_number': int
        }

        self.attribute_map = {
            'id': '_id',
            'state_code': 'state_code',
            'state_name': 'state_name',
            'tin_number': 'tin_number'
        }

        self._id = id
        self._state_code = state_code
        self._state_name = state_name
        self._tin_number = tin_number

    @classmethod
    def from_dict(cls, dikt) -> 'State':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The State of this State.  # noqa: E501
        :rtype: State
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this State.


        :return: The id of this State.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this State.


        :param id: The id of this State.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state_code(self) -> str:
        """Gets the state_code of this State.


        :return: The state_code of this State.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code: str):
        """Sets the state_code of this State.


        :param state_code: The state_code of this State.
        :type state_code: str
        """
        if state_code is None:
            raise ValueError("Invalid value for `state_code`, must not be `None`")  # noqa: E501

        self._state_code = state_code

    @property
    def state_name(self) -> str:
        """Gets the state_name of this State.


        :return: The state_name of this State.
        :rtype: str
        """
        return self._state_name

    @state_name.setter
    def state_name(self, state_name: str):
        """Sets the state_name of this State.


        :param state_name: The state_name of this State.
        :type state_name: str
        """
        if state_name is None:
            raise ValueError("Invalid value for `state_name`, must not be `None`")  # noqa: E501

        self._state_name = state_name

    @property
    def tin_number(self) -> int:
        """Gets the tin_number of this State.


        :return: The tin_number of this State.
        :rtype: int
        """
        return self._tin_number

    @tin_number.setter
    def tin_number(self, tin_number: int):
        """Sets the tin_number of this State.


        :param tin_number: The tin_number of this State.
        :type tin_number: int
        """
        if tin_number is None:
            raise ValueError("Invalid value for `tin_number`, must not be `None`")  # noqa: E501

        self._tin_number = tin_number