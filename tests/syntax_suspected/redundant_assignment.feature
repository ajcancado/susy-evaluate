Feature: Redundant Assignment
    Code analysis beyond compilation

Scenario: Code with redundant assignment
    Given <filename>.c has redundant assignment
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição redundante"

Scenario: Code without redundant assignment
    Given <filename>.c doesn't have redundant assignment
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"