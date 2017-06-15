Feature: Unread Variable
    Code analysis beyond compilation

Scenario: Code with unread variable 
    Given <filename>.c has unread variable
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição de valor à variável mas nunca utilizado"

Scenario: Code without unread variable
    Given <filename>.c doesn't have unread variable
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
