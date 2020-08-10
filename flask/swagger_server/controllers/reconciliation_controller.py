import connexion
import six

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
from swagger_server import util


def create_cid_set_file(body=None):  # noqa: E501
    """Criar Arquivo de CIDs

    Cria um arquivo contendo todos os CIDs de um determinado tipo de chave do participante. O formato do arquivo é um CID por linha (&#x27;\\n&#x27; como EOL), sem ordem definida.  Geração do arquivo é feita assincronamente. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateCidSetFileResponse
    """
    if connexion.request.is_json:
        body = CreateCidSetFileRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_sync_verification(body=None):  # noqa: E501
    """Verificar Sincronismo

    Cria uma verificação de sincronismo para um partipante e tipo de chave. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateSyncVerificationResponse
    """
    if connexion.request.is_json:
        body = CreateSyncVerificationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_cid_set_file(id, pi_requesting_participant):  # noqa: E501
    """Consultar Arquivo de CIDs

    Obtém detalhes do arquivo de CIDs requisitado # noqa: E501

    :param id: 
    :type id: int
    :param pi_requesting_participant: Identificador SPB do participante (direto ou indireto) que faz a requisição.
    :type pi_requesting_participant: str

    :rtype: GetCidSetFileResponse
    """
    return 'do some magic!'


def get_entry_by_cid(cid):  # noqa: E501
    """Consultar Vínculo por CID

    Obtém detalhes de um vínculo ativo identificado pelo CID # noqa: E501

    :param cid: 
    :type cid: dict | bytes

    :rtype: GetEntryByCidResponse
    """
    if connexion.request.is_json:
        cid = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def list_cid_set_events(participant, key_type, start_time=None, end_time=None, limit=None):  # noqa: E501
    """Listar Eventos de CIDs

    Lista os eventos de CIDs para um tipo de chave do participante, ordenados de forma crescente por &#x60;Timestamp&#x60;.  A tabela abaixo resume os eventos de CIDs gerados como conseqüência de cada operação.  |  Operação                                            |  Eventos de CID             | |------------------------------------------------------|-----------------------------| |  [Criar Vínculo](#operation/createEntry)             | adiciona                    | |  [Remover Vínculo](#operation/deleteEntry)           | remove                      | |  [Atualizar Vínculo](#operation/updateEntry)         | remove e adiciona           | |  [Confirmar Reivindicação](#operation/confirmClaim)  | remove (PSP doador)         | |  [Concluir Reivindicação](#operation/completeClaim)  | adiciona (PSP reivindicador)| # noqa: E501

    :param participant: ISPB do partipante direto ou indireto interessado
    :type participant: str
    :param key_type: Tipo de chave
    :type key_type: dict | bytes
    :param start_time: Filtra eventos com data-hora maior ou igual a &#x60;StartTime&#x60;
    :type start_time: str
    :param end_time: Filtra eventos com data-hora menor ou igual a &#x60;EndTime&#x60;
    :type end_time: str
    :param limit: Número limite de eventos a retornar
    :type limit: int

    :rtype: ListCidSetEventsResponse
    """
    if connexion.request.is_json:
        key_type = .from_dict(connexion.request.get_json())  # noqa: E501
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return 'do some magic!'
