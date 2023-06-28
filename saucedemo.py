import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from POM.loginPage import loginPage
from POM.data import inputan

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/" 

    def test_a_success_login(self):
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_login(self, driver)

    def test_a_failed_login(self):
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        baseLogin.test_failedlogin(self, driver, inputan.invalid_user, inputan.invalid_passw)
        #validasi
        response_data = driver.find_element(By.CSS_SELECTOR, loginPage.errorMsg).text
        self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()