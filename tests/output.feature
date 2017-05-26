Feature: Output
    Code analysis beyond compilation

Scenario: Uninitialized variable analysis
    Given the code has uninitialized variables
    When it is submitted to SuSy
    Then I shouldt receive the following message “[test.cpp:4]: (error) Variável não inicializada"
