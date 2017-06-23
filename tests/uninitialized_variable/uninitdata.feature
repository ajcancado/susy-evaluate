Feature: uninitialized data
    Code analysis beyond compilation

Scenario: Code with uninitialized data
    Given <filename>.c has uninitialized data
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Memória foi alocada mas não foi inicializada"

Scenario: Code without uninitialized data
    Given <filename>.c doesn't have uninitialized data
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Memória foi alocada mas não foi inicializada"
