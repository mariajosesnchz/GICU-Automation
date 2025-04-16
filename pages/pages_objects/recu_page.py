from selenium.webdriver.common.by import By
from pages.actions.base_actions import BaseActions

class RecuPage(BaseActions):
    def is_recu_page_displayed(self):
        return self.is_visible((By.XPATH, "//h6[contains(text(),'Reporte Estructurado de Calidad Universitaria')]"))

    def click_generar_button(self):
        self.click((By.XPATH, "//button[normalize-space()='GENERAR']"))

    def click_explorar_by_title(self, title):
        self.click((By.XPATH,
                    f"//div[contains(text(), '{title}')]/ancestor::div[contains(@class, 'card')]//button[contains(text(),'EXPLORAR')]"))

    btn_generar = (By.CLASS_NAME,"v-btn__content")
    campo_titulo =(By.ID, "input-648")
    campo_notas=(By.ID, "input-649")
    select_periodo=(By.ID,"v-select__selections")
    select_tipo= ("v-select__selections")
    select_estrategia= ()
    select_modo= ()
    importar_excel=()
    btn_confirmar_generar= ()