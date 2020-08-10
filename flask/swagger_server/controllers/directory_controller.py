import connexion
import six

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
from swagger_server import util


def create_entry(body=None):  # noqa: E501
    """Criar Vínculo

    Cria um novo vínculo de chave com conta transacional.  ### Idempotência A operação de criação de vínculo é idempotente. Isso significa que é seguro realizar uma nova tentativa em caso de falhas  temporárias, como erros de conexão ou término abrupto de processos. A resposta retornada para uma requisição repetida é  equivalente à resposta dada à primeira requisição processada.  Para garantir a idempotência da operação, a requisição tem um campo &#x60;RequestId&#x60;. Esse campo é um  [UUID versão 4](https://tools.ietf.org/html/rfc4122#section-4.4) e deve ser único no contexto de um mesmo participante.  O &#x60;RequestId&#x60; fica associado ao vínculo criado e é usado no cálculo do seu CID (ver seção de reconciliação).  Uma requisição de criação é considerada repetida quando o CID do vínculo contido na requisição já existe no DICT. Caso seja feita uma requisição com um &#x60;RequestId&#x60; previamente usado, mas com parâmetros diferentes para o vínculo, será retornado o erro &#x60;RequestIdAlreadyUsed&#x60;. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CreateEntryResponse
    """
    if connexion.request.is_json:
        body = CreateEntryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_entry(key, body=None):  # noqa: E501
    """Remover Vínculo

    Remove um vínculo de chave com conta. # noqa: E501

    :param key: 
    :type key: dict | bytes
    :param body: 
    :type body: dict | bytes

    :rtype: DeleteEntryResponse
    """
    if connexion.request.is_json:
        key = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = DeleteEntryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_entry(key, pi_requesting_participant, pi_payer_id, pi_end_to_end_id):  # noqa: E501
    """Consultar Vínculo

    Obtém um vínculo contendo os detalhes de conta transacional associados a uma chave de endereçamento.  ### Dados anti-fraude A fim de permitir avaliação de risco de fraude, na consulta de vínculos são fornecidos contadores dos seguintes eventos:  1. transações realizadas 2. disputas de fraude e pld/ft abertas 3. disputas de fraude e pld/ft procedentes  Os eventos são agregados por chave, titular (cpf ou cnpj) e conta transacional em 3 janelas temporais:  - últimos 3 dias (d3) - últimos 30 dias (d30)  - últimos 6 meses, sem contar o mês corrente (m6)  Esses contadores tem ciclo de vida independente do vínculo. Eles não são zerados, mesmo que haja  desativação da chave ou da conta. Se houver troca de titularidade, ou portabilidade, os dados  são herdados pelo novo registro no que couber (titular, chave, ou conta).  Os contadores de transações realizadas são quantizados. A escala usada é 0, 1, 5, 10, 50, 100, 500, 1000, 5000 ... Arrendonda-se o número para cima, por exemplo: 3 → 5, 190 → 500 .  ### Limitação de requisições A política de limitação (_rate-limiting_) funciona com base em cabeçalhos enviados na requisição.  O parâmetro &#x60;PI-PayerId&#x60; é o identificador pseudonimizado do usuário final, vinculado a um participante.  Requisições vindas de um mesmo usuário, para um mesmo participante, devem usar o mesmo identificador.  Como sugestão de implementação, pode ser utilizado o valor hexadecimal da aplicação de  [HMAC-SHA-256](https://tools.ietf.org/html/rfc4634#section-7) a um identificador do usuário,  com chave de conhecimento restrito ao participante.  ### Cache Consultas a vínculos podem ter suas respostas _cacheadas_ no PSP, devendo seguir as  diretivas contidas no header [&#x60;Cache-Control&#x60;](https://tools.ietf.org/html/rfc7234#section-5.2).  _Importante_: Para fazer uso de cache, clientes HTTP geralmente precisam ser configurados. Não é comum que tenham essa funcionalidade habilitada por padrão. # noqa: E501

    :param key: 
    :type key: dict | bytes
    :param pi_requesting_participant: Identificador SPB do participante (direto ou indireto) que faz a requisição.
    :type pi_requesting_participant: str
    :param pi_payer_id: Identificador pseudonimizado do pagador que originou a requisição. Usado para _rate-limiting_.
    :type pi_payer_id: str
    :param pi_end_to_end_id: Identificador fim-a-fim do pagamento associado a essa requisição. Corresponde ao campo &#x60;EndToEndId&#x60; na mensagem pacs.008. Usado para _rate-limiting_.
    :type pi_end_to_end_id: str

    :rtype: GetEntryResponse
    """
    if connexion.request.is_json:
        key = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_entry(key, body=None):  # noqa: E501
    """Atualizar Vínculo

    Atualiza um vínculo.   A ser utilizado no cenário de atualização da informação da conta de um cliente, permanecendo este no mesmo PSP. Somente pode ser atualizada a informação de conta do vínculo. Outras atualizações do vínculo devem ser feitas por exclusão/inclusão do vínculo, portabilidade ou reivindicação de posse, a depender da situação. # noqa: E501

    :param key: 
    :type key: dict | bytes
    :param body: 
    :type body: dict | bytes

    :rtype: UpdateEntryResponse
    """
    if connexion.request.is_json:
        key = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        body = UpdateEntryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
