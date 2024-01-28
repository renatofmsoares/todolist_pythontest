
@ForFutureImplementation
Feature: Manage Tasks

  Scenario: Add a new task
    Given the user has an active account
    When the user adds a new task with a title and description
    Then the task should be added to the todo-list

  Scenario: Mark a task as completed
    Given the user has an active account with tasks
    When the user marks a task as completed
    Then the task status should be updated to completed

  Scenario: Edit task details
    Given the user has an active account with tasks
    When the user edits the title or description of an existing task
    Then the task details should be updated in the todo-list

  Scenario: Delete a task
    Given the user has an active account with tasks
    When the user deletes a task
    Then the task should be removed from the todo-list