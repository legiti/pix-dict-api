# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class AcknowledgeDisputeRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, dispute_id: str=None, participant: AllOfAcknowledgeDisputeRequestParticipant=None):  # noqa: E501
        """AcknowledgeDisputeRequest - a model defined in Swagger

        :param signature: The signature of this AcknowledgeDisputeRequest.  # noqa: E501
        :type signature: object
        :param dispute_id: The dispute_id of this AcknowledgeDisputeRequest.  # noqa: E501
        :type dispute_id: str
        :param participant: The participant of this AcknowledgeDisputeRequest.  # noqa: E501
        :type participant: AllOfAcknowledgeDisputeRequestParticipant
        """
        self.swagger_types = {
            'signature': object,
            'dispute_id': str,
            'participant': AllOfAcknowledgeDisputeRequestParticipant
        }

        self.attribute_map = {
            'signature': 'Signature',
            'dispute_id': 'DisputeId',
            'participant': 'Participant'
        }
        self._signature = signature
        self._dispute_id = dispute_id
        self._participant = participant

    @classmethod
    def from_dict(cls, dikt) -> 'AcknowledgeDisputeRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AcknowledgeDisputeRequest of this AcknowledgeDisputeRequest.  # noqa: E501
        :rtype: AcknowledgeDisputeRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this AcknowledgeDisputeRequest.


        :return: The signature of this AcknowledgeDisputeRequest.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this AcknowledgeDisputeRequest.


        :param signature: The signature of this AcknowledgeDisputeRequest.
        :type signature: object
        """

        self._signature = signature

    @property
    def dispute_id(self) -> str:
        """Gets the dispute_id of this AcknowledgeDisputeRequest.

        ID da disputa  # noqa: E501

        :return: The dispute_id of this AcknowledgeDisputeRequest.
        :rtype: str
        """
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, dispute_id: str):
        """Sets the dispute_id of this AcknowledgeDisputeRequest.

        ID da disputa  # noqa: E501

        :param dispute_id: The dispute_id of this AcknowledgeDisputeRequest.
        :type dispute_id: str
        """

        self._dispute_id = dispute_id

    @property
    def participant(self) -> AllOfAcknowledgeDisputeRequestParticipant:
        """Gets the participant of this AcknowledgeDisputeRequest.


        :return: The participant of this AcknowledgeDisputeRequest.
        :rtype: AllOfAcknowledgeDisputeRequestParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant: AllOfAcknowledgeDisputeRequestParticipant):
        """Sets the participant of this AcknowledgeDisputeRequest.


        :param participant: The participant of this AcknowledgeDisputeRequest.
        :type participant: AllOfAcknowledgeDisputeRequestParticipant
        """

        self._participant = participant
