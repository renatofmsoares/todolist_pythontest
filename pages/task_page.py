from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TaskPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_task_details(self, task_title, task_description):
        task_title_input = self.driver.find_element(By.ID, "task-title-input")
        task_description_input = self.driver.find_element(By.ID, "task-description-input")

        task_title_input.send_keys(task_title)
        task_description_input.send_keys(task_description)

    def click_add_button(self):
        add_button = self.driver.find_element(By.ID, "task-add-button")
        add_button.click()

    def is_task_added_to_list(self, task_title):
        task_list = self.driver.find_element(By.ID, "task-list").find_elements(By.TAG_NAME, "li")
        for task_element in task_list: # print(task_element.text)
            if task_element.text.__contains__(task_title):
                return True
        return False

    def is_task_details_displayed(self, task_title, task_description):
        return self.driver.find_element(By.XPATH, f"//li[contains(text(), '{task_title}') and contains(text(), '{task_description}')]")
    
    


        