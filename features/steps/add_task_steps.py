from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
from pages.task_page import TaskPage

@given("the user is on the homepage")
def step_given_user_on_homepage(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_to_homepage()

@when("the user clicks on the \"Add Task\" button")
def step_when_user_clicks_add_task_button(context):
    context.home_page.click_add_task_button()

@when("enters a task name and description")
def step_when_user_enters_task_details(context):
    context.task_page = TaskPage(context.driver)
    context.task_page.enter_task_details("Task 1", "Description for Task 1")

@when("clicks the \"Save\" button")
def step_when_user_clicks_save_button(context):
    context.task_page.click_save_button()

@then("the task should be added to the task list")
def step_then_task_added_to_list(context):
    assert context.task_page.is_task_added_to_list(), "Task not added to the list."

@then("the task details should be displayed on the page")
def step_then_task_details_displayed(context):
    assert context.task_page.is_task_details_displayed(), "Task details not displayed on the page."