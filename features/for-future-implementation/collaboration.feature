@ForFutureImplementation
Feature: Collaboration

  Scenario: Share tasks with other users
    Given the user has an active account with tasks
    When the user shares a task with another user
    Then the other user should be able to view the shared task