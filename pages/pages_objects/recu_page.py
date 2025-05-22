from selenium.webdriver.common.by import By
from pages.actions.base_actions import BaseActions

class RecuPage(BaseActions):
    #def is_recu_page_displayed(self):
    #    return self.is_visible((By.XPATH, "//h6[contains(text(),'Reporte Estructurado de Calidad Universitaria')]"))

    #def click_generar_button(self):
     #   self.click((By.XPATH, "//button[normalize-space()='GENERAR']"))

    #def click_explorar_by_title(self, title):
    #    self.click((By.XPATH,
                #    f"//div[contains(text(), '{title}')]/ancestor::div[contains(@class, 'card')]//button[contains(text(),'EXPLORAR')]"))

    btn_generar = (By.CSS_SELECTOR,".v-btn--primary:nth-child(3) > .v-btn__content")

    titulo_formulario_generar=(By.CLASS_NAME, "header2")
    campo_titulo =(By.ID, "input-734")
    campo_notas=(By.ID, "input-649")
    select_periodo =(By.CSS_SELECTOR, ".v-input--is-focused .v-select__selections)")
    #select_periodo=(By.ID,"v-select__selections")
    select_tipo= ("v-select__selections")
    select_estrategia= ()
    select_modo= ()
    importar_excel=()
    btn_confirmar_generar= ()