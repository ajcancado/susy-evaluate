Feature: Null Pointer Redundant Check
    Code analysis beyond compilation

Scenario: Code with null pointer redundant check 
    Given <filename>.c has null pointer redundant check
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Existe uma possibilidade do valor acessado do ponteiro ser nulo"

Scenario: Code without null pointer redundant check
    Given <filename>.c doesn't have null pointer redundant check
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Existe uma possibilidade do valor acessado do ponteiro ser nulo"