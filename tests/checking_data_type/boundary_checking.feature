Feature: Boundary checking
    Code analysis beyond compilation

Scenario: Code with array accessed out of bounds
    Given a1.c has an array accessed out of bounds
    When it is submitted to the app
    Then it should receive the following message "[<filename>.c:<linha>]: (error) Acesso à posição inválida de vetor"

Scenario: Code without array accessed out of bounds
    Given a2.c doesn't have an array accessed out of bounds
    When it is submitted to the app
    Then  shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"
