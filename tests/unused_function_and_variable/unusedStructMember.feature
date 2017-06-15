Feature: Unused Struct Member
    Code analysis beyond compilation

Scenario: Code with unused struct member 
    Given <filename>.c has unused struct member
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi utilizada"

Scenario: Code without unused struct member
    Given <filename>.c doesn't have unused struct member
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
