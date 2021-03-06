# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.extended_claimall_of0 import ExtendedClaimallOf0  # noqa: F401,E501
from swagger_server import util


class CreateClaimRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, claim: ExtendedClaimallOf0=None):  # noqa: E501
        """CreateClaimRequest - a model defined in Swagger

        :param signature: The signature of this CreateClaimRequest.  # noqa: E501
        :type signature: object
        :param claim: The claim of this CreateClaimRequest.  # noqa: E501
        :type claim: ExtendedClaimallOf0
        """
        self.swagger_types = {
            'signature': object,
            'claim': ExtendedClaimallOf0
        }

        self.attribute_map = {
            'signature': 'Signature',
            'claim': 'Claim'
        }
        self._signature = signature
        self._claim = claim

    @classmethod
    def from_dict(cls, dikt) -> 'CreateClaimRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateClaimRequest of this CreateClaimRequest.  # noqa: E501
        :rtype: CreateClaimRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this CreateClaimRequest.


        :return: The signature of this CreateClaimRequest.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this CreateClaimRequest.


        :param signature: The signature of this CreateClaimRequest.
        :type signature: object
        """

        self._signature = signature

    @property
    def claim(self) -> ExtendedClaimallOf0:
        """Gets the claim of this CreateClaimRequest.


        :return: The claim of this CreateClaimRequest.
        :rtype: ExtendedClaimallOf0
        """
        return self._claim

    @claim.setter
    def claim(self, claim: ExtendedClaimallOf0):
        """Sets the claim of this CreateClaimRequest.


        :param claim: The claim of this CreateClaimRequest.
        :type claim: ExtendedClaimallOf0
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501

        self._claim = claim
