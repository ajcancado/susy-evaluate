Feature: Buffer Access Out Of Bounds
    Code analysis beyond compilation

Scenario: Code with buffer access out Of bounds 
    Given <filename>.c has buffer access out Of bounds
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Vetor acessado em índice inválido, portanto fora do seu limite"

Scenario: Code without buffer access out Of bounds
    Given <filename>.c doesn't have buffer access out Of bounds
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
