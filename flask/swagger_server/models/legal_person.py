# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class LegalPerson(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str='LEGAL_PERSON', tax_id_number: str=None, name: str=None, trade_name: str=None):  # noqa: E501
        """LegalPerson - a model defined in Swagger

        :param type: The type of this LegalPerson.  # noqa: E501
        :type type: str
        :param tax_id_number: The tax_id_number of this LegalPerson.  # noqa: E501
        :type tax_id_number: str
        :param name: The name of this LegalPerson.  # noqa: E501
        :type name: str
        :param trade_name: The trade_name of this LegalPerson.  # noqa: E501
        :type trade_name: str
        """
        self.swagger_types = {
            'type': str,
            'tax_id_number': str,
            'name': str,
            'trade_name': str
        }

        self.attribute_map = {
            'type': 'Type',
            'tax_id_number': 'TaxIdNumber',
            'name': 'Name',
            'trade_name': 'TradeName'
        }
        self._type = type
        self._tax_id_number = tax_id_number
        self._name = name
        self._trade_name = trade_name

    @classmethod
    def from_dict(cls, dikt) -> 'LegalPerson':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LegalPerson of this LegalPerson.  # noqa: E501
        :rtype: LegalPerson
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this LegalPerson.


        :return: The type of this LegalPerson.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this LegalPerson.


        :param type: The type of this LegalPerson.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def tax_id_number(self) -> str:
        """Gets the tax_id_number of this LegalPerson.

        CNPJ - Cadastro Nacional de Pessoa Jurídica  # noqa: E501

        :return: The tax_id_number of this LegalPerson.
        :rtype: str
        """
        return self._tax_id_number

    @tax_id_number.setter
    def tax_id_number(self, tax_id_number: str):
        """Sets the tax_id_number of this LegalPerson.

        CNPJ - Cadastro Nacional de Pessoa Jurídica  # noqa: E501

        :param tax_id_number: The tax_id_number of this LegalPerson.
        :type tax_id_number: str
        """
        if tax_id_number is None:
            raise ValueError("Invalid value for `tax_id_number`, must not be `None`")  # noqa: E501

        self._tax_id_number = tax_id_number

    @property
    def name(self) -> str:
        """Gets the name of this LegalPerson.

        Razão social.  # noqa: E501

        :return: The name of this LegalPerson.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this LegalPerson.

        Razão social.  # noqa: E501

        :param name: The name of this LegalPerson.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def trade_name(self) -> str:
        """Gets the trade_name of this LegalPerson.

        Nome fantasia.  # noqa: E501

        :return: The trade_name of this LegalPerson.
        :rtype: str
        """
        return self._trade_name

    @trade_name.setter
    def trade_name(self, trade_name: str):
        """Sets the trade_name of this LegalPerson.

        Nome fantasia.  # noqa: E501

        :param trade_name: The trade_name of this LegalPerson.
        :type trade_name: str
        """

        self._trade_name = trade_name
