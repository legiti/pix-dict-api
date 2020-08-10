import connexion
import six

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
from swagger_server import util


def acknowledge_claim(claim_id, body=None):  # noqa: E501
    """Receber Reivindicação

    Notifica recebimento pelo participante doador de reivindicação com status &#x60;OPEN&#x60;.    ### Idempotência   A operação é idempotente. Caso reivindicação já tenha sido recebida e ela esteja ainda com    status &#x60;WAITING_RESOLUTION&#x60;, será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param claim_id: 
    :type claim_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: AcknowledgeClaimResponse
    """
    if connexion.request.is_json:
        body = AcknowledgeClaimRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def cancel_claim(claim_id, body=None):  # noqa: E501
    """Cancelar Reivindicação

    Cancela reivindicação.           Para reivindicação de posse, status deve ser &#x60;WAITING_RESOLUTION&#x60; ou &#x60;CONFIRMED&#x60;.  Para portabilidade, status deve ser &#x60;WAITING_RESOLUTION&#x60;. Se razão de cancelamento for  &#x60;DEFAULT_OPERATION&#x60;, prazo definido pelo campo &#x60;ResolutionPeriodEnd&#x60; deve ter passado.  A tabela abaixo define, a depender da razão e do tipo, quem pode cancelar.  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;&lt;/th&gt;       &lt;th colspan&#x3D;\&quot;2\&quot;&gt;OWNERSHIP&lt;/th&gt;       &lt;th colspan&#x3D;\&quot;2\&quot;&gt;PORTABILITY&lt;/th&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;th&gt;Razão&lt;/th&gt;       &lt;th&gt;Doador&lt;/th&gt;       &lt;th&gt;Reivindicador&lt;/th&gt;       &lt;th&gt;Doador&lt;/th&gt;       &lt;th&gt;Reivindicador&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;USER_REQUESTED&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;ACCOUNT_CLOSURE&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;FRAUD&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;DEFAULT_OPERATION&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;    ### Idempotência   A operação é idempotente. Caso reivindicação já tenha sido cancelada com os mesmos parâmetros,    será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param claim_id: 
    :type claim_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: CancelClaimResponse
    """
    if connexion.request.is_json:
        body = CancelClaimRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def complete_claim(claim_id, body=None):  # noqa: E501
    """Concluir Reivindicação

    Conclui reivindicação pelo reivindicador. Como consequência, vínculo da chave com participante reivindicador é criado.  Para reivindicação de posse, status deve ser &#x60;CONFIRMED&#x60; e prazo definido pelo campo &#x60;CompletionPeriodEnd&#x60; deve ter passado.  Para portabilidade, status deve ser &#x60;CONFIRMED&#x60;.  ### Idempotência A operação de conclusão de reivindicação é idempotente. Valem aqui as mesmas considerações feitas sobre esse tema na operação de [Criar Vínculo](#operation/createEntry). # noqa: E501

    :param claim_id: 
    :type claim_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: CompleteClaimResponse
    """
    if connexion.request.is_json:
        body = CompleteClaimRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def confirm_claim(claim_id, body=None):  # noqa: E501
    """Confirmar Reivindicação

    Confirma a operação de reivindicação. Como consequência, vínculo da chave com participante doador é removido.  Status deve estar em &#x60;WAITING_RESOLUTION&#x60;.  Para reivindicação de posse, caso razão seja &#x60;DEFAULT_OPERATION&#x60;, o prazo de resolução (&#x60;ResolutionPeriodEnd&#x60;)   deve ter passado. Se a razão informada for &#x60;USER_REQUESTED&#x60;, o prazo de encerramento (&#x60;CompletionPeriodEnd&#x60;)   será adiantado para permitir o encerramento imediato pelo reivindicador.  A tabela abaixo define, a depender da razão e do tipo, quem pode confirmar.  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th&gt;&lt;/th&gt;       &lt;th colspan&#x3D;\&quot;2\&quot;&gt;OWNERSHIP&lt;/th&gt;       &lt;th colspan&#x3D;\&quot;2\&quot;&gt;PORTABILITY&lt;/th&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;th&gt;Razão&lt;/th&gt;       &lt;th&gt;Doador&lt;/th&gt;       &lt;th&gt;Reivindicador&lt;/th&gt;       &lt;th&gt;Doador&lt;/th&gt;       &lt;th&gt;Reivindicador&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td&gt;USER_REQUESTED&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;ACCOUNT_CLOSURE&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td&gt;DEFAULT_OPERATION&lt;/td&gt;       &lt;td&gt;✓&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;       &lt;td&gt;&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;    ### Idempotência   A operação é idempotente. Caso reivindicação já tenha sido confirmada com os mesmos parâmetros   e esteja ainda com status &#x60;CONFIRMED&#x60;, será retornada resposta equivalente à primeira requisição. # noqa: E501

    :param claim_id: 
    :type claim_id: 
    :param body: 
    :type body: dict | bytes

    :rtype: ConfirmClaimResponse
    """
    if connexion.request.is_json:
        body = ConfirmClaimRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_claim(body=None):  # noqa: E501
    """Criar Reivindicação

    Cria uma nova reivindicação.   Essa operação é feita pelo participante reivindicador a pedido do usuário final. O vínculo atual permanece inalterado, até que haja a confirmação pelo PSP doador.  Nem todo tipo de chave pode ser reivindicado ou portado. A tabela abaixo define as possibilidades:    |  compatível?  | OWNERSHIP  | PORTABILITY  |   |---------------|:----------:|:------------:|   | CPF           |            |      ✓       |   | CNPJ          |            |      ✓       |   | PHONE         |    ✓      |      ✓       |   | EMAIL         |    ✓      |      ✓       |   | EVP           |            |              | # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateClaimResponse
    """
    if connexion.request.is_json:
        body = CreateClaimRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_claim(claim_id, pi_requesting_participant):  # noqa: E501
    """Consultar Reivindicação

    Obtém detalhes de uma reivindicação. # noqa: E501

    :param claim_id: 
    :type claim_id: 
    :param pi_requesting_participant: Identificador SPB do participante (direto ou indireto) que faz a requisição.
    :type pi_requesting_participant: str

    :rtype: GetClaimResponse
    """
    return 'do some magic!'


