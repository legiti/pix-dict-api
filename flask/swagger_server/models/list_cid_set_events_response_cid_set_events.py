# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
import re  # noqa: F401,E501
from swagger_server import util


class ListCidSetEventsResponseCidSetEvents(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, cid: str=None, timestamp: datetime=None):  # noqa: E501
        """ListCidSetEventsResponseCidSetEvents - a model defined in Swagger

        :param type: The type of this ListCidSetEventsResponseCidSetEvents.  # noqa: E501
        :type type: str
        :param cid: The cid of this ListCidSetEventsResponseCidSetEvents.  # noqa: E501
        :type cid: str
        :param timestamp: The timestamp of this ListCidSetEventsResponseCidSetEvents.  # noqa: E501
        :type timestamp: datetime
        """
        self.swagger_types = {
            'type': str,
            'cid': str,
            'timestamp': datetime
        }

        self.attribute_map = {
            'type': 'Type',
            'cid': 'Cid',
            'timestamp': 'Timestamp'
        }
        self._type = type
        self._cid = cid
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'ListCidSetEventsResponseCidSetEvents':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListCidSetEventsResponse_CidSetEvents of this ListCidSetEventsResponseCidSetEvents.  # noqa: E501
        :rtype: ListCidSetEventsResponseCidSetEvents
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ListCidSetEventsResponseCidSetEvents.


        :return: The type of this ListCidSetEventsResponseCidSetEvents.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ListCidSetEventsResponseCidSetEvents.


        :param type: The type of this ListCidSetEventsResponseCidSetEvents.
        :type type: str
        """
        allowed_values = ["ADDED", "REMOVED"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def cid(self) -> str:
        """Gets the cid of this ListCidSetEventsResponseCidSetEvents.

        Identificador de conteúdo  # noqa: E501

        :return: The cid of this ListCidSetEventsResponseCidSetEvents.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid: str):
        """Sets the cid of this ListCidSetEventsResponseCidSetEvents.

        Identificador de conteúdo  # noqa: E501

        :param cid: The cid of this ListCidSetEventsResponseCidSetEvents.
        :type cid: str
        """

        self._cid = cid

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this ListCidSetEventsResponseCidSetEvents.

        Data-hora do evento  # noqa: E501

        :return: The timestamp of this ListCidSetEventsResponseCidSetEvents.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this ListCidSetEventsResponseCidSetEvents.

        Data-hora do evento  # noqa: E501

        :param timestamp: The timestamp of this ListCidSetEventsResponseCidSetEvents.
        :type timestamp: datetime
        """

        self._timestamp = timestamp
