# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_summary import BusinessSummary  # noqa: F401,E501
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server import util


class BusinessSummaryResultsObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business: List[BusinessSummary]=None, metadata: Metadata=None):  # noqa: E501
        """BusinessSummaryResultsObject - a model defined in Swagger

        :param business: The business of this BusinessSummaryResultsObject.  # noqa: E501
        :type business: List[BusinessSummary]
        :param metadata: The metadata of this BusinessSummaryResultsObject.  # noqa: E501
        :type metadata: Metadata
        """
        self.swagger_types = {
            'business': List[BusinessSummary],
            'metadata': Metadata
        }

        self.attribute_map = {
            'business': 'business',
            'metadata': 'metadata'
        }

        self._business = business
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessSummaryResultsObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessSummaryResultsObject of this BusinessSummaryResultsObject.  # noqa: E501
        :rtype: BusinessSummaryResultsObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business(self) -> List[BusinessSummary]:
        """Gets the business of this BusinessSummaryResultsObject.


        :return: The business of this BusinessSummaryResultsObject.
        :rtype: List[BusinessSummary]
        """
        return self._business

    @business.setter
    def business(self, business: List[BusinessSummary]):
        """Sets the business of this BusinessSummaryResultsObject.


        :param business: The business of this BusinessSummaryResultsObject.
        :type business: List[BusinessSummary]
        """

        self._business = business

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this BusinessSummaryResultsObject.


        :return: The metadata of this BusinessSummaryResultsObject.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this BusinessSummaryResultsObject.


        :param metadata: The metadata of this BusinessSummaryResultsObject.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
