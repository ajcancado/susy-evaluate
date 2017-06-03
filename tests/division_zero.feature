Feature: Division by zero
    Code analysis beyond compilation

Scenario: Code with division by zero
    Given a1.c has a division by zero
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (error) Divisão por zero"

Scenario: Code without division by zero
    Given a2.c doesn't have a division by zero
    When it is submitted to the app
    Then  shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"
