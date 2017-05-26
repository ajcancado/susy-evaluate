Feature: Uninitialized variables
    Code analysis beyond compilation

Scenario: Code with uninitialized variables
    Given the code has uninitialized variables
    When it is submitted to the app
    Then I should receive the following message “[<filename>.c:<linha>]: (error) Variável não inicializada"

Scenario: Code without uninitialized variables
    Given the code doesn't have uninitialized variables
    When it is submitted to the app
    Then I shouldn't receive any messages
