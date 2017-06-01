Feature: Redundant Assignment
    Code analysis beyond compilation

Scenario: Code with redundant assignment
    Given the code has redundant assignment
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição redundante"

Scenario: Code without redundant assignment
    Given the code doesn't have redundant assignment
    When it is submitted to the app
    Then I shouldn't receive any messages 