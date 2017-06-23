Feature: Invalid Print Argument Type Float
    Code analysis beyond compilation

Scenario: Code with invalid print argument type float 
    Given <filename>.c has invalid print argument type float
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'float' é inválido neste caso"

Scenario: Code without invalid print argument type float
    Given <filename>.c doesn't have invalid print argument type float
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Argumento de tipo 'float' é inválido neste caso"