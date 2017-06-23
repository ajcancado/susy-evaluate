Feature: Wrong Print Scanf Argument Number
    Code analysis beyond compilation

Scenario: Code with wrong print scanf argument number 
    Given <filename>.c has wrong print scanf argument number
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"

Scenario: Code without wrong print scanf argument number
    Given <filename>.c doesn't have wrong print scanf argument number
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"