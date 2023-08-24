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
from webdriver_manager.chrome import ChromeDriverManager
driver_exec_path = ChromeDriverManager().install()


class Tracker:

    # Main entry point when running the application.
    def __init__(self):    

        # Initalize a browser driver to automate web browser (Chrome)
        self.driver = uc.Chrome(driver_executable_path=driver_exec_path)

        # Bank Url
        self.bank_url = "https://online.asb.co.nz/auth/?fm=header:login"

        # Initalize flag to false
        self.login_successful = False
     
        self.login()
        time.sleep(2)

        new_url = self.driver.current_url

        if new_url != self.bank_url:
            self.login_successful = True
       

        
        time.sleep(5)

    
        
       



    def login(self):
        # Retrieve bank username and password from environment variables
        username = os.environ.get('BANK_USERNAME')
        password = os.environ.get('BANK_PASSWORD')

        # Navigate to bank website
        self.driver.get(self.bank_url)

        # Appropriate fields to enter username and password
        usernameField = self.driver.find_element(By.ID, "dUsername")
        usernameField.send_keys(username)
        passwordField = self.driver.find_element(By.ID,"password")
        passwordField.send_keys(password)


        # Login via clicking
        loginField = self.driver.find_element(By.ID, "loginBtn")
        loginField.click()

        
        
if __name__ == '__main__':
    instance = Tracker()