# Import os to get Environment Variables for bank username and password
import os

# Import selenium to automate web browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import time to add delays
import time

# Import Chrome Driver
import undetected_chromedriver as uc


class Tracker:

    # Main entry point when running the application.
    def __init__(self):    

        # Initalize a browser driver to automate web browser (Chrome)
        self.driver = uc.Chrome()

        self.login()
        login = True

        # Create an element so that the program waits until my primary account is loaded
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "account-123659006323050"))
        )

        # Click on the element to load the account and see transactions
        element.click()

    def login(self):
        # Retrieve bank username and password from environment variables
        username = os.environ.get('BANK_USERNAME')
        password = os.environ.get('BANK_PASSWORD')

        # Navigate to bank website
        bank_url = "https://online.asb.co.nz/auth/?fm=header:login"
        self.driver.get(bank_url)

        # Appropriate fields to enter username and password
        usernameField = self.driver.find_element(By.ID, "dUsername")
        usernameField.send_keys(username)
        time.sleep(5)
        passwordField = self.driver.find_element(By.ID,"password")
        passwordField.send_keys(password)
        time.sleep(5)


        # Login via clicking
        loginField = self.driver.find_element(By.ID, "loginBtn")
        loginField.click()
        
if __name__ == '__main__':
    instance = Tracker()