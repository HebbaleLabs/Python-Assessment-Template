# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.loan_application_notes import LoanApplicationNotes  # noqa: F401,E501
from swagger_server import util


class LoanApplicationNotesObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, loan_app_notes: LoanApplicationNotes=None):  # noqa: E501
        """LoanApplicationNotesObject - a model defined in Swagger

        :param loan_app_notes: The loan_app_notes of this LoanApplicationNotesObject.  # noqa: E501
        :type loan_app_notes: LoanApplicationNotes
        """
        self.swagger_types = {
            'loan_app_notes': LoanApplicationNotes
        }

        self.attribute_map = {
            'loan_app_notes': 'loanAppNotes'
        }

        self._loan_app_notes = loan_app_notes

    @classmethod
    def from_dict(cls, dikt) -> 'LoanApplicationNotesObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LoanApplicationNotesObject of this LoanApplicationNotesObject.  # noqa: E501
        :rtype: LoanApplicationNotesObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def loan_app_notes(self) -> LoanApplicationNotes:
        """Gets the loan_app_notes of this LoanApplicationNotesObject.


        :return: The loan_app_notes of this LoanApplicationNotesObject.
        :rtype: LoanApplicationNotes
        """
        return self._loan_app_notes

    @loan_app_notes.setter
    def loan_app_notes(self, loan_app_notes: LoanApplicationNotes):
        """Sets the loan_app_notes of this LoanApplicationNotesObject.


        :param loan_app_notes: The loan_app_notes of this LoanApplicationNotesObject.
        :type loan_app_notes: LoanApplicationNotes
        """
        if loan_app_notes is None:
            raise ValueError("Invalid value for `loan_app_notes`, must not be `None`")  # noqa: E501

        self._loan_app_notes = loan_app_notes
