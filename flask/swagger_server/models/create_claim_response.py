# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class CreateClaimResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, claim: AllOfCreateClaimResponseClaim=None):  # noqa: E501
        """CreateClaimResponse - a model defined in Swagger

        :param signature: The signature of this CreateClaimResponse.  # noqa: E501
        :type signature: object
        :param claim: The claim of this CreateClaimResponse.  # noqa: E501
        :type claim: AllOfCreateClaimResponseClaim
        """
        self.swagger_types = {
            'signature': object,
            'claim': AllOfCreateClaimResponseClaim
        }

        self.attribute_map = {
            'signature': 'Signature',
            'claim': 'Claim'
        }
        self._signature = signature
        self._claim = claim

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClaimResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClaimResponse of this CreateClaimResponse.  # noqa: E501
        :rtype: CreateClaimResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this CreateClaimResponse.


        :return: The signature of this CreateClaimResponse.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this CreateClaimResponse.


        :param signature: The signature of this CreateClaimResponse.
        :type signature: object
        """

        self._signature = signature

    @property
    def claim(self) -> AllOfCreateClaimResponseClaim:
        """Gets the claim of this CreateClaimResponse.


        :return: The claim of this CreateClaimResponse.
        :rtype: AllOfCreateClaimResponseClaim
        """
        return self._claim

    @claim.setter
    def claim(self, claim: AllOfCreateClaimResponseClaim):
        """Sets the claim of this CreateClaimResponse.


        :param claim: The claim of this CreateClaimResponse.
        :type claim: AllOfCreateClaimResponseClaim
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501

        self._claim = claim
