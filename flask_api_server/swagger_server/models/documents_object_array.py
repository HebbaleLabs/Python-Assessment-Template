# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.documents import Documents  # noqa: F401,E501
from swagger_server import util


class DocumentsObjectArray(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, files: List[Documents]=None):  # noqa: E501
        """DocumentsObjectArray - a model defined in Swagger

        :param files: The files of this DocumentsObjectArray.  # noqa: E501
        :type files: List[Documents]
        """
        self.swagger_types = {
            'files': List[Documents]
        }

        self.attribute_map = {
            'files': 'Files'
        }

        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'DocumentsObjectArray':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DocumentsObjectArray of this DocumentsObjectArray.  # noqa: E501
        :rtype: DocumentsObjectArray
        """
        return util.deserialize_model(dikt, cls)

    @property
    def files(self) -> List[Documents]:
        """Gets the files of this DocumentsObjectArray.


        :return: The files of this DocumentsObjectArray.
        :rtype: List[Documents]
        """
        return self._files

    @files.setter
    def files(self, files: List[Documents]):
        """Sets the files of this DocumentsObjectArray.


        :param files: The files of this DocumentsObjectArray.
        :type files: List[Documents]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files
