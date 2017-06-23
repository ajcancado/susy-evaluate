Feature: Unused Allocated Memory
    Code analysis beyond compilation

Scenario: Code with unused allocated memory 
    Given <filename>.c has unused allocated memory
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"

Scenario: Code without unused allocated memory
    Given <filename>.c doesn't have unused allocated memory
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"