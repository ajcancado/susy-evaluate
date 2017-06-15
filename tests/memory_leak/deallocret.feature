Feature: Dealloc Return error
    Code analysis beyond compilation

Scenario: Code with dealloc return error 
    Given <filename>.c has dealloc return error
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Retorno/acesso de variável já desalocada"

Scenario: Code without dealloc return error
    Given <filename>.c doesn't have dealloc return error
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
