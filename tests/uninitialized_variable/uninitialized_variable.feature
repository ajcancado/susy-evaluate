Feature: Uninitialized variables
    Code analysis beyond compilation

Scenario: Code with uninitialized variables
    Given <filename>.c has uninitialized variables
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (error) Variável não inicializada"

Scenario: Code without uninitialized variables
    Given <filename>.c doesn't have uninitialized variables
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"
