Feature: Unprecise Math Call
    Code analysis beyond compilation

Scenario: Code with unprecise math call 
    Given <filename>.c has unprecise math call
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"

Scenario: Code without unprecise math call
    Given <filename>.c doesn't have unprecise math call
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"
