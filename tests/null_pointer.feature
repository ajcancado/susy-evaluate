Feature: Null pointer dereference
    Code analysis beyond compilation

Scenario: Code with null pointer dereference
    Given the code has null pointer dereference
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (error) Desreferenciamento de ponteiro nulo"

Scenario: Code without null pointer dereference
    Given the code doesn't have null pointer dereference
    When it is submitted to the app
    Then I shouldn't receive any messages
