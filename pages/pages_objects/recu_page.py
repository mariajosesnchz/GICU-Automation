from selenium.webdriver.common.by import By
from pages.actions.base_actions import BaseActions

class RecuPage(BaseActions):
    btn_generar = (By.CSS_SELECTOR,".v-btn--primary:nth-child(3) > .v-btn__content")
    titulo_formulario_generar=(By.CLASS_NAME, "header2")
    campo_titulo =(By.ID, "input-734")
    campo_notas=(By.ID, "input-649")
    select_dropdown=(By.CSS_SELECTOR,"div.v-input.v-select")
    input_archivo = (By.NAME, "file_input")
    btn_confirmar_generar=(By.CSS_SELECTOR,".v-btn--primary:nth-child(2) > .v-btn__content")
    @staticmethod
    def opcion_dropdown_con_texto(texto):
        return By.XPATH, f"//div[contains(@class,'v-list-item__title') and contains(text(), '{texto}')]"


