Feature: Uninitialized Struct Member
    Code analysis beyond compilation

Scenario: Code with uninitialized struct member
    Given <filename>.c has uninitialized struct member
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi inicializada"

Scenario: Code without uninitialized struct member
    Given <filename>.c doesn't have uninitialized struct member
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi inicializada"