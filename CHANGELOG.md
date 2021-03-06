# Changelog

Mudanças relevantes na API do DICT serão documentadas aqui.

## [1.0.0-RC5] - 2020-07-22
### Adicionado
- Contadores para avaliação de risco de fraude em GetEntryResponse
- Campo obrigatório OpeningDate em BrazilianAccount
- Campo HasMoreElements em ListClaimsResponse, ListCidSetEventsResponse
- Header obrigatório PI-RequestingParticipant para operações getEntry, getClaim e getCidSetFile
- Possibilidade de remover vínculo com razão FRAUD (correção da spec)
- _Endpoints_ de disputas

### Alterado
- Campos CreationDate e KeyOwnershipDate de ExtendedEntry passaram do formato date para date-time
- Colocada restrição de caracteres para nomes de NaturalPerson e LegalPerson

### Removido
- Header PI-PayerAccountServicer para operação getEntry

## [1.0.0-RC4] - 2020-06-24
### Adicionado
- Campo Reason em ConfirmClaimRequest (correção da spec)
- Campo Participant em AcknowledgeClaimRequest, CancelClaimRequest, ConfirmClaimRequest, CompleteClaimRequest e DeleteEntryRequest
- Erro InternalServerError (spec omitia)
- Definições de idempotência para operações de acknowledgeClaim, confirmClaim e cancelClaim

### Alterado
- Campo SyncVerifier tornou-se ParticipantSyncVerifier em SyncVerification

### Removido
- Campo Reason de CompleteClaimRequest (correção da spec)
- Campo SyncVerifierLastModified de ExtendedSyncVerification

## [1.0.0-RC3] - 2020-05-29
### Adicionado
- Campo opcional correlationId a Problem
- Erro InvalidReason
- Possibilidade de confirmar reivindicação com razão USER_REQUESTED
- Parâmetro Id na operação getCidSetFile (correção da spec)

### Alterado
- Campo CompletionPeriodEnd deixou de ser preenchido para portabilidade

### Removido
- Campo SyncVerifierLastModified de CreateSyncVerificationRequest

## [1.0.0-RC2] - 2020-05-08
### Adicionado
- _Endpoints_ para reconciliação
- Campo obrigatório _RequestId_ em CreateEntryRequest e CompleteClaimResponse
- Erro RequestIdAlreadyUsed

### Alterado
- Tamanho válido do campo _AccountNumber_, de 4 a 10 para 1 a 20
- Tamanho válido do campo _Branch_, de 4 para 1 a 4
- Campo _Branch_ tornou-se opcional
- Erro EntryLimitExceededForOwner substituído por EntryLimitExceeded

### Removido
- Campos _CreatedEntryCid_ e _DeleteEntryCid_
  - Dos componentes CreateEntryResponse, DeleteEntryResponse, UpdateEntryResponse, ConfirmClaimResponse e CompleteClaimResponse

## [1.RC1] - 2020-04-01
### Adicionado
- _Endpoints_ para reivindicação de posse e portabilidade
- Novo tipo de chave EVP - Endereço Virtual de Pagamento
- Campo obrigatório _Reason_ em CreateEntryRequest e DeleteEntryRequest
- Campo _CreatedEntryCid_ em CreateEntryResponse
- _Endpoint_ updateEntry

### Alterado
- Tamanho máximo de chave alterado de 72 para 77 caracteres
- Código de sucesso da remoção de vínculo mudou para 200, inclui agora DeleteEntryResponse no corpo
- Atualizada referência para versão 2.0 do Manual de Segurança PIX

## [1.RC0] - 2020-02-18

Primeiro _release candidate_ da versão 1 da API.

