Feature: Unassigned Variable
    Code analysis beyond compilation

Scenario: Code with unassigned variable 
    Given <filename>.c has unassigned variable
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Variável não foi atribuída"

Scenario: Code without unassigned variable
    Given <filename>.c doesn't have unassigned variable
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
