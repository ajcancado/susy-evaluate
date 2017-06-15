Feature: Dealloc Dealloc
    Code analysis beyond compilation

Scenario: Code with dealloc dealloc 
    Given <filename>.c has dealloc dealloc
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"

Scenario: Code without dealloc dealloc
    Given <filename>.c doesn't have dealloc dealloc
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
