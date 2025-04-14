from selenium.webdriver.common.by import By

class MenuSidebar:

    origenes_datos = (By.CLASS_NAME, "v-list-item__title")
    recu = (By.CLASS_NAME, "v-list-item__title")
    encuestas = (By.XPATH, "//span[contains(text(),'Encuestas')]")
    finalizados = (By.XPATH, "//span[contains(text(),'Finalizados')]")
    abandono = (By.XPATH, "//span[contains(text(),'Abandono')]")