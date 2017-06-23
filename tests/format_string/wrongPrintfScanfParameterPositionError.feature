Feature: Wrong Printf Scanf Parameter Position Error
    Code analysis beyond compilation

Scenario: Code with wrong printf scanf parameter position error 
    Given <filename>.c has wrong printf scanf parameter position error
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Referenciamento de parâmetro foi realizado incorretamente"

Scenario: Code without wrong printf scanf parameter position error
    Given <filename>.c doesn't have wrong printf scanf parameter position error
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Referenciamento de parâmetro foi realizado incorretamente"