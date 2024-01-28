@ForFutureImplementation
Feature: User Authentication

  Scenario: User registration
    Given the user is on the registration page
    When the user provides valid registration details
    Then the user should be registered successfully

  Scenario: User login
    Given the user is on the login page
    When the user provides valid login credentials
    Then the user should be logged in successfully