Feature: Compare Bool Expression with Integer
    Code analysis beyond compilation

Scenario: Code with compare boolen expression with integer 
    Given <filename>.c has compare boolen expression with integer
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Comparação de tipo booleano com tipo inteiro"

Scenario: Code without compare boolen expression with integer
    Given <filename>.c doesn't have compare boolen expression with integer
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Comparação de tipo booleano com tipo inteiro"