def list_claims(participant, is_donor=None, is_claimer=None, status=None, type=None, modified_after=None, modified_before=None, limit=None):  # noqa: E501
    """Listar Reivindicações

    Obtém lista de reivindicações em que o participante é doador ou reivindicador.  Lista de reivindicações é ordenada de forma crescente pelo campo &#x60;LastModified&#x60; .  _Atenção_: Ao percorrer a lista em intervalos de tempo fechados, recomendável para que  não se pule nenhum elemento, alguns elementos retornados poderão se repetir. # noqa: E501

    :param participant: ISPB do partipante direto ou indireto interessado
    :type participant: str
    :param is_donor: Restringe a reivindicações em que o participante é doador
    :type is_donor: bool
    :param is_claimer: Restringe a reivindicações em que o participante é reivindicador
    :type is_claimer: bool
    :param status: Status da reivindicação
    :type status: dict | bytes
    :param type: Tipo de reivindicação
    :type type: dict | bytes
    :param modified_after: Filtra reivindicações com data-hora de modificação maior ou igual a &#x60;modifiedAfter&#x60;
    :type modified_after: str
    :param modified_before: Filtra reivindicações com data-hora de modificação menor ou igual a &#x60;modifiedBefore&#x60;
    :type modified_before: str
    :param limit: Número limite de reivindicações a retornar
    :type limit: int

    :rtype: ListClaimsResponse
    """
    if connexion.request.is_json:
        status = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        type = .from_dict(connexion.request.get_json())  # noqa: E501
    modified_after = util.deserialize_datetime(modified_after)
    modified_before = util.deserialize_datetime(modified_before)
    return 'do some magic!'
