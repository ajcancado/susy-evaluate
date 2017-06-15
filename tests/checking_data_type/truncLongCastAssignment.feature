Feature: Truncated Long Cast Assignment
    Code analysis beyond compilation

Scenario: Code with truncated long cast assignment 
    Given <filename>.c has truncated long cast assignment
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação"

Scenario: Code without truncated long cast assignment
    Given <filename>.c doesn't have truncated long cast assignment
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
