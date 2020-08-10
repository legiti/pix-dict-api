import connexion
import six

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
from swagger_server import util


def acknowledge_dispute(dispute_id, body=None):  # noqa: E501
    """Receber Disputa

    Notifica recebimento pelo participante demandado de uma disputa com status &#x60;OPEN&#x60;.    ### Idempotência   A operação é idempotente. Caso disputa já tenha sido recebida e ela esteja ainda com    status &#x60;ACKNOWLEDGED&#x60;, será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param dispute_id: 
    :type dispute_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: AcknowledgeDisputeResponse
    """
    if connexion.request.is_json:
        body = AcknowledgeDisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cancel_dispute(dispute_id, body=None):  # noqa: E501
    """Cancelar Disputa

    Cancela a disputa. Só pode ser realizada pelo participante pagador.    ### Idempotência   A operação é idempotente. Caso disputa já tenha sido cancelada com os mesmos parâmetros,    será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param dispute_id: 
    :type dispute_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: CancelDisputeResponse
    """
    if connexion.request.is_json:
        body = CancelDisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def close_dispute(dispute_id, body=None):  # noqa: E501
    """Fechar Disputa

    Fecha a disputa. Só pode ser realizada pelo participante demandado.    ### Idempotência   A operação é idempotente. Caso disputa já tenha sido fechada com os mesmos parâmetros,    será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param dispute_id: 
    :type dispute_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: CloseDisputeResponse
    """
    if connexion.request.is_json:
        body = CloseDisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_dispute(body=None):  # noqa: E501
    """Criar Disputa

    Cria uma disputa. Utilizado pelo participante do usuário pagador para criar uma disputa sobre uma transação realizada. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateDisputeResponse
    """
    if connexion.request.is_json:
        body = CreateDisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_dispute(dispute_id, pi_requesting_participant):  # noqa: E501
    """Consultar Disputa

    Obtém detalhes de uma disputa. # noqa: E501

    :param dispute_id: 
    :type dispute_id: 
    :param pi_requesting_participant: Identificador SPB do participante (direto ou indireto) que faz a requisição.
    :type pi_requesting_participant: str

    :rtype: GetDisputeResponse
    """
    return 'do some magic!'


def list_disputes(participant, is_payer=None, is_disputed=None, status=None, include_details=None, modified_after=None, modified_before=None, limit=None):  # noqa: E501
    """Listar Disputas

    Obtém lista de disputas em que o participante é parte.  Lista de disputas é ordenada de forma crescente pelo campo &#x60;LastModified&#x60; . # noqa: E501

    :param participant: ISPB do partipante direto ou indireto interessado
    :type participant: str
    :param is_payer: Restringe a disputas em que o participante é o pagador
    :type is_payer: bool
    :param is_disputed: Restringe a disputas em que o participante é o recebedor
    :type is_disputed: bool
    :param status: Status da disputa
    :type status: dict | bytes
    :param include_details: Inclui os detalhes da disputa
    :type include_details: bool
    :param modified_after: Filtra disputas com data-hora de modificação maior ou igual a &#x60;modifiedAfter&#x60;
    :type modified_after: str
    :param modified_before: Filtra disputas com data-hora de modificação menor ou igual a &#x60;modifiedBefore&#x60;
    :type modified_before: str
    :param limit: Número limite de disputas a retornar
    :type limit: int

    :rtype: ListDisputesResponse
    """
    if connexion.request.is_json:
        status = .from_dict(connexion.request.get_json())  # noqa: E501
    modified_after = util.deserialize_datetime(modified_after)
    modified_before = util.deserialize_datetime(modified_before)
    return 'do some magic!'
