Feature: Memory leak
    Code analysis beyond compilation

Scenario: Code with memory leak 
    Given a1.c has memory leak
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória"

Scenario: Code without memory leak
    Given a2.c doesn't have memory leak
    When it is submitted to the app
    Then shows me "[a2.c]: Nenhum erro de análise estática foi encontrado" 