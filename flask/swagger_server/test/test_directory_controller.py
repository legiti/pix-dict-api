# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.componentsresponses_not_foundcontentapplication1problem2_bxmlschema import ComponentsresponsesNotFoundcontentapplication1problem2Bxmlschema  # noqa: E501
from swagger_server.models.create_entry_request import CreateEntryRequest  # noqa: E501
from swagger_server.models.create_entry_response import CreateEntryResponse  # noqa: E501
from swagger_server.models.delete_entry_request import DeleteEntryRequest  # noqa: E501
from swagger_server.models.delete_entry_response import DeleteEntryResponse  # noqa: E501
from swagger_server.models.get_entry_response import GetEntryResponse  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.key import Key  # noqa: E501
from swagger_server.models.update_entry_request import UpdateEntryRequest  # noqa: E501
from swagger_server.models.update_entry_response import UpdateEntryResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDirectoryController(BaseTestCase):
    """DirectoryController integration test stubs"""

    def test_create_entry(self):
        """Test case for create_entry

        Criar Vínculo
        """
        body = CreateEntryRequest()
        response = self.client.open(
            '/api/v1-rc5//entries/',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_entry(self):
        """Test case for delete_entry

        Remover Vínculo
        """
        body = DeleteEntryRequest()
        response = self.client.open(
            '/api/v1-rc5//entries/{Key}/delete'.format(key=Key()),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_entry(self):
        """Test case for get_entry

        Consultar Vínculo
        """
        headers = [('pi_requesting_participant', 'pi_requesting_participant_example'),
                   ('pi_payer_id', 'pi_payer_id_example'),
                   ('pi_end_to_end_id', 'pi_end_to_end_id_example')]
        response = self.client.open(
            '/api/v1-rc5//entries/{Key}'.format(key=Key()),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_entry(self):
        """Test case for update_entry

        Atualizar Vínculo
        """
        body = UpdateEntryRequest()
        response = self.client.open(
            '/api/v1-rc5//entries/{Key}'.format(key=Key()),
            method='PUT',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
