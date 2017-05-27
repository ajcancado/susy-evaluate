Feature: Input
    An app that reads a file that has a list of code files

Scenario: All files have errors reported by cppcheck 
    Given a file that contains a list of files
    When I call the app with the file as parameter
    Then shows me a list of files with errors


Scenario: Not all files have errors reported by cppcheck
	Given a file that contains a list of good and bad files
	When I call the app with the file as parameter
	Then shows me a list of files with errors

Scenario: No files have errors reported by cppcheck
	Given a file that contains a list of good files
	When I call the app with the file as parameter
	Then shows me nothing