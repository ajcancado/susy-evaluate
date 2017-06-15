Feature: Resource Leak
    Code analysis beyond compilation

Scenario: Code with resource leak 
    Given <filename>.c has resource leak
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de recursos"

Scenario: Code without resource leak
    Given <filename>.c doesn't have resource leak
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
