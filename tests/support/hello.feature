Feature: Hello
    An app that says hello given a name

Scenario: Say hello
    Given I'm a student user
    When I give my name
    Then I should see a message that has hello before my name
