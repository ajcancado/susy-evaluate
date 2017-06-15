Feature: fflush On Input Stream
    Code analysis beyond compilation

Scenario: Code with fflush on input stream 
    Given <filename>.c has fflush on input stream
    When it is submitted to the app
    Then I should receive the following message "[<filename>.c:<linha>]: (erro) Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux"

Scenario: Code without fflush on input stream
    Given <filename>.c doesn't have fflush on input stream
    When it is submitted to the app
    Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado" 
