Feature: Memory leak
    Code analysis beyond compilation

Scenario: Code with memory leak 
    Given <filename>.c has memory leak
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória"

Scenario: Code without memory leak
    Given <filename>.c doesn't have memory leak
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Vazamento de memória"