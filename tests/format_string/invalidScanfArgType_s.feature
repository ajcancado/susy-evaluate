Feature: Invalid Scanf Argument Type String
    Code analysis beyond compilation

Scenario: Code with invalid scanf argument type string 
    Given <filename>.c has invalid scanf argument type string
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo 'string/char*' inválido"

Scenario: Code without invalid scanf argument type string
    Given <filename>.c doesn't have invalid scanf argument type string
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo 'string/char*' inválido"