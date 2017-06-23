Feature: Invalid Print Argument Type Number
    Code analysis beyond compilation

Scenario: Code with invalid print argument type number 
    Given <filename>.c has invalid print argument type number
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento do tipo 'number' no formato apresentado é inválido"

Scenario: Code without invalid print argument type number
    Given <filename>.c doesn't have invalid print argument type number
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Argumento do tipo 'number' no formato apresentado é inválido"