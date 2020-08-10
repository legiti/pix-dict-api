# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.create_claim_responseproperties_claim import CreateClaimResponsepropertiesClaim  # noqa: F401,E501
from swagger_server import util


class AcknowledgeClaimResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, claim: CreateClaimResponsepropertiesClaim=None):  # noqa: E501
        """AcknowledgeClaimResponse - a model defined in Swagger

        :param signature: The signature of this AcknowledgeClaimResponse.  # noqa: E501
        :type signature: object
        :param claim: The claim of this AcknowledgeClaimResponse.  # noqa: E501
        :type claim: CreateClaimResponsepropertiesClaim
        """
        self.swagger_types = {
            'signature': object,
            'claim': CreateClaimResponsepropertiesClaim
        }

        self.attribute_map = {
            'signature': 'Signature',
            'claim': 'Claim'
        }
        self._signature = signature
        self._claim = claim

    @classmethod
    def from_dict(cls, dikt) -> 'AcknowledgeClaimResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AcknowledgeClaimResponse of this AcknowledgeClaimResponse.  # noqa: E501
        :rtype: AcknowledgeClaimResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this AcknowledgeClaimResponse.


        :return: The signature of this AcknowledgeClaimResponse.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this AcknowledgeClaimResponse.


        :param signature: The signature of this AcknowledgeClaimResponse.
        :type signature: object
        """

        self._signature = signature

    @property
    def claim(self) -> CreateClaimResponsepropertiesClaim:
        """Gets the claim of this AcknowledgeClaimResponse.


        :return: The claim of this AcknowledgeClaimResponse.
        :rtype: CreateClaimResponsepropertiesClaim
        """
        return self._claim

    @claim.setter
    def claim(self, claim: CreateClaimResponsepropertiesClaim):
        """Sets the claim of this AcknowledgeClaimResponse.


        :param claim: The claim of this AcknowledgeClaimResponse.
        :type claim: CreateClaimResponsepropertiesClaim
        """
        if claim is None:
            raise ValueError("Invalid value for `claim`, must not be `None`")  # noqa: E501

        self._claim = claim
