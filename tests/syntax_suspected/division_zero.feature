Feature: Division by zero
    Code analysis beyond compilation

Scenario: Code with division by zero
    Given <filename>.c has a division by zero
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Divisão por zero"

Scenario: Code without division by zero
    Given <filename>.c doesn't have a division by zero
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Divisão por zero"