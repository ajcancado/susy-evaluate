Feature: Out Of Bounds
    Code analysis beyond compilation

Scenario: Code with out of bounds 
    Given <filename>.c has out of bounds
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso inválido"

Scenario: Code without out of bounds
    Given <filename>.c doesn't have out of bounds
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Acesso inválido"