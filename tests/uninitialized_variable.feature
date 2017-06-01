Feature: Uninitialized variables
    Code analysis beyond compilation

Scenario: Code with uninitialized variables
    Given a1.c has uninitialized variables
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (error) Variável não inicializada"

Scenario: Code without uninitialized variables
    Given a2.c doesn't have uninitialized variables
    When it is submitted to the app
    Then shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"
