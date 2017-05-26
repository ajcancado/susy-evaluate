Feature: Memory leak
    Code analysis beyond compilation

Scenario: Uninitialized variable analysis
    Given the code has uninitialized variables
    When it is submitted to SuSy
    Then I should receive the following message “[<filename>.c:2]: (error) vazamento de memória"

Scenario: Uninitialized variable analysis
    Given the code doesn't have uninitialized variables
    When it is submitted to SuSy
    Then I shouldn't receive any messages 