# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LoanApplicationNotes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: str=None, notes: str=None, note_id: int=None):  # noqa: E501
        """LoanApplicationNotes - a model defined in Swagger

        :param user_id: The user_id of this LoanApplicationNotes.  # noqa: E501
        :type user_id: str
        :param notes: The notes of this LoanApplicationNotes.  # noqa: E501
        :type notes: str
        :param note_id: The note_id of this LoanApplicationNotes.  # noqa: E501
        :type note_id: int
        """
        self.swagger_types = {
            'user_id': str,
            'notes': str,
            'note_id': int
        }

        self.attribute_map = {
            'user_id': 'userId',
            'notes': 'notes',
            'note_id': 'noteId'
        }

        self._user_id = user_id
        self._notes = notes
        self._note_id = note_id

    @classmethod
    def from_dict(cls, dikt) -> 'LoanApplicationNotes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LoanApplicationNotes of this LoanApplicationNotes.  # noqa: E501
        :rtype: LoanApplicationNotes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> str:
        """Gets the user_id of this LoanApplicationNotes.


        :return: The user_id of this LoanApplicationNotes.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this LoanApplicationNotes.


        :param user_id: The user_id of this LoanApplicationNotes.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def notes(self) -> str:
        """Gets the notes of this LoanApplicationNotes.


        :return: The notes of this LoanApplicationNotes.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this LoanApplicationNotes.


        :param notes: The notes of this LoanApplicationNotes.
        :type notes: str
        """
        if notes is None:
            raise ValueError("Invalid value for `notes`, must not be `None`")  # noqa: E501

        self._notes = notes

    @property
    def note_id(self) -> int:
        """Gets the note_id of this LoanApplicationNotes.


        :return: The note_id of this LoanApplicationNotes.
        :rtype: int
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id: int):
        """Sets the note_id of this LoanApplicationNotes.


        :param note_id: The note_id of this LoanApplicationNotes.
        :type note_id: int
        """

        self._note_id = note_id
