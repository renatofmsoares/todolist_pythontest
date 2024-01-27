# pages/task_page.py
from selenium.webdriver.common.by import By

class TaskPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_task_details(self, task_name, task_description):
        task_name_input = self.driver.find_element(By.ID, "task-name-input")
        task_description_input = self.driver.find_element(By.ID, "task-description-input")

        task_name_input.send_keys(task_name)
        task_description_input.send_keys(task_description)

    def click_save_button(self):
        save_button = self.driver.find_element(By.ID, "save-task-button")
        save_button.click()

    def is_task_added_to_list(self):
        # Implement logic to check if the task is added to the list
        pass

    def is_task_details_displayed(self):
        # Implement logic to check if task details are displayed on the page
        pass