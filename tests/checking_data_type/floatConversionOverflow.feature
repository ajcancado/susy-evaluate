Feature: Float Conversion Overflow
    Code analysis beyond compilation

Scenario: Code with float conversion overflow 
    Given <filename>.c has float conversion overflow
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow de variável do tipo 'float'"

Scenario: Code without float conversion overflow
    Given <filename>.c doesn't have float conversion overflow
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
