# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.entryproperties_key_type import EntrypropertiesKeyType  # noqa: F401,E501
from swagger_server.models.list_cid_set_events_response_cid_set_events import ListCidSetEventsResponseCidSetEvents  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class ListCidSetEventsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, signature: object=None, has_more_elements: bool=None, participant: AllOfListCidSetEventsResponseParticipant=None, key_type: EntrypropertiesKeyType=None, start_time: datetime=None, end_time: datetime=None, sync_verifier_start: AllOfListCidSetEventsResponseSyncVerifierStart=None, sync_verifier_end: AllOfListCidSetEventsResponseSyncVerifierEnd=None, cid_set_events: List[ListCidSetEventsResponseCidSetEvents]=None):  # noqa: E501
        """ListCidSetEventsResponse - a model defined in Swagger

        :param signature: The signature of this ListCidSetEventsResponse.  # noqa: E501
        :type signature: object
        :param has_more_elements: The has_more_elements of this ListCidSetEventsResponse.  # noqa: E501
        :type has_more_elements: bool
        :param participant: The participant of this ListCidSetEventsResponse.  # noqa: E501
        :type participant: AllOfListCidSetEventsResponseParticipant
        :param key_type: The key_type of this ListCidSetEventsResponse.  # noqa: E501
        :type key_type: EntrypropertiesKeyType
        :param start_time: The start_time of this ListCidSetEventsResponse.  # noqa: E501
        :type start_time: datetime
        :param end_time: The end_time of this ListCidSetEventsResponse.  # noqa: E501
        :type end_time: datetime
        :param sync_verifier_start: The sync_verifier_start of this ListCidSetEventsResponse.  # noqa: E501
        :type sync_verifier_start: AllOfListCidSetEventsResponseSyncVerifierStart
        :param sync_verifier_end: The sync_verifier_end of this ListCidSetEventsResponse.  # noqa: E501
        :type sync_verifier_end: AllOfListCidSetEventsResponseSyncVerifierEnd
        :param cid_set_events: The cid_set_events of this ListCidSetEventsResponse.  # noqa: E501
        :type cid_set_events: List[ListCidSetEventsResponseCidSetEvents]
        """
        self.swagger_types = {
            'signature': object,
            'has_more_elements': bool,
            'participant': AllOfListCidSetEventsResponseParticipant,
            'key_type': EntrypropertiesKeyType,
            'start_time': datetime,
            'end_time': datetime,
            'sync_verifier_start': AllOfListCidSetEventsResponseSyncVerifierStart,
            'sync_verifier_end': AllOfListCidSetEventsResponseSyncVerifierEnd,
            'cid_set_events': List[ListCidSetEventsResponseCidSetEvents]
        }

        self.attribute_map = {
            'signature': 'Signature',
            'has_more_elements': 'HasMoreElements',
            'participant': 'Participant',
            'key_type': 'KeyType',
            'start_time': 'StartTime',
            'end_time': 'EndTime',
            'sync_verifier_start': 'SyncVerifierStart',
            'sync_verifier_end': 'SyncVerifierEnd',
            'cid_set_events': 'CidSetEvents'
        }
        self._signature = signature
        self._has_more_elements = has_more_elements
        self._participant = participant
        self._key_type = key_type
        self._start_time = start_time
        self._end_time = end_time
        self._sync_verifier_start = sync_verifier_start
        self._sync_verifier_end = sync_verifier_end
        self._cid_set_events = cid_set_events

    @classmethod
    def from_dict(cls, dikt) -> 'ListCidSetEventsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListCidSetEventsResponse of this ListCidSetEventsResponse.  # noqa: E501
        :rtype: ListCidSetEventsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def signature(self) -> object:
        """Gets the signature of this ListCidSetEventsResponse.


        :return: The signature of this ListCidSetEventsResponse.
        :rtype: object
        """
        return self._signature

    @signature.setter
    def signature(self, signature: object):
        """Sets the signature of this ListCidSetEventsResponse.


        :param signature: The signature of this ListCidSetEventsResponse.
        :type signature: object
        """

        self._signature = signature

    @property
    def has_more_elements(self) -> bool:
        """Gets the has_more_elements of this ListCidSetEventsResponse.

        Existem mais elementos para iterar  # noqa: E501

        :return: The has_more_elements of this ListCidSetEventsResponse.
        :rtype: bool
        """
        return self._has_more_elements

    @has_more_elements.setter
    def has_more_elements(self, has_more_elements: bool):
        """Sets the has_more_elements of this ListCidSetEventsResponse.

        Existem mais elementos para iterar  # noqa: E501

        :param has_more_elements: The has_more_elements of this ListCidSetEventsResponse.
        :type has_more_elements: bool
        """

        self._has_more_elements = has_more_elements

    @property
    def participant(self) -> AllOfListCidSetEventsResponseParticipant:
        """Gets the participant of this ListCidSetEventsResponse.


        :return: The participant of this ListCidSetEventsResponse.
        :rtype: AllOfListCidSetEventsResponseParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant: AllOfListCidSetEventsResponseParticipant):
        """Sets the participant of this ListCidSetEventsResponse.


        :param participant: The participant of this ListCidSetEventsResponse.
        :type participant: AllOfListCidSetEventsResponseParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def key_type(self) -> EntrypropertiesKeyType:
        """Gets the key_type of this ListCidSetEventsResponse.


        :return: The key_type of this ListCidSetEventsResponse.
        :rtype: EntrypropertiesKeyType
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type: EntrypropertiesKeyType):
        """Sets the key_type of this ListCidSetEventsResponse.


        :param key_type: The key_type of this ListCidSetEventsResponse.
        :type key_type: EntrypropertiesKeyType
        """
        if key_type is None:
            raise ValueError("Invalid value for `key_type`, must not be `None`")  # noqa: E501

        self._key_type = key_type

    @property
    def start_time(self) -> datetime:
        """Gets the start_time of this ListCidSetEventsResponse.

        Data-hora do primeiro evento da lista  # noqa: E501

        :return: The start_time of this ListCidSetEventsResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        """Sets the start_time of this ListCidSetEventsResponse.

        Data-hora do primeiro evento da lista  # noqa: E501

        :param start_time: The start_time of this ListCidSetEventsResponse.
        :type start_time: datetime
        """
        if start_time is None:
            raise ValueError("Invalid value for `start_time`, must not be `None`")  # noqa: E501

        self._start_time = start_time

    @property
    def end_time(self) -> datetime:
        """Gets the end_time of this ListCidSetEventsResponse.

        Data-hora do último evento da lista  # noqa: E501

        :return: The end_time of this ListCidSetEventsResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        """Sets the end_time of this ListCidSetEventsResponse.

        Data-hora do último evento da lista  # noqa: E501

        :param end_time: The end_time of this ListCidSetEventsResponse.
        :type end_time: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def sync_verifier_start(self) -> AllOfListCidSetEventsResponseSyncVerifierStart:
        """Gets the sync_verifier_start of this ListCidSetEventsResponse.


        :return: The sync_verifier_start of this ListCidSetEventsResponse.
        :rtype: AllOfListCidSetEventsResponseSyncVerifierStart
        """
        return self._sync_verifier_start

    @sync_verifier_start.setter
    def sync_verifier_start(self, sync_verifier_start: AllOfListCidSetEventsResponseSyncVerifierStart):
        """Sets the sync_verifier_start of this ListCidSetEventsResponse.


        :param sync_verifier_start: The sync_verifier_start of this ListCidSetEventsResponse.
        :type sync_verifier_start: AllOfListCidSetEventsResponseSyncVerifierStart
        """
        if sync_verifier_start is None:
            raise ValueError("Invalid value for `sync_verifier_start`, must not be `None`")  # noqa: E501

        self._sync_verifier_start = sync_verifier_start

    @property
    def sync_verifier_end(self) -> AllOfListCidSetEventsResponseSyncVerifierEnd:
        """Gets the sync_verifier_end of this ListCidSetEventsResponse.


        :return: The sync_verifier_end of this ListCidSetEventsResponse.
        :rtype: AllOfListCidSetEventsResponseSyncVerifierEnd
        """
        return self._sync_verifier_end

    @sync_verifier_end.setter
    def sync_verifier_end(self, sync_verifier_end: AllOfListCidSetEventsResponseSyncVerifierEnd):
        """Sets the sync_verifier_end of this ListCidSetEventsResponse.


        :param sync_verifier_end: The sync_verifier_end of this ListCidSetEventsResponse.
        :type sync_verifier_end: AllOfListCidSetEventsResponseSyncVerifierEnd
        """
        if sync_verifier_end is None:
            raise ValueError("Invalid value for `sync_verifier_end`, must not be `None`")  # noqa: E501

        self._sync_verifier_end = sync_verifier_end

    @property
    def cid_set_events(self) -> List[ListCidSetEventsResponseCidSetEvents]:
        """Gets the cid_set_events of this ListCidSetEventsResponse.


        :return: The cid_set_events of this ListCidSetEventsResponse.
        :rtype: List[ListCidSetEventsResponseCidSetEvents]
        """
        return self._cid_set_events

    @cid_set_events.setter
    def cid_set_events(self, cid_set_events: List[ListCidSetEventsResponseCidSetEvents]):
        """Sets the cid_set_events of this ListCidSetEventsResponse.


        :param cid_set_events: The cid_set_events of this ListCidSetEventsResponse.
        :type cid_set_events: List[ListCidSetEventsResponseCidSetEvents]
        """

        self._cid_set_events = cid_set_events
