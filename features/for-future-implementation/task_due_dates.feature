@ForFutureImplementation
Feature: Task Due Dates

  Scenario: Set due date for a task
    Given the user has an active account with tasks
    When the user sets a due date for a task
    Then the task due date should be updated in the todo-list

  Scenario: Receive reminders for approaching due dates
    Given the user has an active account with tasks and due dates
    When the due date for a task approaches
    Then the user should receive a reminder
