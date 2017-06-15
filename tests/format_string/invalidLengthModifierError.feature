Feature: Invalid Length Modifier Error
    Code analysis beyond compilation

Scenario: Code with invalid length modifier error 
    Given <filename>.c has invalid length modifier error
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Formato de 'string/char*' modificado não pode ser utilizado sem conversão específica"

Scenario: Code without invalid length modifier error
    Given <filename>.c doesn't have invalid length modifier error
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
