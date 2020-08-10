# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class CreateSyncVerificationResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, sync_verification: AllOfCreateSyncVerificationResponseSyncVerification=None):  # noqa: E501
        """CreateSyncVerificationResponse - a model defined in Swagger

        :param signature: The signature of this CreateSyncVerificationResponse.  # noqa: E501
        :type signature: object
        :param sync_verification: The sync_verification of this CreateSyncVerificationResponse.  # noqa: E501
        :type sync_verification: AllOfCreateSyncVerificationResponseSyncVerification
        """
        self.swagger_types = {
            'signature': object,
            'sync_verification': AllOfCreateSyncVerificationResponseSyncVerification
        }

        self.attribute_map = {
            'signature': 'Signature',
            'sync_verification': 'SyncVerification'
        }
        self._signature = signature
        self._sync_verification = sync_verification

    @classmethod
    def from_dict(cls, dikt) -> 'CreateSyncVerificationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateSyncVerificationResponse of this CreateSyncVerificationResponse.  # noqa: E501
        :rtype: CreateSyncVerificationResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this CreateSyncVerificationResponse.


        :return: The signature of this CreateSyncVerificationResponse.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this CreateSyncVerificationResponse.


        :param signature: The signature of this CreateSyncVerificationResponse.
        :type signature: object
        """

        self._signature = signature

    @property
    def sync_verification(self) -> AllOfCreateSyncVerificationResponseSyncVerification:
        """Gets the sync_verification of this CreateSyncVerificationResponse.


        :return: The sync_verification of this CreateSyncVerificationResponse.
        :rtype: AllOfCreateSyncVerificationResponseSyncVerification
        """
        return self._sync_verification

    @sync_verification.setter
    def sync_verification(self, sync_verification: AllOfCreateSyncVerificationResponseSyncVerification):
        """Sets the sync_verification of this CreateSyncVerificationResponse.


        :param sync_verification: The sync_verification of this CreateSyncVerificationResponse.
        :type sync_verification: AllOfCreateSyncVerificationResponseSyncVerification
        """
        if sync_verification is None:
            raise ValueError("Invalid value for `sync_verification`, must not be `None`")  # noqa: E501

        self._sync_verification = sync_verification