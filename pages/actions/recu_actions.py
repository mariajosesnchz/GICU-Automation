from datetime import time

from pages.pages_objects.recu_page import RecuPage
from pages.actions.base_actions import BaseActions


class RecuActions(BaseActions):

    def generar_nuevo_recu(self, titulo, notas, periodo, tipo, estrategia, modo):
        self.element_click(RecuPage.btn_generar)
        self.type_info(RecuPage.campo_titulo, titulo)
        self.send_keys(RecuPage.campo_notas, notas)
        self.select_dropdown_by_text(RecuPage.select_periodo, periodo)
        self.select_dropdown_by_text(RecuPage.select_tipo, tipo)
        self.select_dropdown_by_text(RecuPage.select_estrategia, estrategia)
        self.select_dropdown_by_text(RecuPage.select_modo, modo)
        self.element_click(RecuPage.boton_confirmar_generar)

    def click_generar_button(self):
        botones = self.driver.find_elements(*RecuPage.btn_generar)
        for i, boton in enumerate(botones):
            try:
                span = boton.find_element(*RecuPage.btn_generar)
                print(f"[DEBUG] Botón #{i}: '{span.text.strip()}'")
                if span.text.strip() == "Generar":
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton)
                    boton.click()
                    print("✅ Se hizo clic en el botón 'Generar'")
                    return
            except:
                continue
        raise Exception("❌ No se encontró ningún botón con el texto 'Generar'")





