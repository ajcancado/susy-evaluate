Feature: Unused Label Switch
    Code analysis beyond compilation

Scenario: Code with unused label switch 
    Given <filename>.c has unused label switch
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Label não utilizado"

Scenario: Code without unused label switch
    Given <filename>.c doesn't have unused label switch
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
