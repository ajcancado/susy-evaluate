Feature: Pointer Arith Boolean
    Code analysis beyond compilation

Scenario: Code with Pointer Arith Boolean 
    Given <filename>.c has Pointer Arith Boolean
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Valor booleano atribuído a ponteiro"

Scenario: Code without Pointer Arith Boolean
    Given <filename>.c doesn't have Pointer Arith Boolean
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
