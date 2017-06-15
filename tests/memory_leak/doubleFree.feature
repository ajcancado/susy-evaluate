Feature: Double Free
    Code analysis beyond compilation

Scenario: Code with double free 
    Given <filename>.c has double free
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"

Scenario: Code without double free
    Given <filename>.c doesn't have double free
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
