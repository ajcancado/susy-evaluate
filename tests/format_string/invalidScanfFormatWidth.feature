Feature: Invalid Scanf Format Width
    Code analysis beyond compilation

Scenario: Code with invalid scanf format width 
    Given <filename>.c has invalid scanf format width
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato 'string/char*' é inválida"

Scenario: Code without invalid scanf format width
    Given <filename>.c doesn't have invalid scanf format width
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato 'string/char*' é inválida"