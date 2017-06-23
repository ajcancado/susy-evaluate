Feature: Memleak On Realloc
    Code analysis beyond compilation

Scenario: Code with memleak on realloc 
    Given <filename>.c has memleak on realloc
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória no processo de realocação"

Scenario: Code without memleak on realloc
    Given <filename>.c doesn't have memleak on realloc
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Vazamento de memória no processo de realocação"