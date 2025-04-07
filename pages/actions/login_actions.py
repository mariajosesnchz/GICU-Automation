from .base_actions import BaseActions
from pages.pages_objects.login_page import Login
class LoginActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    def type_user(self, user: str):
        self.clear_field(Login.userInput) # Limpia el campo antes de escribir
        self.type_info(Login.userInput, user)
    def type_password (self, password: str):
        self.clear_field(Login.passwordInput)  # Limpia el campo antes de escribir
        self.type_info(Login.passwordInput, password)
    #def click_to_login(self):
        #self.element_click(Login.loginButton)

    def user_is_logged(self)-> bool:
       return self.is_displayed(Login.userLoginMessage)


    def click_second_button_to_login(self):
        """Hace click en el segundo elemento con la clase 'v-btn__content'."""
        webelements = self.driver.find_elements(*Login.loginButton)
        if len(webelements) > 1:
            segundo_elemento = webelements[1]
            print("Texto del segundo botón:", segundo_elemento.text)
            segundo_elemento.click()
        else:
            raise Exception("No hay suficientes elementos en la página para hacer click en el segundo.")