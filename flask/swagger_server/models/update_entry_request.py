# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.entryproperties_account import EntrypropertiesAccount  # noqa: F401,E501
from swagger_server.models.entryproperties_key import EntrypropertiesKey  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class UpdateEntryRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, key: EntrypropertiesKey=None, account: EntrypropertiesAccount=None, reason: AllOfUpdateEntryRequestReason=None):  # noqa: E501
        """UpdateEntryRequest - a model defined in Swagger

        :param signature: The signature of this UpdateEntryRequest.  # noqa: E501
        :type signature: object
        :param key: The key of this UpdateEntryRequest.  # noqa: E501
        :type key: EntrypropertiesKey
        :param account: The account of this UpdateEntryRequest.  # noqa: E501
        :type account: EntrypropertiesAccount
        :param reason: The reason of this UpdateEntryRequest.  # noqa: E501
        :type reason: AllOfUpdateEntryRequestReason
        """
        self.swagger_types = {
            'signature': object,
            'key': EntrypropertiesKey,
            'account': EntrypropertiesAccount,
            'reason': AllOfUpdateEntryRequestReason
        }

        self.attribute_map = {
            'signature': 'Signature',
            'key': 'Key',
            'account': 'Account',
            'reason': 'Reason'
        }
        self._signature = signature
        self._key = key
        self._account = account
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateEntryRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateEntryRequest of this UpdateEntryRequest.  # noqa: E501
        :rtype: UpdateEntryRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this UpdateEntryRequest.


        :return: The signature of this UpdateEntryRequest.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this UpdateEntryRequest.


        :param signature: The signature of this UpdateEntryRequest.
        :type signature: object
        """

        self._signature = signature

    @property
    def key(self) -> EntrypropertiesKey:
        """Gets the key of this UpdateEntryRequest.


        :return: The key of this UpdateEntryRequest.
        :rtype: EntrypropertiesKey
        """
        return self._key

    @key.setter
    def key(self, key: EntrypropertiesKey):
        """Sets the key of this UpdateEntryRequest.


        :param key: The key of this UpdateEntryRequest.
        :type key: EntrypropertiesKey
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def account(self) -> EntrypropertiesAccount:
        """Gets the account of this UpdateEntryRequest.


        :return: The account of this UpdateEntryRequest.
        :rtype: EntrypropertiesAccount
        """
        return self._account

    @account.setter
    def account(self, account: EntrypropertiesAccount):
        """Sets the account of this UpdateEntryRequest.


        :param account: The account of this UpdateEntryRequest.
        :type account: EntrypropertiesAccount
        """
        if account is None:
            raise ValueError("Invalid value for `account`, must not be `None`")  # noqa: E501

        self._account = account

    @property
    def reason(self) -> AllOfUpdateEntryRequestReason:
        """Gets the reason of this UpdateEntryRequest.


        :return: The reason of this UpdateEntryRequest.
        :rtype: AllOfUpdateEntryRequestReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason: AllOfUpdateEntryRequestReason):
        """Sets the reason of this UpdateEntryRequest.


        :param reason: The reason of this UpdateEntryRequest.
        :type reason: AllOfUpdateEntryRequestReason
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason
