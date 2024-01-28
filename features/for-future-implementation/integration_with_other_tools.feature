@ForFutureImplementation
Feature: Integration with Other Tools

  Scenario: Integrate todo-list with a calendar
    Given the user has an active account
    When the user integrates the todo-list with a calendar
    Then tasks with due dates should be synchronized with the calendar