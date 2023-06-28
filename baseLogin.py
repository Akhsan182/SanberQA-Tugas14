import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from POM.loginPage import loginPage
from POM.data import inputan

def test_login(self, driver):
    driver.find_element(*loginPage.addUsername).send_keys(inputan.valid_user)
    driver.find_element(By.ID, loginPage.passw).send_keys(inputan.valid_passw) # isi password
    driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
    # validasi
    response_data = driver.find_element(By.CLASS_NAME, loginPage.loginTitle).text
    self.assertIn('Products', response_data)

def test_failedlogin(self, driver, username, password):
    driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password) # isi password
    driver.find_element(By.CLASS_NAME, "submit-button.btn_action").click()
