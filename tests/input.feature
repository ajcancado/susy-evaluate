Feature: Input
    An app that reads a file that has a list of code files

Scenario: All files have errors reported by cppcheck 
    Given case1_input.txt contains a list of files: a1.c and a2.c
    When I call the app with the file as parameter
    Then shows me a list of files with errors: a1.c


Scenario: Not all files have errors reported by cppcheck
	Given case2_input.txt contains a list of good and bad files: a1.c and a2.c
	When I call the app with the file as parameter
	Then shows me a list of files with errors: a1.c

Scenario: No files have errors reported by cppcheck
	Given case3_input.txt contains a list of good file: a1.c
	When I call the app with the file as parameter
	Then shows me "[a1.c]: Nenhum erro de análise estática foi encontrado"