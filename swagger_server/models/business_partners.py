# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BusinessPartners(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, version: int=None, first_name: str=None, last_name: str=None, gender: str=None, father_name: str=None, date_of_birth: date=None, aadhaar_no: str=None, marital_status: str=None, main_applicant: str=None, pan_no: str=None, ownership_in_percent: int=None, landline_no: int=None, designation: str=None, residence_ownership: str=None, educational_qualification: str=None, mobile_number: str=None, email_address: str=None, address_line_1: str=None, address_line_2: str=None, address_line_3: str=None, city_name: str=None, city_pin_code: str=None):  # noqa: E501
        """BusinessPartners - a model defined in Swagger

        :param id: The id of this BusinessPartners.  # noqa: E501
        :type id: str
        :param version: The version of this BusinessPartners.  # noqa: E501
        :type version: int
        :param first_name: The first_name of this BusinessPartners.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this BusinessPartners.  # noqa: E501
        :type last_name: str
        :param gender: The gender of this BusinessPartners.  # noqa: E501
        :type gender: str
        :param father_name: The father_name of this BusinessPartners.  # noqa: E501
        :type father_name: str
        :param date_of_birth: The date_of_birth of this BusinessPartners.  # noqa: E501
        :type date_of_birth: date
        :param aadhaar_no: The aadhaar_no of this BusinessPartners.  # noqa: E501
        :type aadhaar_no: str
        :param marital_status: The marital_status of this BusinessPartners.  # noqa: E501
        :type marital_status: str
        :param main_applicant: The main_applicant of this BusinessPartners.  # noqa: E501
        :type main_applicant: str
        :param pan_no: The pan_no of this BusinessPartners.  # noqa: E501
        :type pan_no: str
        :param ownership_in_percent: The ownership_in_percent of this BusinessPartners.  # noqa: E501
        :type ownership_in_percent: int
        :param landline_no: The landline_no of this BusinessPartners.  # noqa: E501
        :type landline_no: int
        :param designation: The designation of this BusinessPartners.  # noqa: E501
        :type designation: str
        :param residence_ownership: The residence_ownership of this BusinessPartners.  # noqa: E501
        :type residence_ownership: str
        :param educational_qualification: The educational_qualification of this BusinessPartners.  # noqa: E501
        :type educational_qualification: str
        :param mobile_number: The mobile_number of this BusinessPartners.  # noqa: E501
        :type mobile_number: str
        :param email_address: The email_address of this BusinessPartners.  # noqa: E501
        :type email_address: str
        :param address_line_1: The address_line_1 of this BusinessPartners.  # noqa: E501
        :type address_line_1: str
        :param address_line_2: The address_line_2 of this BusinessPartners.  # noqa: E501
        :type address_line_2: str
        :param address_line_3: The address_line_3 of this BusinessPartners.  # noqa: E501
        :type address_line_3: str
        :param city_name: The city_name of this BusinessPartners.  # noqa: E501
        :type city_name: str
        :param city_pin_code: The city_pin_code of this BusinessPartners.  # noqa: E501
        :type city_pin_code: str
        """
        self.swagger_types = {
            'id': str,
            'version': int,
            'first_name': str,
            'last_name': str,
            'gender': str,
            'father_name': str,
            'date_of_birth': date,
            'aadhaar_no': str,
            'marital_status': str,
            'main_applicant': str,
            'pan_no': str,
            'ownership_in_percent': int,
            'landline_no': int,
            'designation': str,
            'residence_ownership': str,
            'educational_qualification': str,
            'mobile_number': str,
            'email_address': str,
            'address_line_1': str,
            'address_line_2': str,
            'address_line_3': str,
            'city_name': str,
            'city_pin_code': str
        }

        self.attribute_map = {
            'id': '_id',
            'version': 'version',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'gender': 'gender',
            'father_name': 'father_name',
            'date_of_birth': 'date_of_birth',
            'aadhaar_no': 'aadhaar_no',
            'marital_status': 'marital_status',
            'main_applicant': 'main_applicant',
            'pan_no': 'pan_no',
            'ownership_in_percent': 'ownership_in_percent',
            'landline_no': 'landline_no',
            'designation': 'designation',
            'residence_ownership': 'residence_ownership',
            'educational_qualification': 'educational_qualification',
            'mobile_number': 'mobile_number',
            'email_address': 'email_address',
            'address_line_1': 'address_line_1',
            'address_line_2': 'address_line_2',
            'address_line_3': 'address_line_3',
            'city_name': 'city_name',
            'city_pin_code': 'city_pin_code'
        }

        self._id = id
        self._version = version
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._father_name = father_name
        self._date_of_birth = date_of_birth
        self._aadhaar_no = aadhaar_no
        self._marital_status = marital_status
        self._main_applicant = main_applicant
        self._pan_no = pan_no
        self._ownership_in_percent = ownership_in_percent
        self._landline_no = landline_no
        self._designation = designation
        self._residence_ownership = residence_ownership
        self._educational_qualification = educational_qualification
        self._mobile_number = mobile_number
        self._email_address = email_address
        self._address_line_1 = address_line_1
        self._address_line_2 = address_line_2
        self._address_line_3 = address_line_3
        self._city_name = city_name
        self._city_pin_code = city_pin_code

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessPartners':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessPartners of this BusinessPartners.  # noqa: E501
        :rtype: BusinessPartners
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BusinessPartners.


        :return: The id of this BusinessPartners.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BusinessPartners.


        :param id: The id of this BusinessPartners.
        :type id: str
        """

        self._id = id

    @property
    def version(self) -> int:
        """Gets the version of this BusinessPartners.


        :return: The version of this BusinessPartners.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """Sets the version of this BusinessPartners.


        :param version: The version of this BusinessPartners.
        :type version: int
        """

        self._version = version

    @property
    def first_name(self) -> str:
        """Gets the first_name of this BusinessPartners.


        :return: The first_name of this BusinessPartners.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this BusinessPartners.


        :param first_name: The first_name of this BusinessPartners.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this BusinessPartners.


        :return: The last_name of this BusinessPartners.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this BusinessPartners.


        :param last_name: The last_name of this BusinessPartners.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def gender(self) -> str:
        """Gets the gender of this BusinessPartners.


        :return: The gender of this BusinessPartners.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        """Sets the gender of this BusinessPartners.


        :param gender: The gender of this BusinessPartners.
        :type gender: str
        """
        allowed_values = ["M", "F", "O"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def father_name(self) -> str:
        """Gets the father_name of this BusinessPartners.


        :return: The father_name of this BusinessPartners.
        :rtype: str
        """
        return self._father_name

    @father_name.setter
    def father_name(self, father_name: str):
        """Sets the father_name of this BusinessPartners.


        :param father_name: The father_name of this BusinessPartners.
        :type father_name: str
        """

        self._father_name = father_name

    @property
    def date_of_birth(self) -> date:
        """Gets the date_of_birth of this BusinessPartners.


        :return: The date_of_birth of this BusinessPartners.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        """Sets the date_of_birth of this BusinessPartners.


        :param date_of_birth: The date_of_birth of this BusinessPartners.
        :type date_of_birth: date
        """
        if date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def aadhaar_no(self) -> str:
        """Gets the aadhaar_no of this BusinessPartners.


        :return: The aadhaar_no of this BusinessPartners.
        :rtype: str
        """
        return self._aadhaar_no

    @aadhaar_no.setter
    def aadhaar_no(self, aadhaar_no: str):
        """Sets the aadhaar_no of this BusinessPartners.


        :param aadhaar_no: The aadhaar_no of this BusinessPartners.
        :type aadhaar_no: str
        """
        if aadhaar_no is None:
            raise ValueError("Invalid value for `aadhaar_no`, must not be `None`")  # noqa: E501

        self._aadhaar_no = aadhaar_no

    @property
    def marital_status(self) -> str:
        """Gets the marital_status of this BusinessPartners.


        :return: The marital_status of this BusinessPartners.
        :rtype: str
        """
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status: str):
        """Sets the marital_status of this BusinessPartners.


        :param marital_status: The marital_status of this BusinessPartners.
        :type marital_status: str
        """
        allowed_values = ["Not Married", "Married", "Widowed", "Divorced", "Seperated", "Unspecified"]  # noqa: E501
        if marital_status not in allowed_values:
            raise ValueError(
                "Invalid value for `marital_status` ({0}), must be one of {1}"
                .format(marital_status, allowed_values)
            )

        self._marital_status = marital_status

    @property
    def main_applicant(self) -> str:
        """Gets the main_applicant of this BusinessPartners.


        :return: The main_applicant of this BusinessPartners.
        :rtype: str
        """
        return self._main_applicant

    @main_applicant.setter
    def main_applicant(self, main_applicant: str):
        """Sets the main_applicant of this BusinessPartners.


        :param main_applicant: The main_applicant of this BusinessPartners.
        :type main_applicant: str
        """
        allowed_values = ["Y", "N"]  # noqa: E501
        if main_applicant not in allowed_values:
            raise ValueError(
                "Invalid value for `main_applicant` ({0}), must be one of {1}"
                .format(main_applicant, allowed_values)
            )

        self._main_applicant = main_applicant

    @property
    def pan_no(self) -> str:
        """Gets the pan_no of this BusinessPartners.


        :return: The pan_no of this BusinessPartners.
        :rtype: str
        """
        return self._pan_no

    @pan_no.setter
    def pan_no(self, pan_no: str):
        """Sets the pan_no of this BusinessPartners.


        :param pan_no: The pan_no of this BusinessPartners.
        :type pan_no: str
        """
        if pan_no is None:
            raise ValueError("Invalid value for `pan_no`, must not be `None`")  # noqa: E501

        self._pan_no = pan_no

    @property
    def ownership_in_percent(self) -> int:
        """Gets the ownership_in_percent of this BusinessPartners.


        :return: The ownership_in_percent of this BusinessPartners.
        :rtype: int
        """
        return self._ownership_in_percent

    @ownership_in_percent.setter
    def ownership_in_percent(self, ownership_in_percent: int):
        """Sets the ownership_in_percent of this BusinessPartners.


        :param ownership_in_percent: The ownership_in_percent of this BusinessPartners.
        :type ownership_in_percent: int
        """

        self._ownership_in_percent = ownership_in_percent

    @property
    def landline_no(self) -> int:
        """Gets the landline_no of this BusinessPartners.


        :return: The landline_no of this BusinessPartners.
        :rtype: int
        """
        return self._landline_no

    @landline_no.setter
    def landline_no(self, landline_no: int):
        """Sets the landline_no of this BusinessPartners.


        :param landline_no: The landline_no of this BusinessPartners.
        :type landline_no: int
        """

        self._landline_no = landline_no

    @property
    def designation(self) -> str:
        """Gets the designation of this BusinessPartners.


        :return: The designation of this BusinessPartners.
        :rtype: str
        """
        return self._designation

    @designation.setter
    def designation(self, designation: str):
        """Sets the designation of this BusinessPartners.


        :param designation: The designation of this BusinessPartners.
        :type designation: str
        """

        self._designation = designation

    @property
    def residence_ownership(self) -> str:
        """Gets the residence_ownership of this BusinessPartners.


        :return: The residence_ownership of this BusinessPartners.
        :rtype: str
        """
        return self._residence_ownership

    @residence_ownership.setter
    def residence_ownership(self, residence_ownership: str):
        """Sets the residence_ownership of this BusinessPartners.


        :param residence_ownership: The residence_ownership of this BusinessPartners.
        :type residence_ownership: str
        """
        allowed_values = ["Owned by self", "Owned by Family", "Owned and Mortgaged", "Rented-Less than 1 year", "Rented-1 to 3 years", "Rented-more than 3 years"]  # noqa: E501
        if residence_ownership not in allowed_values:
            raise ValueError(
                "Invalid value for `residence_ownership` ({0}), must be one of {1}"
                .format(residence_ownership, allowed_values)
            )

        self._residence_ownership = residence_ownership

    @property
    def educational_qualification(self) -> str:
        """Gets the educational_qualification of this BusinessPartners.


        :return: The educational_qualification of this BusinessPartners.
        :rtype: str
        """
        return self._educational_qualification

    @educational_qualification.setter
    def educational_qualification(self, educational_qualification: str):
        """Sets the educational_qualification of this BusinessPartners.


        :param educational_qualification: The educational_qualification of this BusinessPartners.
        :type educational_qualification: str
        """
        allowed_values = ["ILLITERATE", "BELOW MATRICULATION", "MATRICULATION", "HIGHER SECONDARY", "GRADUATE", "POST GRADUATE", "PROFESSIONAL"]  # noqa: E501
        if educational_qualification not in allowed_values:
            raise ValueError(
                "Invalid value for `educational_qualification` ({0}), must be one of {1}"
                .format(educational_qualification, allowed_values)
            )

        self._educational_qualification = educational_qualification

    @property
    def mobile_number(self) -> str:
        """Gets the mobile_number of this BusinessPartners.


        :return: The mobile_number of this BusinessPartners.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number: str):
        """Sets the mobile_number of this BusinessPartners.


        :param mobile_number: The mobile_number of this BusinessPartners.
        :type mobile_number: str
        """
        if mobile_number is None:
            raise ValueError("Invalid value for `mobile_number`, must not be `None`")  # noqa: E501

        self._mobile_number = mobile_number

    @property
    def email_address(self) -> str:
        """Gets the email_address of this BusinessPartners.


        :return: The email_address of this BusinessPartners.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address: str):
        """Sets the email_address of this BusinessPartners.


        :param email_address: The email_address of this BusinessPartners.
        :type email_address: str
        """

        self._email_address = email_address

    @property
    def address_line_1(self) -> str:
        """Gets the address_line_1 of this BusinessPartners.


        :return: The address_line_1 of this BusinessPartners.
        :rtype: str
        """
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1: str):
        """Sets the address_line_1 of this BusinessPartners.


        :param address_line_1: The address_line_1 of this BusinessPartners.
        :type address_line_1: str
        """
        if address_line_1 is None:
            raise ValueError("Invalid value for `address_line_1`, must not be `None`")  # noqa: E501
        if address_line_1 is not None and len(address_line_1) > 500:
            raise ValueError("Invalid value for `address_line_1`, length must be less than or equal to `500`")  # noqa: E501
        if address_line_1 is not None and len(address_line_1) < 5:
            raise ValueError("Invalid value for `address_line_1`, length must be greater than or equal to `5`")  # noqa: E501

        self._address_line_1 = address_line_1

    @property
    def address_line_2(self) -> str:
        """Gets the address_line_2 of this BusinessPartners.


        :return: The address_line_2 of this BusinessPartners.
        :rtype: str
        """
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2: str):
        """Sets the address_line_2 of this BusinessPartners.


        :param address_line_2: The address_line_2 of this BusinessPartners.
        :type address_line_2: str
        """
        if address_line_2 is not None and len(address_line_2) > 500:
            raise ValueError("Invalid value for `address_line_2`, length must be less than or equal to `500`")  # noqa: E501
        if address_line_2 is not None and len(address_line_2) < 5:
            raise ValueError("Invalid value for `address_line_2`, length must be greater than or equal to `5`")  # noqa: E501

        self._address_line_2 = address_line_2

    @property
    def address_line_3(self) -> str:
        """Gets the address_line_3 of this BusinessPartners.


        :return: The address_line_3 of this BusinessPartners.
        :rtype: str
        """
        return self._address_line_3

    @address_line_3.setter
    def address_line_3(self, address_line_3: str):
        """Sets the address_line_3 of this BusinessPartners.


        :param address_line_3: The address_line_3 of this BusinessPartners.
        :type address_line_3: str
        """
        if address_line_3 is not None and len(address_line_3) > 500:
            raise ValueError("Invalid value for `address_line_3`, length must be less than or equal to `500`")  # noqa: E501
        if address_line_3 is not None and len(address_line_3) < 5:
            raise ValueError("Invalid value for `address_line_3`, length must be greater than or equal to `5`")  # noqa: E501

        self._address_line_3 = address_line_3

    @property
    def city_name(self) -> str:
        """Gets the city_name of this BusinessPartners.


        :return: The city_name of this BusinessPartners.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name: str):
        """Sets the city_name of this BusinessPartners.


        :param city_name: The city_name of this BusinessPartners.
        :type city_name: str
        """
        if city_name is None:
            raise ValueError("Invalid value for `city_name`, must not be `None`")  # noqa: E501

        self._city_name = city_name

    @property
    def city_pin_code(self) -> str:
        """Gets the city_pin_code of this BusinessPartners.


        :return: The city_pin_code of this BusinessPartners.
        :rtype: str
        """
        return self._city_pin_code

    @city_pin_code.setter
    def city_pin_code(self, city_pin_code: str):
        """Sets the city_pin_code of this BusinessPartners.


        :param city_pin_code: The city_pin_code of this BusinessPartners.
        :type city_pin_code: str
        """
        if city_pin_code is None:
            raise ValueError("Invalid value for `city_pin_code`, must not be `None`")  # noqa: E501

        self._city_pin_code = city_pin_code
