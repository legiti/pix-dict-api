# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class Dispute(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, disputed_transaction_id: str=None, reason: str=None, disputed_amount: str=None, details: Object=None):  # noqa: E501
        """Dispute - a model defined in Swagger

        :param disputed_transaction_id: The disputed_transaction_id of this Dispute.  # noqa: E501
        :type disputed_transaction_id: str
        :param reason: The reason of this Dispute.  # noqa: E501
        :type reason: str
        :param disputed_amount: The disputed_amount of this Dispute.  # noqa: E501
        :type disputed_amount: str
        :param details: The details of this Dispute.  # noqa: E501
        :type details: Object
        """
        self.swagger_types = {
            'disputed_transaction_id': str,
            'reason': str,
            'disputed_amount': str,
            'details': Object
        }

        self.attribute_map = {
            'disputed_transaction_id': 'DisputedTransactionId',
            'reason': 'Reason',
            'disputed_amount': 'DisputedAmount',
            'details': 'Details'
        }
        self._disputed_transaction_id = disputed_transaction_id
        self._reason = reason
        self._disputed_amount = disputed_amount
        self._details = details

    @classmethod
    def from_dict(cls, dikt) -> 'Dispute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dispute of this Dispute.  # noqa: E501
        :rtype: Dispute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def disputed_transaction_id(self) -> str:
        """Gets the disputed_transaction_id of this Dispute.

        Identificador da transação que está sendo disputada  # noqa: E501

        :return: The disputed_transaction_id of this Dispute.
        :rtype: str
        """
        return self._disputed_transaction_id

    @disputed_transaction_id.setter
    def disputed_transaction_id(self, disputed_transaction_id: str):
        """Sets the disputed_transaction_id of this Dispute.

        Identificador da transação que está sendo disputada  # noqa: E501

        :param disputed_transaction_id: The disputed_transaction_id of this Dispute.
        :type disputed_transaction_id: str
        """
        if disputed_transaction_id is None:
            raise ValueError("Invalid value for `disputed_transaction_id`, must not be `None`")  # noqa: E501

        self._disputed_transaction_id = disputed_transaction_id

    @property
    def reason(self) -> str:
        """Gets the reason of this Dispute.

        Motivo da disputa  # noqa: E501

        :return: The reason of this Dispute.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this Dispute.

        Motivo da disputa  # noqa: E501

        :param reason: The reason of this Dispute.
        :type reason: str
        """
        allowed_values = ["FRAUD", "ERROR", "AML_CTF", "USER_REQUESTED"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"
                .format(reason, allowed_values)
            )

        self._reason = reason

    @property
    def disputed_amount(self) -> str:
        """Gets the disputed_amount of this Dispute.


        :return: The disputed_amount of this Dispute.
        :rtype: str
        """
        return self._disputed_amount

    @disputed_amount.setter
    def disputed_amount(self, disputed_amount: str):
        """Sets the disputed_amount of this Dispute.


        :param disputed_amount: The disputed_amount of this Dispute.
        :type disputed_amount: str
        """
        if disputed_amount is None:
            raise ValueError("Invalid value for `disputed_amount`, must not be `None`")  # noqa: E501

        self._disputed_amount = disputed_amount

    @property
    def details(self) -> Object:
        """Gets the details of this Dispute.

        Detalhes que possam ajudar o participante recebedor a analisar a disputa  # noqa: E501

        :return: The details of this Dispute.
        :rtype: Object
        """
        return self._details

    @details.setter
    def details(self, details: Object):
        """Sets the details of this Dispute.

        Detalhes que possam ajudar o participante recebedor a analisar a disputa  # noqa: E501

        :param details: The details of this Dispute.
        :type details: Object
        """

        self._details = details
