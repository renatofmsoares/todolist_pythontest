# features/support/environment.py
from selenium import webdriver

def before_all(context):
    print(context)
    context.driver = webdriver.Chrome()

def after_all(context):
    context.driver.quit()