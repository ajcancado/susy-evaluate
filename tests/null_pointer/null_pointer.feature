Feature: Null pointer dereference
    Code analysis beyond compilation

Scenario: Code with null pointer dereference
    Given a1.c has null pointer dereference
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (error) Desreferenciamento de ponteiro nulo"

Scenario: Code without null pointer dereference
    Given a2.c doesn't have null pointer dereference
    When it is submitted to the app
    Then shows me "[a2.c]: Nenhum erro de análise estática foi encontrado" 
