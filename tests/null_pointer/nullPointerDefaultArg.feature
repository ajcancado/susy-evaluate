Feature: Null Pointer Default Argument
    Code analysis beyond compilation

Scenario: Code with null pointer default argument 
    Given <filename>.c has null pointer default argument
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso a ponteiro nulo se o valor padrão foi utilizado"

Scenario: Code without null pointer default argument
    Given <filename>.c doesn't have null pointer default argument
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Possível acesso a ponteiro nulo se o valor padrão foi utilizado"