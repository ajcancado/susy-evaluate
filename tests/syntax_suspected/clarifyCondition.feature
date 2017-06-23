Feature: Clarify Condition
    Code analysis beyond compilation

Scenario: Code with clarify condition 
    Given <filename>.c has clarify condition
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Condição não esta claramente definida"

Scenario: Code without clarify condition
    Given <filename>.c doesn't have clarify condition
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Condição não esta claramente definida"