# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cid import Cid  # noqa: E501
from swagger_server.models.componentsresponses_not_foundcontentapplication1problem2_bxmlschema import ComponentsresponsesNotFoundcontentapplication1problem2Bxmlschema  # noqa: E501
from swagger_server.models.create_cid_set_file_request import CreateCidSetFileRequest  # noqa: E501
from swagger_server.models.create_cid_set_file_response import CreateCidSetFileResponse  # noqa: E501
from swagger_server.models.create_sync_verification_request import CreateSyncVerificationRequest  # noqa: E501
from swagger_server.models.create_sync_verification_response import CreateSyncVerificationResponse  # noqa: E501
from swagger_server.models.get_cid_set_file_response import GetCidSetFileResponse  # noqa: E501
from swagger_server.models.get_entry_by_cid_response import GetEntryByCidResponse  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.key_type import KeyType  # noqa: E501
from swagger_server.models.list_cid_set_events_response import ListCidSetEventsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReconciliationController(BaseTestCase):
    """ReconciliationController integration test stubs"""

    def test_create_cid_set_file(self):
        """Test case for create_cid_set_file

        Criar Arquivo de CIDs
        """
        body = CreateCidSetFileRequest()
        response = self.client.open(
            '/api/v1-rc5//cids/files/',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_sync_verification(self):
        """Test case for create_sync_verification

        Verificar Sincronismo
        """
        body = CreateSyncVerificationRequest()
        response = self.client.open(
            '/api/v1-rc5//sync-verifications/',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cid_set_file(self):
        """Test case for get_cid_set_file

        Consultar Arquivo de CIDs
        """
        headers = [('pi_requesting_participant', 'pi_requesting_participant_example')]
        response = self.client.open(
            '/api/v1-rc5//cids/files/{Id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_entry_by_cid(self):
        """Test case for get_entry_by_cid

        Consultar Vínculo por CID
        """
        response = self.client.open(
            '/api/v1-rc5//cids/entries/{Cid}'.format(cid=Cid()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_cid_set_events(self):
        """Test case for list_cid_set_events

        Listar Eventos de CIDs
        """
        query_string = [('participant', 'participant_example'),
                        ('key_type', KeyType()),
                        ('start_time', '2013-10-20T19:20:30+01:00'),
                        ('end_time', '2013-10-20T19:20:30+01:00'),
                        ('limit', 56)]
        response = self.client.open(
            '/api/v1-rc5//cids/events',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
