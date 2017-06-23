Feature: Invalid Print Argument Type Pointer
    Code analysis beyond compilation

Scenario: Code with invalid print argument type pointer 
    Given <filename>.c has invalid print argument type pointer
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento do tipo ponteiro no formato apresentado é inválido"

Scenario: Code without invalid print argument type pointer
    Given <filename>.c doesn't have invalid print argument type pointer
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Argumento do tipo ponteiro no formato apresentado é inválido"