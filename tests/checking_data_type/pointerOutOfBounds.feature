Feature: Pointer Out Of Bounds
    Code analysis beyond compilation

Scenario: Code with pointer out of bounds 
    Given <filename>.c has pointer out of bounds
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a posição inválida do ponteiro"

Scenario: Code without pointer out of bounds
    Given <filename>.c doesn't have pointer out of bounds
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Acesso a posição inválida do ponteiro"
