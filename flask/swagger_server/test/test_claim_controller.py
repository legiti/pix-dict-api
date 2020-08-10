# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.acknowledge_claim_request import AcknowledgeClaimRequest  # noqa: E501
from swagger_server.models.acknowledge_claim_response import AcknowledgeClaimResponse  # noqa: E501
from swagger_server.models.cancel_claim_request import CancelClaimRequest  # noqa: E501
from swagger_server.models.cancel_claim_response import CancelClaimResponse  # noqa: E501
from swagger_server.models.claim_status import ClaimStatus  # noqa: E501
from swagger_server.models.claim_type import ClaimType  # noqa: E501
from swagger_server.models.complete_claim_request import CompleteClaimRequest  # noqa: E501
from swagger_server.models.complete_claim_response import CompleteClaimResponse  # noqa: E501
from swagger_server.models.componentsresponses_not_foundcontentapplication1problem2_bxmlschema import ComponentsresponsesNotFoundcontentapplication1problem2Bxmlschema  # noqa: E501
from swagger_server.models.confirm_claim_request import ConfirmClaimRequest  # noqa: E501
from swagger_server.models.confirm_claim_response import ConfirmClaimResponse  # noqa: E501
from swagger_server.models.create_claim_request import CreateClaimRequest  # noqa: E501
from swagger_server.models.create_claim_response import CreateClaimResponse  # noqa: E501
from swagger_server.models.get_claim_response import GetClaimResponse  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server.models.list_claims_response import ListClaimsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClaimController(BaseTestCase):
    """ClaimController integration test stubs"""

    def test_acknowledge_claim(self):
        """Test case for acknowledge_claim

        Receber Reivindicação
        """
        body = AcknowledgeClaimRequest()
        response = self.client.open(
            '/api/v1-rc5//claims/{ClaimId}/acknowledge'.format(claim_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cancel_claim(self):
        """Test case for cancel_claim

        Cancelar Reivindicação
        """
        body = CancelClaimRequest()
        response = self.client.open(
            '/api/v1-rc5//claims/{ClaimId}/cancel'.format(claim_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_complete_claim(self):
        """Test case for complete_claim

        Concluir Reivindicação
        """
        body = CompleteClaimRequest()
        response = self.client.open(
            '/api/v1-rc5//claims/{ClaimId}/complete'.format(claim_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_confirm_claim(self):
        """Test case for confirm_claim

        Confirmar Reivindicação
        """
        body = ConfirmClaimRequest()
        response = self.client.open(
            '/api/v1-rc5//claims/{ClaimId}/confirm'.format(claim_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_claim(self):
        """Test case for create_claim

        Criar Reivindicação
        """
        body = CreateClaimRequest()
        response = self.client.open(
            '/api/v1-rc5//claims/',
            method='POST',
            data=json.dumps(body),
            content_type='application/xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_claim(self):
        """Test case for get_claim

        Consultar Reivindicação
        """
        headers = [('pi_requesting_participant', 'pi_requesting_participant_example')]
        response = self.client.open(
            '/api/v1-rc5//claims/{ClaimId}'.format(claim_id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_claims(self):
        """Test case for list_claims

        Listar Reivindicações
        """
        query_string = [('participant', 'participant_example'),
                        ('is_donor', true),
                        ('is_claimer', true),
                        ('status', ClaimStatus()),
                        ('type', ClaimType()),
                        ('modified_after', '2013-10-20T19:20:30+01:00'),
                        ('modified_before', '2013-10-20T19:20:30+01:00'),
                        ('limit', 200)]
        response = self.client.open(
            '/api/v1-rc5//claims/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
