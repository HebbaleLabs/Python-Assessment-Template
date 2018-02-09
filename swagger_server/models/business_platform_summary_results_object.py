# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.business_platform_summary import BusinessPlatformSummary  # noqa: F401,E501
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server import util


class BusinessPlatformSummaryResultsObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, business_platform: List[BusinessPlatformSummary]=None, metadata: Metadata=None):  # noqa: E501
        """BusinessPlatformSummaryResultsObject - a model defined in Swagger

        :param business_platform: The business_platform of this BusinessPlatformSummaryResultsObject.  # noqa: E501
        :type business_platform: List[BusinessPlatformSummary]
        :param metadata: The metadata of this BusinessPlatformSummaryResultsObject.  # noqa: E501
        :type metadata: Metadata
        """
        self.swagger_types = {
            'business_platform': List[BusinessPlatformSummary],
            'metadata': Metadata
        }

        self.attribute_map = {
            'business_platform': 'businessPlatform',
            'metadata': 'metadata'
        }

        self._business_platform = business_platform
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'BusinessPlatformSummaryResultsObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BusinessPlatformSummaryResultsObject of this BusinessPlatformSummaryResultsObject.  # noqa: E501
        :rtype: BusinessPlatformSummaryResultsObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_platform(self) -> List[BusinessPlatformSummary]:
        """Gets the business_platform of this BusinessPlatformSummaryResultsObject.


        :return: The business_platform of this BusinessPlatformSummaryResultsObject.
        :rtype: List[BusinessPlatformSummary]
        """
        return self._business_platform

    @business_platform.setter
    def business_platform(self, business_platform: List[BusinessPlatformSummary]):
        """Sets the business_platform of this BusinessPlatformSummaryResultsObject.


        :param business_platform: The business_platform of this BusinessPlatformSummaryResultsObject.
        :type business_platform: List[BusinessPlatformSummary]
        """

        self._business_platform = business_platform

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this BusinessPlatformSummaryResultsObject.


        :return: The metadata of this BusinessPlatformSummaryResultsObject.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this BusinessPlatformSummaryResultsObject.


        :param metadata: The metadata of this BusinessPlatformSummaryResultsObject.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata