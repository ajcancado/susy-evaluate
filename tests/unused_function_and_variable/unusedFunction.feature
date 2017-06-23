Feature: Unused Function
    Code analysis beyond compilation

Scenario: Code with unused function 
    Given <filename>.c has unused function
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"

Scenario: Code without unused function
    Given <filename>.c doesn't have unused function
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"