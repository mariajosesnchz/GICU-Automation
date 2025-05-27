from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.pages_objects.recu_page import RecuPage
from pages.actions.base_actions import BaseActions
from selenium.webdriver.support import expected_conditions as EC


class RecuActions(BaseActions):

    def  generar_nuevo_recu(self, periodo, tipo, estrategia, modo,ruta):
        #self.send_keys(RecuPage.campo_notas, notas)

        # Seleccionamos cada dropdown por índice
        self.select_dropdown_by_index(0, periodo)
        self.select_dropdown_by_index(1, tipo)
        self.select_dropdown_by_index(2, estrategia)
        self.select_dropdown_by_index(3, modo)
        self.subir_archivo(ruta)
        self.element_click(RecuPage.btn_confirmar_generar)

        # Aquí deberías ubicar el botón confirmar si existe
        #try:
        #    self.element_click(RecuPage.btn_confirmar_generar)
        #except Exception as e:
        #    print(f"[DEBUG] No se pudo hacer clic en confirmar: {e}")

    def select_dropdown_by_index(self, index, value_to_select):
        wait = WebDriverWait(self.driver, 10)
        dropdowns = wait.until(EC.presence_of_all_elements_located(RecuPage.select_dropdown))

        print(f"Cantidad de dropdowns encontrados: {len(dropdowns)}")
        dropdown = dropdowns[index]

        dropdown.click()  # Abre el menú

        # Espera el menú desplegable y hace clic en el valor deseado
        option = wait.until(EC.visibility_of_element_located(RecuPage.opcion_dropdown_con_texto(value_to_select)))
        option.click()


    def subir_archivo(self, ruta_archivo):
        wait = WebDriverWait(self.driver, 10)
        input_file = wait.until(EC.presence_of_element_located(RecuPage.input_archivo))
        input_file.send_keys(ruta_archivo)

    def click_generar_button(self):
        wait = WebDriverWait(self.driver, 10)

        # Esperamos a que los botones estén presentes
        botones = wait.until(EC.presence_of_all_elements_located(RecuPage.btn_generar))
        print(f"[DEBUG] Se encontraron {len(botones)} botones 'Generar'")

        for i in range(len(botones)):
            try:
                # Volvemos a capturar los botones para evitar errores stale
                botones_actualizados = wait.until(EC.presence_of_all_elements_located(RecuPage.btn_generar))
                boton = botones_actualizados[i]
                texto = boton.text.strip()
                print(f"[DEBUG] Botón #{i}: '{texto}'")

                if texto.lower() == "generar":
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", boton)
                    wait.until(EC.element_to_be_clickable(RecuPage.btn_generar))
                    boton.click()
                    print("✅ Se hizo clic en el botón 'Generar'") 
                    return
            except Exception as e:
                print(f"[DEBUG] Error con el botón #{i}: {e}")
                continue

        raise Exception("No se encontró ningún botón con el texto 'Generar'")

    def type_titulo(self, titulo: str):
        wait = WebDriverWait(self.driver, 5)


        try:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "v-overlay__scrim")))
        except TimeoutException:
            print("[DEBUG] El overlay no desapareció, pero se intentará continuar.")

        # Asegurarse que el campo sea clickeable
        wait.until(EC.element_to_be_clickable(RecuPage.campo_titulo))

        self.clear_field(RecuPage.campo_titulo)
        self.type_info(RecuPage.campo_titulo, titulo)











