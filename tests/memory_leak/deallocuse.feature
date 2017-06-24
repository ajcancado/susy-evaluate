Feature: Dealloc Use
    Code analysis beyond compilation

Scenario: Code with dealloc use 
    Given <filename>.c has dealloc use
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso à variável já desalocada"

Scenario: Code without dealloc use
    Given <filename>.c doesn't have dealloc use
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Acesso à variável já desalocada"