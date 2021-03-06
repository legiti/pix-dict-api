# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.entryproperties_key_type import EntrypropertiesKeyType  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class CreateCidSetFileResponseCidSetFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, status: AllOfCreateCidSetFileResponseCidSetFileStatus=None, participant: AllOfCreateCidSetFileResponseCidSetFileParticipant=None, key_type: EntrypropertiesKeyType=None, request_time: datetime=None, creation_time: datetime=None, url: str=None, bytes: int=None, sha256: str=None):  # noqa: E501
        """CreateCidSetFileResponseCidSetFile - a model defined in Swagger

        :param id: The id of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type id: int
        :param status: The status of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type status: AllOfCreateCidSetFileResponseCidSetFileStatus
        :param participant: The participant of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type participant: AllOfCreateCidSetFileResponseCidSetFileParticipant
        :param key_type: The key_type of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type key_type: EntrypropertiesKeyType
        :param request_time: The request_time of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type request_time: datetime
        :param creation_time: The creation_time of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type creation_time: datetime
        :param url: The url of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type url: str
        :param bytes: The bytes of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type bytes: int
        :param sha256: The sha256 of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :type sha256: str
        """
        self.swagger_types = {
            'id': int,
            'status': AllOfCreateCidSetFileResponseCidSetFileStatus,
            'participant': AllOfCreateCidSetFileResponseCidSetFileParticipant,
            'key_type': EntrypropertiesKeyType,
            'request_time': datetime,
            'creation_time': datetime,
            'url': str,
            'bytes': int,
            'sha256': str
        }

        self.attribute_map = {
            'id': 'Id',
            'status': 'Status',
            'participant': 'Participant',
            'key_type': 'KeyType',
            'request_time': 'RequestTime',
            'creation_time': 'CreationTime',
            'url': 'Url',
            'bytes': 'Bytes',
            'sha256': 'Sha256'
        }
        self._id = id
        self._status = status
        self._participant = participant
        self._key_type = key_type
        self._request_time = request_time
        self._creation_time = creation_time
        self._url = url
        self._bytes = bytes
        self._sha256 = sha256

    @classmethod
    def from_dict(cls, dikt) -> 'CreateCidSetFileResponseCidSetFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateCidSetFileResponse_CidSetFile of this CreateCidSetFileResponseCidSetFile.  # noqa: E501
        :rtype: CreateCidSetFileResponseCidSetFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this CreateCidSetFileResponseCidSetFile.


        :return: The id of this CreateCidSetFileResponseCidSetFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CreateCidSetFileResponseCidSetFile.


        :param id: The id of this CreateCidSetFileResponseCidSetFile.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self) -> AllOfCreateCidSetFileResponseCidSetFileStatus:
        """Gets the status of this CreateCidSetFileResponseCidSetFile.


        :return: The status of this CreateCidSetFileResponseCidSetFile.
        :rtype: AllOfCreateCidSetFileResponseCidSetFileStatus
        """
        return self._status

    @status.setter
    def status(self, status: AllOfCreateCidSetFileResponseCidSetFileStatus):
        """Sets the status of this CreateCidSetFileResponseCidSetFile.


        :param status: The status of this CreateCidSetFileResponseCidSetFile.
        :type status: AllOfCreateCidSetFileResponseCidSetFileStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def participant(self) -> AllOfCreateCidSetFileResponseCidSetFileParticipant:
        """Gets the participant of this CreateCidSetFileResponseCidSetFile.


        :return: The participant of this CreateCidSetFileResponseCidSetFile.
        :rtype: AllOfCreateCidSetFileResponseCidSetFileParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant: AllOfCreateCidSetFileResponseCidSetFileParticipant):
        """Sets the participant of this CreateCidSetFileResponseCidSetFile.


        :param participant: The participant of this CreateCidSetFileResponseCidSetFile.
        :type participant: AllOfCreateCidSetFileResponseCidSetFileParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def key_type(self) -> EntrypropertiesKeyType:
        """Gets the key_type of this CreateCidSetFileResponseCidSetFile.


        :return: The key_type of this CreateCidSetFileResponseCidSetFile.
        :rtype: EntrypropertiesKeyType
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type: EntrypropertiesKeyType):
        """Sets the key_type of this CreateCidSetFileResponseCidSetFile.


        :param key_type: The key_type of this CreateCidSetFileResponseCidSetFile.
        :type key_type: EntrypropertiesKeyType
        """
        if key_type is None:
            raise ValueError("Invalid value for `key_type`, must not be `None`")  # noqa: E501

        self._key_type = key_type

    @property
    def request_time(self) -> datetime:
        """Gets the request_time of this CreateCidSetFileResponseCidSetFile.

        Data-hora de solicitação da geração do arquivo.  # noqa: E501

        :return: The request_time of this CreateCidSetFileResponseCidSetFile.
        :rtype: datetime
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time: datetime):
        """Sets the request_time of this CreateCidSetFileResponseCidSetFile.

        Data-hora de solicitação da geração do arquivo.  # noqa: E501

        :param request_time: The request_time of this CreateCidSetFileResponseCidSetFile.
        :type request_time: datetime
        """
        if request_time is None:
            raise ValueError("Invalid value for `request_time`, must not be `None`")  # noqa: E501

        self._request_time = request_time

    @property
    def creation_time(self) -> datetime:
        """Gets the creation_time of this CreateCidSetFileResponseCidSetFile.

        Data-hora em que o arquivo foi gerado. Presente quando status for `AVAILABLE`.  # noqa: E501

        :return: The creation_time of this CreateCidSetFileResponseCidSetFile.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time: datetime):
        """Sets the creation_time of this CreateCidSetFileResponseCidSetFile.

        Data-hora em que o arquivo foi gerado. Presente quando status for `AVAILABLE`.  # noqa: E501

        :param creation_time: The creation_time of this CreateCidSetFileResponseCidSetFile.
        :type creation_time: datetime
        """

        self._creation_time = creation_time

    @property
    def url(self) -> str:
        """Gets the url of this CreateCidSetFileResponseCidSetFile.

        URL para download do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :return: The url of this CreateCidSetFileResponseCidSetFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this CreateCidSetFileResponseCidSetFile.

        URL para download do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :param url: The url of this CreateCidSetFileResponseCidSetFile.
        :type url: str
        """

        self._url = url

    @property
    def bytes(self) -> int:
        """Gets the bytes of this CreateCidSetFileResponseCidSetFile.

        Tamanho do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :return: The bytes of this CreateCidSetFileResponseCidSetFile.
        :rtype: int
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes: int):
        """Sets the bytes of this CreateCidSetFileResponseCidSetFile.

        Tamanho do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :param bytes: The bytes of this CreateCidSetFileResponseCidSetFile.
        :type bytes: int
        """

        self._bytes = bytes

    @property
    def sha256(self) -> str:
        """Gets the sha256 of this CreateCidSetFileResponseCidSetFile.

        SHA256 do conteúdo do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :return: The sha256 of this CreateCidSetFileResponseCidSetFile.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256: str):
        """Sets the sha256 of this CreateCidSetFileResponseCidSetFile.

        SHA256 do conteúdo do arquivo. Presente quando status for `AVAILABLE`.  # noqa: E501

        :param sha256: The sha256 of this CreateCidSetFileResponseCidSetFile.
        :type sha256: str
        """

        self._sha256 = sha256
