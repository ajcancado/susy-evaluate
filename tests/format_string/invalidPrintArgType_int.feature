Feature: Invalid Print Argument Type Integer
    Code analysis beyond compilation

Scenario: Code with invalid print argument type integer 
    Given <filename>.c has invalid print argument type integer
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'int' é inválido neste caso"

Scenario: Code without invalid print argument type integer
    Given <filename>.c doesn't have invalid print argument type integer
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
