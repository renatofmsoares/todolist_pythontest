@ForFutureImplementation
Feature: Task Prioritization

  Scenario: Set task priority
    Given the user has an active account with tasks
    When the user sets the priority for a task
    Then the task priority should be updated in the todo-list