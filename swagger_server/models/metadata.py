# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Metadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, total: int=None, offset: int=None, limit: int=None):  # noqa: E501
        """Metadata - a model defined in Swagger

        :param count: The count of this Metadata.  # noqa: E501
        :type count: int
        :param total: The total of this Metadata.  # noqa: E501
        :type total: int
        :param offset: The offset of this Metadata.  # noqa: E501
        :type offset: int
        :param limit: The limit of this Metadata.  # noqa: E501
        :type limit: int
        """
        self.swagger_types = {
            'count': int,
            'total': int,
            'offset': int,
            'limit': int
        }

        self.attribute_map = {
            'count': 'count',
            'total': 'total',
            'offset': 'offset',
            'limit': 'limit'
        }

        self._count = count
        self._total = total
        self._offset = offset
        self._limit = limit

    @classmethod
    def from_dict(cls, dikt) -> 'Metadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Metadata of this Metadata.  # noqa: E501
        :rtype: Metadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this Metadata.


        :return: The count of this Metadata.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this Metadata.


        :param count: The count of this Metadata.
        :type count: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def total(self) -> int:
        """Gets the total of this Metadata.


        :return: The total of this Metadata.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total: int):
        """Sets the total of this Metadata.


        :param total: The total of this Metadata.
        :type total: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def offset(self) -> int:
        """Gets the offset of this Metadata.


        :return: The offset of this Metadata.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset: int):
        """Sets the offset of this Metadata.


        :param offset: The offset of this Metadata.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self) -> int:
        """Gets the limit of this Metadata.


        :return: The limit of this Metadata.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit: int):
        """Sets the limit of this Metadata.


        :param limit: The limit of this Metadata.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit
