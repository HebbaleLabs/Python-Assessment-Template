# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_bank_account import BusinessBankAccount  # noqa: F401,E501
from swagger_server import util


class BusinessBankAccountObjectSingle(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_bank_account: BusinessBankAccount=None):  # noqa: E501
        """BusinessBankAccountObjectSingle - a model defined in Swagger

        :param business_bank_account: The business_bank_account of this BusinessBankAccountObjectSingle.  # noqa: E501
        :type business_bank_account: BusinessBankAccount
        """
        self.swagger_types = {
            'business_bank_account': BusinessBankAccount
        }

        self.attribute_map = {
            'business_bank_account': 'businessBankAccount'
        }

        self._business_bank_account = business_bank_account

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessBankAccountObjectSingle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessBankAccountObjectSingle of this BusinessBankAccountObjectSingle.  # noqa: E501
        :rtype: BusinessBankAccountObjectSingle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_bank_account(self) -> BusinessBankAccount:
        """Gets the business_bank_account of this BusinessBankAccountObjectSingle.


        :return: The business_bank_account of this BusinessBankAccountObjectSingle.
        :rtype: BusinessBankAccount
        """
        return self._business_bank_account

    @business_bank_account.setter
    def business_bank_account(self, business_bank_account: BusinessBankAccount):
        """Sets the business_bank_account of this BusinessBankAccountObjectSingle.


        :param business_bank_account: The business_bank_account of this BusinessBankAccountObjectSingle.
        :type business_bank_account: BusinessBankAccount
        """

        self._business_bank_account = business_bank_account
