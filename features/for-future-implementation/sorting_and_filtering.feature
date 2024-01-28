@ForFutureImplementation
Feature: Sorting and Filtering

  Scenario: Sort tasks based on different criteria
    Given the user has an active account with tasks
    When the user chooses to sort tasks based on a specific criterion
    Then the tasks should be displayed in the specified order

  Scenario: Filter tasks based on specific criteria
    Given the user has an active account with tasks
    When the user applies a filter based on specific criteria
    Then only the relevant tasks should be displayed