@ForFutureImplementation
Feature: Task Categories by Tags

  Scenario: Categorize tasks using tags
    Given the user has an active account with tasks
    When the user adds tags to a task
    Then the task should be categorized with the specified tags