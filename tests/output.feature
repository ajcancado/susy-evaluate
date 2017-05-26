Feature: Output
    Code analysis beyond compilation

Scenario: Uninitialized variable analysis
    Given the code has uninitialized variables
    When it is submitted to SuSy
    Then I shouldt receive the following message “[test1.c:2]: (error) Variável não inicializada"
