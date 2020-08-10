# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.extended_dispute_resolution import ExtendedDisputeResolution  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class ExtendedDispute(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, status: str=None, payer_participant: Object=None, disputed_participant: Object=None, creation_time: datetime=None, last_modified: datetime=None, resolution: ExtendedDisputeResolution=None):  # noqa: E501
        """ExtendedDispute - a model defined in Swagger

        :param id: The id of this ExtendedDispute.  # noqa: E501
        :type id: str
        :param status: The status of this ExtendedDispute.  # noqa: E501
        :type status: str
        :param payer_participant: The payer_participant of this ExtendedDispute.  # noqa: E501
        :type payer_participant: Object
        :param disputed_participant: The disputed_participant of this ExtendedDispute.  # noqa: E501
        :type disputed_participant: Object
        :param creation_time: The creation_time of this ExtendedDispute.  # noqa: E501
        :type creation_time: datetime
        :param last_modified: The last_modified of this ExtendedDispute.  # noqa: E501
        :type last_modified: datetime
        :param resolution: The resolution of this ExtendedDispute.  # noqa: E501
        :type resolution: ExtendedDisputeResolution
        """
        self.swagger_types = {
            'id': str,
            'status': str,
            'payer_participant': Object,
            'disputed_participant': Object,
            'creation_time': datetime,
            'last_modified': datetime,
            'resolution': ExtendedDisputeResolution
        }

        self.attribute_map = {
            'id': 'Id',
            'status': 'Status',
            'payer_participant': 'PayerParticipant',
            'disputed_participant': 'DisputedParticipant',
            'creation_time': 'CreationTime',
            'last_modified': 'LastModified',
            'resolution': 'Resolution'
        }
        self._id = id
        self._status = status
        self._payer_participant = payer_participant
        self._disputed_participant = disputed_participant
        self._creation_time = creation_time
        self._last_modified = last_modified
        self._resolution = resolution

    @classmethod
    def from_dict(cls, dikt) -> 'ExtendedDispute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExtendedDispute of this ExtendedDispute.  # noqa: E501
        :rtype: ExtendedDispute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this ExtendedDispute.


        :return: The id of this ExtendedDispute.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this ExtendedDispute.


        :param id: The id of this ExtendedDispute.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self) -> str:
        """Gets the status of this ExtendedDispute.


        :return: The status of this ExtendedDispute.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this ExtendedDispute.


        :param status: The status of this ExtendedDispute.
        :type status: str
        """
        allowed_values = ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def payer_participant(self) -> Object:
        """Gets the payer_participant of this ExtendedDispute.


        :return: The payer_participant of this ExtendedDispute.
        :rtype: Object
        """
        return self._payer_participant

    @payer_participant.setter
    def payer_participant(self, payer_participant: Object):
        """Sets the payer_participant of this ExtendedDispute.


        :param payer_participant: The payer_participant of this ExtendedDispute.
        :type payer_participant: Object
        """
        if payer_participant is None:
            raise ValueError("Invalid value for `payer_participant`, must not be `None`")  # noqa: E501

        self._payer_participant = payer_participant

    @property
    def disputed_participant(self) -> Object:
        """Gets the disputed_participant of this ExtendedDispute.


        :return: The disputed_participant of this ExtendedDispute.
        :rtype: Object
        """
        return self._disputed_participant

    @disputed_participant.setter
    def disputed_participant(self, disputed_participant: Object):
        """Sets the disputed_participant of this ExtendedDispute.


        :param disputed_participant: The disputed_participant of this ExtendedDispute.
        :type disputed_participant: Object
        """
        if disputed_participant is None:
            raise ValueError("Invalid value for `disputed_participant`, must not be `None`")  # noqa: E501

        self._disputed_participant = disputed_participant

    @property
    def creation_time(self) -> datetime:
        """Gets the creation_time of this ExtendedDispute.

        Data-hora da criação da disputa  # noqa: E501

        :return: The creation_time of this ExtendedDispute.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time: datetime):
        """Sets the creation_time of this ExtendedDispute.

        Data-hora da criação da disputa  # noqa: E501

        :param creation_time: The creation_time of this ExtendedDispute.
        :type creation_time: datetime
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def last_modified(self) -> datetime:
        """Gets the last_modified of this ExtendedDispute.

        Data-hora da última atualização de status  # noqa: E501

        :return: The last_modified of this ExtendedDispute.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified: datetime):
        """Sets the last_modified of this ExtendedDispute.

        Data-hora da última atualização de status  # noqa: E501

        :param last_modified: The last_modified of this ExtendedDispute.
        :type last_modified: datetime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def resolution(self) -> ExtendedDisputeResolution:
        """Gets the resolution of this ExtendedDispute.


        :return: The resolution of this ExtendedDispute.
        :rtype: ExtendedDisputeResolution
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: ExtendedDisputeResolution):
        """Sets the resolution of this ExtendedDispute.


        :param resolution: The resolution of this ExtendedDispute.
        :type resolution: ExtendedDisputeResolution
        """

        self._resolution = resolution
