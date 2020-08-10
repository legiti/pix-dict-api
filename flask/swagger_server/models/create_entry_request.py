# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.complete_claim_requestproperties_request_id import CompleteClaimRequestpropertiesRequestId  # noqa: F401,E501
from swagger_server.models.extended_entryall_of0 import ExtendedEntryallOf0  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class CreateEntryRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, entry: ExtendedEntryallOf0=None, reason: AllOfCreateEntryRequestReason=None, request_id: CompleteClaimRequestpropertiesRequestId=None):  # noqa: E501
        """CreateEntryRequest - a model defined in Swagger

        :param signature: The signature of this CreateEntryRequest.  # noqa: E501
        :type signature: object
        :param entry: The entry of this CreateEntryRequest.  # noqa: E501
        :type entry: ExtendedEntryallOf0
        :param reason: The reason of this CreateEntryRequest.  # noqa: E501
        :type reason: AllOfCreateEntryRequestReason
        :param request_id: The request_id of this CreateEntryRequest.  # noqa: E501
        :type request_id: CompleteClaimRequestpropertiesRequestId
        """
        self.swagger_types = {
            'signature': object,
            'entry': ExtendedEntryallOf0,
            'reason': AllOfCreateEntryRequestReason,
            'request_id': CompleteClaimRequestpropertiesRequestId
        }

        self.attribute_map = {
            'signature': 'Signature',
            'entry': 'Entry',
            'reason': 'Reason',
            'request_id': 'RequestId'
        }
        self._signature = signature
        self._entry = entry
        self._reason = reason
        self._request_id = request_id

    @classmethod
    def from_dict(cls, dikt) -> 'CreateEntryRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateEntryRequest of this CreateEntryRequest.  # noqa: E501
        :rtype: CreateEntryRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this CreateEntryRequest.


        :return: The signature of this CreateEntryRequest.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this CreateEntryRequest.


        :param signature: The signature of this CreateEntryRequest.
        :type signature: object
        """

        self._signature = signature

    @property
    def entry(self) -> ExtendedEntryallOf0:
        """Gets the entry of this CreateEntryRequest.


        :return: The entry of this CreateEntryRequest.
        :rtype: ExtendedEntryallOf0
        """
        return self._entry

    @entry.setter
    def entry(self, entry: ExtendedEntryallOf0):
        """Sets the entry of this CreateEntryRequest.


        :param entry: The entry of this CreateEntryRequest.
        :type entry: ExtendedEntryallOf0
        """
        if entry is None:
            raise ValueError("Invalid value for `entry`, must not be `None`")  # noqa: E501

        self._entry = entry

    @property
    def reason(self) -> AllOfCreateEntryRequestReason:
        """Gets the reason of this CreateEntryRequest.


        :return: The reason of this CreateEntryRequest.
        :rtype: AllOfCreateEntryRequestReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason: AllOfCreateEntryRequestReason):
        """Sets the reason of this CreateEntryRequest.


        :param reason: The reason of this CreateEntryRequest.
        :type reason: AllOfCreateEntryRequestReason
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def request_id(self) -> CompleteClaimRequestpropertiesRequestId:
        """Gets the request_id of this CreateEntryRequest.


        :return: The request_id of this CreateEntryRequest.
        :rtype: CompleteClaimRequestpropertiesRequestId
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: CompleteClaimRequestpropertiesRequestId):
        """Sets the request_id of this CreateEntryRequest.


        :param request_id: The request_id of this CreateEntryRequest.
        :type request_id: CompleteClaimRequestpropertiesRequestId
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id