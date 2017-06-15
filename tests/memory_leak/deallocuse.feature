Feature: Dealloc Use
    Code analysis beyond compilation

Scenario: Code with dealloc use 
    Given <filename>.c has dealloc use
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a variável já desalocada"

Scenario: Code without dealloc use
    Given <filename>.c doesn't have dealloc use
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
