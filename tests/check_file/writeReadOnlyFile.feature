Feature: Write Read Only File
    Code analysis beyond compilation

Scenario: Code with write read only file 
    Given <filename>.c has write read only file
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de escrita em um arquivo que foi aberto somente para leitura"

Scenario: Code without write read only file
    Given <filename>.c doesn't have write read only file
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
