# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server.models.relationship import Relationship  # noqa: F401,E501
from swagger_server import util


class RelationshipResultsObject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, relationship: List[Relationship]=None, metadata: Metadata=None):  # noqa: E501
        """RelationshipResultsObject - a model defined in Swagger

        :param relationship: The relationship of this RelationshipResultsObject.  # noqa: E501
        :type relationship: List[Relationship]
        :param metadata: The metadata of this RelationshipResultsObject.  # noqa: E501
        :type metadata: Metadata
        """
        self.swagger_types = {
            'relationship': List[Relationship],
            'metadata': Metadata
        }

        self.attribute_map = {
            'relationship': 'relationship',
            'metadata': 'metadata'
        }

        self._relationship = relationship
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'RelationshipResultsObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RelationshipResultsObject of this RelationshipResultsObject.  # noqa: E501
        :rtype: RelationshipResultsObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def relationship(self) -> List[Relationship]:
        """Gets the relationship of this RelationshipResultsObject.


        :return: The relationship of this RelationshipResultsObject.
        :rtype: List[Relationship]
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship: List[Relationship]):
        """Sets the relationship of this RelationshipResultsObject.


        :param relationship: The relationship of this RelationshipResultsObject.
        :type relationship: List[Relationship]
        """

        self._relationship = relationship

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this RelationshipResultsObject.


        :return: The metadata of this RelationshipResultsObject.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this RelationshipResultsObject.


        :param metadata: The metadata of this RelationshipResultsObject.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata
