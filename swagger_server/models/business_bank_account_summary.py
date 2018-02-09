# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BusinessBankAccountSummary(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, business_pan: str=None, bank_name: str=None, account_number: int=None, ifsc_code: str=None, account_type: str=None, primary_account: str=None):  # noqa: E501
        """BusinessBankAccountSummary - a model defined in Swagger

        :param id: The id of this BusinessBankAccountSummary.  # noqa: E501
        :type id: str
        :param business_pan: The business_pan of this BusinessBankAccountSummary.  # noqa: E501
        :type business_pan: str
        :param bank_name: The bank_name of this BusinessBankAccountSummary.  # noqa: E501
        :type bank_name: str
        :param account_number: The account_number of this BusinessBankAccountSummary.  # noqa: E501
        :type account_number: int
        :param ifsc_code: The ifsc_code of this BusinessBankAccountSummary.  # noqa: E501
        :type ifsc_code: str
        :param account_type: The account_type of this BusinessBankAccountSummary.  # noqa: E501
        :type account_type: str
        :param primary_account: The primary_account of this BusinessBankAccountSummary.  # noqa: E501
        :type primary_account: str
        """
        self.swagger_types = {
            'id': str,
            'business_pan': str,
            'bank_name': str,
            'account_number': int,
            'ifsc_code': str,
            'account_type': str,
            'primary_account': str
        }

        self.attribute_map = {
            'id': '_id',
            'business_pan': 'business_pan',
            'bank_name': 'bank_name',
            'account_number': 'account_number',
            'ifsc_code': 'ifsc_code',
            'account_type': 'account_type',
            'primary_account': 'primary_account'
        }

        self._id = id
        self._business_pan = business_pan
        self._bank_name = bank_name
        self._account_number = account_number
        self._ifsc_code = ifsc_code
        self._account_type = account_type
        self._primary_account = primary_account

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessBankAccountSummary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessBankAccountSummary of this BusinessBankAccountSummary.  # noqa: E501
        :rtype: BusinessBankAccountSummary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BusinessBankAccountSummary.


        :return: The id of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BusinessBankAccountSummary.


        :param id: The id of this BusinessBankAccountSummary.
        :type id: str
        """

        self._id = id

    @property
    def business_pan(self) -> str:
        """Gets the business_pan of this BusinessBankAccountSummary.


        :return: The business_pan of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._business_pan

    @business_pan.setter
    def business_pan(self, business_pan: str):
        """Sets the business_pan of this BusinessBankAccountSummary.


        :param business_pan: The business_pan of this BusinessBankAccountSummary.
        :type business_pan: str
        """

        self._business_pan = business_pan

    @property
    def bank_name(self) -> str:
        """Gets the bank_name of this BusinessBankAccountSummary.


        :return: The bank_name of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name: str):
        """Sets the bank_name of this BusinessBankAccountSummary.


        :param bank_name: The bank_name of this BusinessBankAccountSummary.
        :type bank_name: str
        """

        self._bank_name = bank_name

    @property
    def account_number(self) -> int:
        """Gets the account_number of this BusinessBankAccountSummary.


        :return: The account_number of this BusinessBankAccountSummary.
        :rtype: int
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: int):
        """Sets the account_number of this BusinessBankAccountSummary.


        :param account_number: The account_number of this BusinessBankAccountSummary.
        :type account_number: int
        """

        self._account_number = account_number

    @property
    def ifsc_code(self) -> str:
        """Gets the ifsc_code of this BusinessBankAccountSummary.


        :return: The ifsc_code of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._ifsc_code

    @ifsc_code.setter
    def ifsc_code(self, ifsc_code: str):
        """Sets the ifsc_code of this BusinessBankAccountSummary.


        :param ifsc_code: The ifsc_code of this BusinessBankAccountSummary.
        :type ifsc_code: str
        """

        self._ifsc_code = ifsc_code

    @property
    def account_type(self) -> str:
        """Gets the account_type of this BusinessBankAccountSummary.


        :return: The account_type of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type: str):
        """Sets the account_type of this BusinessBankAccountSummary.


        :param account_type: The account_type of this BusinessBankAccountSummary.
        :type account_type: str
        """

        self._account_type = account_type

    @property
    def primary_account(self) -> str:
        """Gets the primary_account of this BusinessBankAccountSummary.


        :return: The primary_account of this BusinessBankAccountSummary.
        :rtype: str
        """
        return self._primary_account

    @primary_account.setter
    def primary_account(self, primary_account: str):
        """Sets the primary_account of this BusinessBankAccountSummary.


        :param primary_account: The primary_account of this BusinessBankAccountSummary.
        :type primary_account: str
        """

        self._primary_account = primary_account
