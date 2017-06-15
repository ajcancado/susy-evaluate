Feature: Unused Variable
    Code analysis beyond compilation

Scenario: Code with unused Variable 
    Given <filename>.c has unused Variable
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Variável nunca foi utilizada"

Scenario: Code without unused Variable
    Given <filename>.c doesn't have unused Variable
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
