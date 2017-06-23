Feature: Truncated Long Cast Return
    Code analysis beyond compilation

Scenario: Code with truncated long cast return 
    Given <filename>.c has truncated long cast return
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação"

Scenario: Code without truncated long cast return
    Given <filename>.c doesn't have truncated long cast return
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação"