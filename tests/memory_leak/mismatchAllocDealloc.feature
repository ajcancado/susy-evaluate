Feature: Mismatch Allocation and Deallocation
    Code analysis beyond compilation

Scenario: Code with mismatch allocation and deallocation 
    Given <filename>.c has mismatch allocation and deallocation
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"

Scenario: Code without mismatch allocation and deallocation
    Given <filename>.c doesn't have mismatch allocation and deallocation
    When it is submitted to the app
    Then it doesn't show me "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"