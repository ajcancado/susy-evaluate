Feature: Invalid Scanf Argument Type Float
    Code analysis beyond compilation

Scenario: Code with invalid scanf argument type float 
    Given <filename>.c has invalid scanf argument type float
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo 'float' inválido"

Scenario: Code without invalid scanf argument type float
    Given <filename>.c doesn't have invalid scanf argument type float
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
