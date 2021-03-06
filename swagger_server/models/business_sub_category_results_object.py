# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_sub_category import BusinessSubCategory  # noqa: F401,E501
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server import util


class BusinessSubCategoryResultsObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_sub_category: List[BusinessSubCategory]=None, metadata: Metadata=None):  # noqa: E501
        """BusinessSubCategoryResultsObject - a model defined in Swagger

        :param business_sub_category: The business_sub_category of this BusinessSubCategoryResultsObject.  # noqa: E501
        :type business_sub_category: List[BusinessSubCategory]
        :param metadata: The metadata of this BusinessSubCategoryResultsObject.  # noqa: E501
        :type metadata: Metadata
        """
        self.swagger_types = {
            'business_sub_category': List[BusinessSubCategory],
            'metadata': Metadata
        }

        self.attribute_map = {
            'business_sub_category': 'businessSubCategory',
            'metadata': 'metadata'
        }

        self._business_sub_category = business_sub_category
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessSubCategoryResultsObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessSubCategoryResultsObject of this BusinessSubCategoryResultsObject.  # noqa: E501
        :rtype: BusinessSubCategoryResultsObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_sub_category(self) -> List[BusinessSubCategory]:
        """Gets the business_sub_category of this BusinessSubCategoryResultsObject.


        :return: The business_sub_category of this BusinessSubCategoryResultsObject.
        :rtype: List[BusinessSubCategory]
        """
        return self._business_sub_category

    @business_sub_category.setter
    def business_sub_category(self, business_sub_category: List[BusinessSubCategory]):
        """Sets the business_sub_category of this BusinessSubCategoryResultsObject.


        :param business_sub_category: The business_sub_category of this BusinessSubCategoryResultsObject.
        :type business_sub_category: List[BusinessSubCategory]
        """

        self._business_sub_category = business_sub_category

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this BusinessSubCategoryResultsObject.


        :return: The metadata of this BusinessSubCategoryResultsObject.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this BusinessSubCategoryResultsObject.


        :param metadata: The metadata of this BusinessSubCategoryResultsObject.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
