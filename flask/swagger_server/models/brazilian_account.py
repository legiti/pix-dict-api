# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class BrazilianAccount(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, participant: AllOfBrazilianAccountParticipant=None, branch: str=None, account_number: str=None, account_type: str=None, opening_date: datetime=None):  # noqa: E501
        """BrazilianAccount - a model defined in Swagger

        :param participant: The participant of this BrazilianAccount.  # noqa: E501
        :type participant: AllOfBrazilianAccountParticipant
        :param branch: The branch of this BrazilianAccount.  # noqa: E501
        :type branch: str
        :param account_number: The account_number of this BrazilianAccount.  # noqa: E501
        :type account_number: str
        :param account_type: The account_type of this BrazilianAccount.  # noqa: E501
        :type account_type: str
        :param opening_date: The opening_date of this BrazilianAccount.  # noqa: E501
        :type opening_date: datetime
        """
        self.swagger_types = {
            'participant': AllOfBrazilianAccountParticipant,
            'branch': str,
            'account_number': str,
            'account_type': str,
            'opening_date': datetime
        }

        self.attribute_map = {
            'participant': 'Participant',
            'branch': 'Branch',
            'account_number': 'AccountNumber',
            'account_type': 'AccountType',
            'opening_date': 'OpeningDate'
        }
        self._participant = participant
        self._branch = branch
        self._account_number = account_number
        self._account_type = account_type
        self._opening_date = opening_date

    @classmethod
    def from_dict(cls, dikt) -> 'BrazilianAccount':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BrazilianAccount of this BrazilianAccount.  # noqa: E501
        :rtype: BrazilianAccount
        """
        return util.deserialize_model(dikt, cls)

    @property
    def participant(self) -> AllOfBrazilianAccountParticipant:
        """Gets the participant of this BrazilianAccount.


        :return: The participant of this BrazilianAccount.
        :rtype: AllOfBrazilianAccountParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant: AllOfBrazilianAccountParticipant):
        """Sets the participant of this BrazilianAccount.


        :param participant: The participant of this BrazilianAccount.
        :type participant: AllOfBrazilianAccountParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def branch(self) -> str:
        """Gets the branch of this BrazilianAccount.

        Agência, sem dígito verificador.  # noqa: E501

        :return: The branch of this BrazilianAccount.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this BrazilianAccount.

        Agência, sem dígito verificador.  # noqa: E501

        :param branch: The branch of this BrazilianAccount.
        :type branch: str
        """

        self._branch = branch

    @property
    def account_number(self) -> str:
        """Gets the account_number of this BrazilianAccount.

        Número de conta, incluindo verificador. Se verificador for letra, substituir por 0.  # noqa: E501

        :return: The account_number of this BrazilianAccount.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: str):
        """Sets the account_number of this BrazilianAccount.

        Número de conta, incluindo verificador. Se verificador for letra, substituir por 0.  # noqa: E501

        :param account_number: The account_number of this BrazilianAccount.
        :type account_number: str
        """
        if account_number is None:
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501

        self._account_number = account_number

    @property
    def account_type(self) -> str:
        """Gets the account_type of this BrazilianAccount.

        Tipo de conta, conforme dicionário de domínio para a mensagem pacs.008 do SPI.  # noqa: E501

        :return: The account_type of this BrazilianAccount.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type: str):
        """Sets the account_type of this BrazilianAccount.

        Tipo de conta, conforme dicionário de domínio para a mensagem pacs.008 do SPI.  # noqa: E501

        :param account_type: The account_type of this BrazilianAccount.
        :type account_type: str
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def opening_date(self) -> datetime:
        """Gets the opening_date of this BrazilianAccount.

        Data de abertura da conta. Para o horário, caso não seja conhecido, convenciona-se o início do dia em BRT  # noqa: E501

        :return: The opening_date of this BrazilianAccount.
        :rtype: datetime
        """
        return self._opening_date

    @opening_date.setter
    def opening_date(self, opening_date: datetime):
        """Sets the opening_date of this BrazilianAccount.

        Data de abertura da conta. Para o horário, caso não seja conhecido, convenciona-se o início do dia em BRT  # noqa: E501

        :param opening_date: The opening_date of this BrazilianAccount.
        :type opening_date: datetime
        """
        if opening_date is None:
            raise ValueError("Invalid value for `opening_date`, must not be `None`")  # noqa: E501

        self._opening_date = opening_date
