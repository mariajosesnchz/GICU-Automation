from selenium.webdriver.common.by import By

class Login:
    userInput = (By.ID, "input-17")
    passwordInput= (By.ID, "password")
    loginButton= (By.CLASS_NAME, "v-btn__content")
    userLoginMessage = (By.CLASS_NAME, "copyright-notice")