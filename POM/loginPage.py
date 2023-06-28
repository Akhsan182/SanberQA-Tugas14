from selenium.webdriver.common.by import By

class loginPage():
    Username = "username"
    passw = "password"
    errorMsg = "[data-test='error']"
    loginTitle = "title"

    addUsername = (By.CSS_SELECTOR, "[data-test='username']")