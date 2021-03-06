# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.statistics_counters import StatisticsCounters  # noqa: F401,E501
from swagger_server import util


class GetEntryResponseStatistics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, last_updated: datetime=None, counters: List[StatisticsCounters]=None):  # noqa: E501
        """GetEntryResponseStatistics - a model defined in Swagger

        :param last_updated: The last_updated of this GetEntryResponseStatistics.  # noqa: E501
        :type last_updated: datetime
        :param counters: The counters of this GetEntryResponseStatistics.  # noqa: E501
        :type counters: List[StatisticsCounters]
        """
        self.swagger_types = {
            'last_updated': datetime,
            'counters': List[StatisticsCounters]
        }

        self.attribute_map = {
            'last_updated': 'LastUpdated',
            'counters': 'Counters'
        }
        self._last_updated = last_updated
        self._counters = counters

    @classmethod
    def from_dict(cls, dikt) -> 'GetEntryResponseStatistics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetEntryResponse_Statistics of this GetEntryResponseStatistics.  # noqa: E501
        :rtype: GetEntryResponseStatistics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def last_updated(self) -> datetime:
        """Gets the last_updated of this GetEntryResponseStatistics.

        data-hora da última atualização dos dados antifraude  # noqa: E501

        :return: The last_updated of this GetEntryResponseStatistics.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: datetime):
        """Sets the last_updated of this GetEntryResponseStatistics.

        data-hora da última atualização dos dados antifraude  # noqa: E501

        :param last_updated: The last_updated of this GetEntryResponseStatistics.
        :type last_updated: datetime
        """

        self._last_updated = last_updated

    @property
    def counters(self) -> List[StatisticsCounters]:
        """Gets the counters of this GetEntryResponseStatistics.

        Contadores de eventos de algum tipo  # noqa: E501

        :return: The counters of this GetEntryResponseStatistics.
        :rtype: List[StatisticsCounters]
        """
        return self._counters

    @counters.setter
    def counters(self, counters: List[StatisticsCounters]):
        """Sets the counters of this GetEntryResponseStatistics.

        Contadores de eventos de algum tipo  # noqa: E501

        :param counters: The counters of this GetEntryResponseStatistics.
        :type counters: List[StatisticsCounters]
        """

        self._counters = counters
