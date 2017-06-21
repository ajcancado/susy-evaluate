Feature: known Condition True False
    Code analysis beyond compilation

Scenario: Code with known condition true false 
    Given <filename>.c has known condition true false
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Condição sempre verdadeira ou falsa"

Scenario: Code without known condition true false
    Given <filename>.c doesn't have known condition true false
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 