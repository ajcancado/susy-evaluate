Feature: Memory leak
    Code analysis beyond compilation

Scenario: Code with memory leak 
    Given the code has memory leak
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:2]: (error) vazamento de memória"

Scenario: Code without memory leak
    Given the code doesn't have memory leak
    When it is submitted to the app
    Then I shouldn't receive any messages 