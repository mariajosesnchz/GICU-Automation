from pages.actions.base_actions import BaseActions
from pages.pages_objects.menu_sidebar import MenuSidebar

class MenuSidebarActions(BaseActions):
    def click_origenes_datos(self):
        self.element_click(MenuSidebar.origenes_datos)

    def go_to_recu(self):
        self.element_click(MenuSidebar.recu)

    def go_to_encuestas(self):
        self.element_click(MenuSidebar.encuestas)

    def go_to_finalizados(self):
        self.element_click(MenuSidebar.finalizados)

    def go_to_abandono(self):
        self.element_click(MenuSidebar.abandono)