from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("http://localhost:5000")  # Update with your application's URL

    def click_add_task_button(self):
        add_task_button = self.driver.find_element(By.ID, "add-task-button")
        add_task_button.click()