Feature: Possible Buffer Access Out Bounds
    Code analysis beyond compilation

Scenario: Code with possible buffer access out bounds 
    Given <filename>.c has possible buffer access out bounds
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso inválido"

Scenario: Code without possible buffer access out bounds
    Given <filename>.c doesn't have possible buffer access out bounds
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
