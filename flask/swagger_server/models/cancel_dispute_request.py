# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class CancelDisputeRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, dispute_id: str=None, participant: AllOfCancelDisputeRequestParticipant=None):  # noqa: E501
        """CancelDisputeRequest - a model defined in Swagger

        :param signature: The signature of this CancelDisputeRequest.  # noqa: E501
        :type signature: object
        :param dispute_id: The dispute_id of this CancelDisputeRequest.  # noqa: E501
        :type dispute_id: str
        :param participant: The participant of this CancelDisputeRequest.  # noqa: E501
        :type participant: AllOfCancelDisputeRequestParticipant
        """
        self.swagger_types = {
            'signature': object,
            'dispute_id': str,
            'participant': AllOfCancelDisputeRequestParticipant
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
    def from_dict(cls, dikt) -> 'CancelDisputeRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CancelDisputeRequest of this CancelDisputeRequest.  # noqa: E501
        :rtype: CancelDisputeRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this CancelDisputeRequest.


        :return: The signature of this CancelDisputeRequest.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this CancelDisputeRequest.


        :param signature: The signature of this CancelDisputeRequest.
        :type signature: object
        """

        self._signature = signature

    @property
    def dispute_id(self) -> str:
        """Gets the dispute_id of this CancelDisputeRequest.

        ID da disputa  # noqa: E501

        :return: The dispute_id of this CancelDisputeRequest.
        :rtype: str
        """
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, dispute_id: str):
        """Sets the dispute_id of this CancelDisputeRequest.

        ID da disputa  # noqa: E501

        :param dispute_id: The dispute_id of this CancelDisputeRequest.
        :type dispute_id: str
        """

        self._dispute_id = dispute_id

    @property
    def participant(self) -> AllOfCancelDisputeRequestParticipant:
        """Gets the participant of this CancelDisputeRequest.


        :return: The participant of this CancelDisputeRequest.
        :rtype: AllOfCancelDisputeRequestParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant: AllOfCancelDisputeRequestParticipant):
        """Sets the participant of this CancelDisputeRequest.


        :param participant: The participant of this CancelDisputeRequest.
        :type participant: AllOfCancelDisputeRequestParticipant
        """

        self._participant = participant
