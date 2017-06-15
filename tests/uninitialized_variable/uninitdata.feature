Feature: Uninitiazed date
    Code analysis beyond compilation

Scenario: Code with uninitiazed date 
    Given <filename>.c has uninitiazed date
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Mémoria foi alocada mas não foi inicializada"

Scenario: Code without uninitiazed date
    Given <filename>.c doesn't have uninitiazed date
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
