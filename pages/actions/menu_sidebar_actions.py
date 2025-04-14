from pages.actions.base_actions import BaseActions
from pages.pages_objects.menu_sidebar import MenuSidebar

class MenuSidebarActions(BaseActions):

    def click_origenes_de_datos(self):
        """Hace click en el elemento que contenga el texto 'Orígenes de datos' (con o sin error ortográfico)."""
        webelements = self.driver.find_elements(*MenuSidebar.origenes_datos)
        print(f"[DEBUG] Elementos encontrados con selector {MenuSidebar.origenes_datos}: {len(webelements)}")

        for i, el in enumerate(webelements):
            texto = el.text.strip()
            print(f"[DEBUG] Elemento #{i}: '{texto}'")

            if "Orígenes de datos" in texto or "Orígines de datos" in texto:
                print("[DEBUG] Se encontró el elemento correcto. Haciendo scroll y click...")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                el.click()
                return
        raise Exception("No se encontró el elemento 'Orígenes de datos'")

    def go_to_recu(self):
        """Hace click en el enlace 'Recu' dentro del menú lateral."""
        webelements = self.driver.find_elements(*MenuSidebar.recu)
        print(f"[DEBUG] Buscando 'Recu' con selector {MenuSidebar.recu}. Elementos encontrados: {len(webelements)}")

        for i, el in enumerate(webelements):
            texto = el.text.strip()
            print(f"[DEBUG] Elemento #{i}: '{texto}'")

            if "recu" in texto.lower():
                print("[DEBUG] Se encontró el enlace 'Recu'. Haciendo scroll y click...")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
                el.click()
                return

        raise Exception("No se encontró el enlace 'Recu' en el menú lateral.")

    def go_to_encuestas(self):
        self.element_click(MenuSidebar.encuestas)

    def go_to_finalizados(self):
        self.element_click(MenuSidebar.finalizados)

    def go_to_abandono(self):
        self.element_click(MenuSidebar.abandono)

