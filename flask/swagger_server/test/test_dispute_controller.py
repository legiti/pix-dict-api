# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.acknowledge_dispute_request import AcknowledgeDisputeRequest  # noqa: E501
from swagger_server.models.acknowledge_dispute_response import AcknowledgeDisputeResponse  # noqa: E501
from swagger_server.models.cancel_dispute_request import CancelDisputeRequest  # noqa: E501
from swagger_server.models.cancel_dispute_response import CancelDisputeResponse  # noqa: E501
from swagger_server.models.close_dispute_request import CloseDisputeRequest  # noqa: E501
from swagger_server.models.close_dispute_response import CloseDisputeResponse  # noqa: E501
from swagger_server.models.componentsresponses_not_foundcontentapplication1problem2_bxmlschema import ComponentsresponsesNotFoundcontentapplication1problem2Bxmlschema  # noqa: E501
from swagger_server.models.create_dispute_request import CreateDisputeRequest  # noqa: E501
from swagger_server.models.create_dispute_response import CreateDisputeResponse  # noqa: E501
from swagger_server.models.dispute_status import DisputeStatus  # noqa: E501
from swagger_server.models.get_dispute_response import GetDisputeResponse  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.list_disputes_response import ListDisputesResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDisputeController(BaseTestCase):
    """DisputeController integration test stubs"""

    def test_acknowledge_dispute(self):
        """Test case for acknowledge_dispute

        Receber Disputa
        """
        body = AcknowledgeDisputeRequest()
        response = self.client.open(
            '/api/v1-rc5//disputes/{DisputeId}/acknowledge'.format(dispute_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cancel_dispute(self):
        """Test case for cancel_dispute

        Cancelar Disputa
        """
        body = CancelDisputeRequest()
        response = self.client.open(
            '/api/v1-rc5//disputes/{DisputeId}/cancel'.format(dispute_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_close_dispute(self):
        """Test case for close_dispute

        Fechar Disputa
        """
        body = CloseDisputeRequest()
        response = self.client.open(
            '/api/v1-rc5//disputes/{DisputeId}/close'.format(dispute_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_dispute(self):
        """Test case for create_dispute

        Criar Disputa
        """
        body = CreateDisputeRequest()
        response = self.client.open(
            '/api/v1-rc5//disputes/',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dispute(self):
        """Test case for get_dispute

        Consultar Disputa
        """
        headers = [('pi_requesting_participant', 'pi_requesting_participant_example')]
        response = self.client.open(
            '/api/v1-rc5//disputes/{DisputeId}'.format(dispute_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_disputes(self):
        """Test case for list_disputes

        Listar Disputas
        """
        query_string = [('participant', 'participant_example'),
                        ('is_payer', true),
                        ('is_disputed', true),
                        ('status', DisputeStatus()),
                        ('include_details', false),
                        ('modified_after', '2013-10-20T19:20:30+01:00'),
                        ('modified_before', '2013-10-20T19:20:30+01:00'),
                        ('limit', 200)]
        response = self.client.open(
            '/api/v1-rc5//disputes/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
