# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_partners import BusinessPartners  # noqa: F401,E501
from swagger_server import util


class BusinessUpdate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_type_code: str=None, business_category_code: str=None, business_sub_cat_code: str=None, operating_type_code: str=None, operating_since_month: str=None, operating_since_year: int=None, gstin_no: str=None, retailer_id: str=None, no_of_partners: int=None, no_of_employees: int=1, business_mobile_no: str=None, business_landline_no: int=None, email_id: str=None, bank_od_cc_limit: str=None, annual_turnover: str=None, primary_address_line_1: str=None, primary_address_line_2: str=None, primary_address_line_3: str=None, primary_city_name: str=None, business_ownership: str=None, primary_pin_code: str=None, business_partners: List[BusinessPartners]=None):  # noqa: E501
        """BusinessUpdate - a model defined in Swagger

        :param business_type_code: The business_type_code of this BusinessUpdate.  # noqa: E501
        :type business_type_code: str
        :param business_category_code: The business_category_code of this BusinessUpdate.  # noqa: E501
        :type business_category_code: str
        :param business_sub_cat_code: The business_sub_cat_code of this BusinessUpdate.  # noqa: E501
        :type business_sub_cat_code: str
        :param operating_type_code: The operating_type_code of this BusinessUpdate.  # noqa: E501
        :type operating_type_code: str
        :param operating_since_month: The operating_since_month of this BusinessUpdate.  # noqa: E501
        :type operating_since_month: str
        :param operating_since_year: The operating_since_year of this BusinessUpdate.  # noqa: E501
        :type operating_since_year: int
        :param gstin_no: The gstin_no of this BusinessUpdate.  # noqa: E501
        :type gstin_no: str
        :param retailer_id: The retailer_id of this BusinessUpdate.  # noqa: E501
        :type retailer_id: str
        :param no_of_partners: The no_of_partners of this BusinessUpdate.  # noqa: E501
        :type no_of_partners: int
        :param no_of_employees: The no_of_employees of this BusinessUpdate.  # noqa: E501
        :type no_of_employees: int
        :param business_mobile_no: The business_mobile_no of this BusinessUpdate.  # noqa: E501
        :type business_mobile_no: str
        :param business_landline_no: The business_landline_no of this BusinessUpdate.  # noqa: E501
        :type business_landline_no: int
        :param email_id: The email_id of this BusinessUpdate.  # noqa: E501
        :type email_id: str
        :param bank_od_cc_limit: The bank_od_cc_limit of this BusinessUpdate.  # noqa: E501
        :type bank_od_cc_limit: str
        :param annual_turnover: The annual_turnover of this BusinessUpdate.  # noqa: E501
        :type annual_turnover: str
        :param primary_address_line_1: The primary_address_line_1 of this BusinessUpdate.  # noqa: E501
        :type primary_address_line_1: str
        :param primary_address_line_2: The primary_address_line_2 of this BusinessUpdate.  # noqa: E501
        :type primary_address_line_2: str
        :param primary_address_line_3: The primary_address_line_3 of this BusinessUpdate.  # noqa: E501
        :type primary_address_line_3: str
        :param primary_city_name: The primary_city_name of this BusinessUpdate.  # noqa: E501
        :type primary_city_name: str
        :param business_ownership: The business_ownership of this BusinessUpdate.  # noqa: E501
        :type business_ownership: str
        :param primary_pin_code: The primary_pin_code of this BusinessUpdate.  # noqa: E501
        :type primary_pin_code: str
        :param business_partners: The business_partners of this BusinessUpdate.  # noqa: E501
        :type business_partners: List[BusinessPartners]
        """
        self.swagger_types = {
            'business_type_code': str,
            'business_category_code': str,
            'business_sub_cat_code': str,
            'operating_type_code': str,
            'operating_since_month': str,
            'operating_since_year': int,
            'gstin_no': str,
            'retailer_id': str,
            'no_of_partners': int,
            'no_of_employees': int,
            'business_mobile_no': str,
            'business_landline_no': int,
            'email_id': str,
            'bank_od_cc_limit': str,
            'annual_turnover': str,
            'primary_address_line_1': str,
            'primary_address_line_2': str,
            'primary_address_line_3': str,
            'primary_city_name': str,
            'business_ownership': str,
            'primary_pin_code': str,
            'business_partners': List[BusinessPartners]
        }

        self.attribute_map = {
            'business_type_code': 'business_type_code',
            'business_category_code': 'business_category_code',
            'business_sub_cat_code': 'business_sub_cat_code',
            'operating_type_code': 'operating_type_code',
            'operating_since_month': 'operating_since_month',
            'operating_since_year': 'operating_since_year',
            'gstin_no': 'gstin_no',
            'retailer_id': 'retailer_id',
            'no_of_partners': 'no_of_partners',
            'no_of_employees': 'no_of_employees',
            'business_mobile_no': 'business_mobile_no',
            'business_landline_no': 'business_landline_no',
            'email_id': 'email_id',
            'bank_od_cc_limit': 'bank_od_cc_limit',
            'annual_turnover': 'annual_turnover',
            'primary_address_line_1': 'primary_address_line_1',
            'primary_address_line_2': 'primary_address_line_2',
            'primary_address_line_3': 'primary_address_line_3',
            'primary_city_name': 'primary_city_name',
            'business_ownership': 'business_ownership',
            'primary_pin_code': 'primary_pin_code',
            'business_partners': 'business_partners'
        }

        self._business_type_code = business_type_code
        self._business_category_code = business_category_code
        self._business_sub_cat_code = business_sub_cat_code
        self._operating_type_code = operating_type_code
        self._operating_since_month = operating_since_month
        self._operating_since_year = operating_since_year
        self._gstin_no = gstin_no
        self._retailer_id = retailer_id
        self._no_of_partners = no_of_partners
        self._no_of_employees = no_of_employees
        self._business_mobile_no = business_mobile_no
        self._business_landline_no = business_landline_no
        self._email_id = email_id
        self._bank_od_cc_limit = bank_od_cc_limit
        self._annual_turnover = annual_turnover
        self._primary_address_line_1 = primary_address_line_1
        self._primary_address_line_2 = primary_address_line_2
        self._primary_address_line_3 = primary_address_line_3
        self._primary_city_name = primary_city_name
        self._business_ownership = business_ownership
        self._primary_pin_code = primary_pin_code
        self._business_partners = business_partners

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessUpdate of this BusinessUpdate.  # noqa: E501
        :rtype: BusinessUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_type_code(self) -> str:
        """Gets the business_type_code of this BusinessUpdate.


        :return: The business_type_code of this BusinessUpdate.
        :rtype: str
        """
        return self._business_type_code

    @business_type_code.setter
    def business_type_code(self, business_type_code: str):
        """Sets the business_type_code of this BusinessUpdate.


        :param business_type_code: The business_type_code of this BusinessUpdate.
        :type business_type_code: str
        """

        self._business_type_code = business_type_code

    @property
    def business_category_code(self) -> str:
        """Gets the business_category_code of this BusinessUpdate.


        :return: The business_category_code of this BusinessUpdate.
        :rtype: str
        """
        return self._business_category_code

    @business_category_code.setter
    def business_category_code(self, business_category_code: str):
        """Sets the business_category_code of this BusinessUpdate.


        :param business_category_code: The business_category_code of this BusinessUpdate.
        :type business_category_code: str
        """

        self._business_category_code = business_category_code

    @property
    def business_sub_cat_code(self) -> str:
        """Gets the business_sub_cat_code of this BusinessUpdate.


        :return: The business_sub_cat_code of this BusinessUpdate.
        :rtype: str
        """
        return self._business_sub_cat_code

    @business_sub_cat_code.setter
    def business_sub_cat_code(self, business_sub_cat_code: str):
        """Sets the business_sub_cat_code of this BusinessUpdate.


        :param business_sub_cat_code: The business_sub_cat_code of this BusinessUpdate.
        :type business_sub_cat_code: str
        """

        self._business_sub_cat_code = business_sub_cat_code

    @property
    def operating_type_code(self) -> str:
        """Gets the operating_type_code of this BusinessUpdate.


        :return: The operating_type_code of this BusinessUpdate.
        :rtype: str
        """
        return self._operating_type_code

    @operating_type_code.setter
    def operating_type_code(self, operating_type_code: str):
        """Sets the operating_type_code of this BusinessUpdate.


        :param operating_type_code: The operating_type_code of this BusinessUpdate.
        :type operating_type_code: str
        """

        self._operating_type_code = operating_type_code

    @property
    def operating_since_month(self) -> str:
        """Gets the operating_since_month of this BusinessUpdate.


        :return: The operating_since_month of this BusinessUpdate.
        :rtype: str
        """
        return self._operating_since_month

    @operating_since_month.setter
    def operating_since_month(self, operating_since_month: str):
        """Sets the operating_since_month of this BusinessUpdate.


        :param operating_since_month: The operating_since_month of this BusinessUpdate.
        :type operating_since_month: str
        """

        self._operating_since_month = operating_since_month

    @property
    def operating_since_year(self) -> int:
        """Gets the operating_since_year of this BusinessUpdate.


        :return: The operating_since_year of this BusinessUpdate.
        :rtype: int
        """
        return self._operating_since_year

    @operating_since_year.setter
    def operating_since_year(self, operating_since_year: int):
        """Sets the operating_since_year of this BusinessUpdate.


        :param operating_since_year: The operating_since_year of this BusinessUpdate.
        :type operating_since_year: int
        """
        if operating_since_year is not None and operating_since_year < 1900:  # noqa: E501
            raise ValueError("Invalid value for `operating_since_year`, must be a value greater than or equal to `1900`")  # noqa: E501

        self._operating_since_year = operating_since_year

    @property
    def gstin_no(self) -> str:
        """Gets the gstin_no of this BusinessUpdate.


        :return: The gstin_no of this BusinessUpdate.
        :rtype: str
        """
        return self._gstin_no

    @gstin_no.setter
    def gstin_no(self, gstin_no: str):
        """Sets the gstin_no of this BusinessUpdate.


        :param gstin_no: The gstin_no of this BusinessUpdate.
        :type gstin_no: str
        """

        self._gstin_no = gstin_no

    @property
    def retailer_id(self) -> str:
        """Gets the retailer_id of this BusinessUpdate.


        :return: The retailer_id of this BusinessUpdate.
        :rtype: str
        """
        return self._retailer_id

    @retailer_id.setter
    def retailer_id(self, retailer_id: str):
        """Sets the retailer_id of this BusinessUpdate.


        :param retailer_id: The retailer_id of this BusinessUpdate.
        :type retailer_id: str
        """

        self._retailer_id = retailer_id

    @property
    def no_of_partners(self) -> int:
        """Gets the no_of_partners of this BusinessUpdate.


        :return: The no_of_partners of this BusinessUpdate.
        :rtype: int
        """
        return self._no_of_partners

    @no_of_partners.setter
    def no_of_partners(self, no_of_partners: int):
        """Sets the no_of_partners of this BusinessUpdate.


        :param no_of_partners: The no_of_partners of this BusinessUpdate.
        :type no_of_partners: int
        """
        if no_of_partners is not None and no_of_partners < 1:  # noqa: E501
            raise ValueError("Invalid value for `no_of_partners`, must be a value greater than or equal to `1`")  # noqa: E501

        self._no_of_partners = no_of_partners

    @property
    def no_of_employees(self) -> int:
        """Gets the no_of_employees of this BusinessUpdate.


        :return: The no_of_employees of this BusinessUpdate.
        :rtype: int
        """
        return self._no_of_employees

    @no_of_employees.setter
    def no_of_employees(self, no_of_employees: int):
        """Sets the no_of_employees of this BusinessUpdate.


        :param no_of_employees: The no_of_employees of this BusinessUpdate.
        :type no_of_employees: int
        """
        if no_of_employees is not None and no_of_employees < 1:  # noqa: E501
            raise ValueError("Invalid value for `no_of_employees`, must be a value greater than or equal to `1`")  # noqa: E501

        self._no_of_employees = no_of_employees

    @property
    def business_mobile_no(self) -> str:
        """Gets the business_mobile_no of this BusinessUpdate.


        :return: The business_mobile_no of this BusinessUpdate.
        :rtype: str
        """
        return self._business_mobile_no

    @business_mobile_no.setter
    def business_mobile_no(self, business_mobile_no: str):
        """Sets the business_mobile_no of this BusinessUpdate.


        :param business_mobile_no: The business_mobile_no of this BusinessUpdate.
        :type business_mobile_no: str
        """

        self._business_mobile_no = business_mobile_no

    @property
    def business_landline_no(self) -> int:
        """Gets the business_landline_no of this BusinessUpdate.


        :return: The business_landline_no of this BusinessUpdate.
        :rtype: int
        """
        return self._business_landline_no

    @business_landline_no.setter
    def business_landline_no(self, business_landline_no: int):
        """Sets the business_landline_no of this BusinessUpdate.


        :param business_landline_no: The business_landline_no of this BusinessUpdate.
        :type business_landline_no: int
        """

        self._business_landline_no = business_landline_no

    @property
    def email_id(self) -> str:
        """Gets the email_id of this BusinessUpdate.


        :return: The email_id of this BusinessUpdate.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id: str):
        """Sets the email_id of this BusinessUpdate.


        :param email_id: The email_id of this BusinessUpdate.
        :type email_id: str
        """

        self._email_id = email_id

    @property
    def bank_od_cc_limit(self) -> str:
        """Gets the bank_od_cc_limit of this BusinessUpdate.


        :return: The bank_od_cc_limit of this BusinessUpdate.
        :rtype: str
        """
        return self._bank_od_cc_limit

    @bank_od_cc_limit.setter
    def bank_od_cc_limit(self, bank_od_cc_limit: str):
        """Sets the bank_od_cc_limit of this BusinessUpdate.


        :param bank_od_cc_limit: The bank_od_cc_limit of this BusinessUpdate.
        :type bank_od_cc_limit: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if bank_od_cc_limit not in allowed_values:
            raise ValueError(
                "Invalid value for `bank_od_cc_limit` ({0}), must be one of {1}"
                .format(bank_od_cc_limit, allowed_values)
            )

        self._bank_od_cc_limit = bank_od_cc_limit

    @property
    def annual_turnover(self) -> str:
        """Gets the annual_turnover of this BusinessUpdate.


        :return: The annual_turnover of this BusinessUpdate.
        :rtype: str
        """
        return self._annual_turnover

    @annual_turnover.setter
    def annual_turnover(self, annual_turnover: str):
        """Sets the annual_turnover of this BusinessUpdate.


        :param annual_turnover: The annual_turnover of this BusinessUpdate.
        :type annual_turnover: str
        """
        allowed_values = ["<25L", "25L-50L", "50L-1Cr", "1Cr-2Cr", "2Cr-3Cr", "3Cr-4Cr", "4Cr-5Cr", ">5Cr"]  # noqa: E501
        if annual_turnover not in allowed_values:
            raise ValueError(
                "Invalid value for `annual_turnover` ({0}), must be one of {1}"
                .format(annual_turnover, allowed_values)
            )

        self._annual_turnover = annual_turnover

    @property
    def primary_address_line_1(self) -> str:
        """Gets the primary_address_line_1 of this BusinessUpdate.


        :return: The primary_address_line_1 of this BusinessUpdate.
        :rtype: str
        """
        return self._primary_address_line_1

    @primary_address_line_1.setter
    def primary_address_line_1(self, primary_address_line_1: str):
        """Sets the primary_address_line_1 of this BusinessUpdate.


        :param primary_address_line_1: The primary_address_line_1 of this BusinessUpdate.
        :type primary_address_line_1: str
        """
        if primary_address_line_1 is not None and len(primary_address_line_1) > 500:
            raise ValueError("Invalid value for `primary_address_line_1`, length must be less than or equal to `500`")  # noqa: E501
        if primary_address_line_1 is not None and len(primary_address_line_1) < 5:
            raise ValueError("Invalid value for `primary_address_line_1`, length must be greater than or equal to `5`")  # noqa: E501

        self._primary_address_line_1 = primary_address_line_1

    @property
    def primary_address_line_2(self) -> str:
        """Gets the primary_address_line_2 of this BusinessUpdate.


        :return: The primary_address_line_2 of this BusinessUpdate.
        :rtype: str
        """
        return self._primary_address_line_2

    @primary_address_line_2.setter
    def primary_address_line_2(self, primary_address_line_2: str):
        """Sets the primary_address_line_2 of this BusinessUpdate.


        :param primary_address_line_2: The primary_address_line_2 of this BusinessUpdate.
        :type primary_address_line_2: str
        """
        if primary_address_line_2 is not None and len(primary_address_line_2) > 500:
            raise ValueError("Invalid value for `primary_address_line_2`, length must be less than or equal to `500`")  # noqa: E501
        if primary_address_line_2 is not None and len(primary_address_line_2) < 5:
            raise ValueError("Invalid value for `primary_address_line_2`, length must be greater than or equal to `5`")  # noqa: E501

        self._primary_address_line_2 = primary_address_line_2

    @property
    def primary_address_line_3(self) -> str:
        """Gets the primary_address_line_3 of this BusinessUpdate.


        :return: The primary_address_line_3 of this BusinessUpdate.
        :rtype: str
        """
        return self._primary_address_line_3

    @primary_address_line_3.setter
    def primary_address_line_3(self, primary_address_line_3: str):
        """Sets the primary_address_line_3 of this BusinessUpdate.


        :param primary_address_line_3: The primary_address_line_3 of this BusinessUpdate.
        :type primary_address_line_3: str
        """
        if primary_address_line_3 is not None and len(primary_address_line_3) > 500:
            raise ValueError("Invalid value for `primary_address_line_3`, length must be less than or equal to `500`")  # noqa: E501
        if primary_address_line_3 is not None and len(primary_address_line_3) < 5:
            raise ValueError("Invalid value for `primary_address_line_3`, length must be greater than or equal to `5`")  # noqa: E501

        self._primary_address_line_3 = primary_address_line_3

    @property
    def primary_city_name(self) -> str:
        """Gets the primary_city_name of this BusinessUpdate.


        :return: The primary_city_name of this BusinessUpdate.
        :rtype: str
        """
        return self._primary_city_name

    @primary_city_name.setter
    def primary_city_name(self, primary_city_name: str):
        """Sets the primary_city_name of this BusinessUpdate.


        :param primary_city_name: The primary_city_name of this BusinessUpdate.
        :type primary_city_name: str
        """

        self._primary_city_name = primary_city_name

    @property
    def business_ownership(self) -> str:
        """Gets the business_ownership of this BusinessUpdate.


        :return: The business_ownership of this BusinessUpdate.
        :rtype: str
        """
        return self._business_ownership

    @business_ownership.setter
    def business_ownership(self, business_ownership: str):
        """Sets the business_ownership of this BusinessUpdate.


        :param business_ownership: The business_ownership of this BusinessUpdate.
        :type business_ownership: str
        """
        allowed_values = ["Owned by self", "Owned by Family", "Owned and Mortgaged", "Rented-Less than 1 year", "Rented-1 to 3 years", "Rented-more than 3 years"]  # noqa: E501
        if business_ownership not in allowed_values:
            raise ValueError(
                "Invalid value for `business_ownership` ({0}), must be one of {1}"
                .format(business_ownership, allowed_values)
            )

        self._business_ownership = business_ownership

    @property
    def primary_pin_code(self) -> str:
        """Gets the primary_pin_code of this BusinessUpdate.


        :return: The primary_pin_code of this BusinessUpdate.
        :rtype: str
        """
        return self._primary_pin_code

    @primary_pin_code.setter
    def primary_pin_code(self, primary_pin_code: str):
        """Sets the primary_pin_code of this BusinessUpdate.


        :param primary_pin_code: The primary_pin_code of this BusinessUpdate.
        :type primary_pin_code: str
        """

        self._primary_pin_code = primary_pin_code

    @property
    def business_partners(self) -> List[BusinessPartners]:
        """Gets the business_partners of this BusinessUpdate.


        :return: The business_partners of this BusinessUpdate.
        :rtype: List[BusinessPartners]
        """
        return self._business_partners

    @business_partners.setter
    def business_partners(self, business_partners: List[BusinessPartners]):
        """Sets the business_partners of this BusinessUpdate.


        :param business_partners: The business_partners of this BusinessUpdate.
        :type business_partners: List[BusinessPartners]
        """

        self._business_partners = business_partners