Feature: Add Task Functionality
  
  @implemented
  Scenario: User adds a new task
    Given the user is on the homepage
    When the user clicks on the "Add Task" button
    And enters a task name and description
    And clicks the "Save" button
    Then the task should be added to the task list
    And the task details should be displayed on the page