Feature: Read Write Only File
    Code analysis beyond compilation

Scenario: Code with read write only file 
    Given <filename>.c has read write only file
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de leitura em um arquivo que foi aberto somente para escrita"

Scenario: Code without read write only file
    Given <filename>.c doesn't have read write only file
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Operação de leitura em um arquivo que foi aberto somente para escrita"
