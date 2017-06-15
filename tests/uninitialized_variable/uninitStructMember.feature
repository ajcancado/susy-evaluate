Feature: Uninitiazed Struct Member
    Code analysis beyond compilation

Scenario: Code with uninitiazed struct member 
    Given <filename>.c has uninitiazed struct member
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi inicializada"

Scenario: Code without uninitiazed struct member
    Given <filename>.c doesn't have uninitiazed struct member
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
