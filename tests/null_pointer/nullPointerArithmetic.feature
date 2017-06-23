Feature: Null Pointer Arithmetic
    Code analysis beyond compilation

Scenario: Code with null pointer arithmetic 
    Given <filename>.c has null pointer arithmetic
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído"

Scenario: Code without null pointer arithmetic
    Given <filename>.c doesn't have null pointer arithmetic
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído"