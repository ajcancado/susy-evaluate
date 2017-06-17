Feature: Input
    An app that reads a file that has a list of code files

Scenario: All files have errors reported by cppcheck
    Given case1_input.txt contains a file list with programming errors: a1.c and a2.c
    When I call the app with the container file as parameter
    Then shows me a file list with programming errors: a1.c, a2.c

Scenario: Not all files have errors reported by cppcheck
  	Given case2_input.txt contains a file with programming errors and a file without programming errors: a1.c and a2.c
  	When I call the app with the container file as parameter
  	Then shows me a file list with programming errors: a1.c

Scenario: Files without errors reported by cppcheck
  	Given case3_input.txt contains a file list without programming errors: a1.c
  	When I call the app with the container file as parameter
  	Then shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"

Scenario: Files with invalid path
  	Given case4_input.txt contains a file list with invalid path
  	When I call the app with the container file as parameter
  	Then shows me nothing

Scenario: Files with invalid extension
  	Given case5_input.txt contains a file list with invalid extension
  	When I call the app with the container file as parameter
  	Then shows me nothing
