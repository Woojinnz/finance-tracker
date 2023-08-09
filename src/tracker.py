# Import os to get Environment Variables for bank username and password
import os
# Import selenium to automate web browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Main entry point when running the application.
def main():    
    # Retrieve bank username and password from environment variables
    username = os.environ.get('BANK_USERNAME')
    password = os.environ.get('BANK_PASSWORD')

    # Initalize a browser driver to automate web browser (Chrome)
    driver = webdriver.Chrome()

    # Navigate to bank website
    bank_url = "https://online.asb.co.nz/auth/?fm=header:login"
    driver.get(bank_url)

    # Appropriate fields to enter username and password
    usernameField = driver.find_element(By.ID, "dUsername")
    usernameField.send_keys(username)
    passwordField = driver.find_element(By.ID,"password")
    passwordField.send_keys(password)

    # Login via clicking
    loginField = driver.find_element(By.ID, "loginBtn")
    loginField.click()
    