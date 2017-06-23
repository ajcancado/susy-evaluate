Feature: Use Closed File
    Code analysis beyond compilation

Scenario: Code with use closed file 
    Given <filename>.c has use closed file
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"

Scenario: Code without use closed file
    Given <filename>.c doesn't have use closed file
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"
