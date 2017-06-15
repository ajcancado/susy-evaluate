Feature: Incorrect String Boolean Error
    Code analysis beyond compilation

Scenario: Code with incorrect string boolean error 
    Given <filename>.c has incorrect string boolean error
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Conversão literal de variável tipo carácter para booleano sempre é verdadeiro"

Scenario: Code without incorrect string boolean error
    Given <filename>.c doesn't have incorrect string boolean error
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
