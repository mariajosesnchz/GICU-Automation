from selenium.webdriver.common.by import By

class MenuSidebar:

    origenes_datos = (By.CLASS_NAME, "v-app-bar__nav-icon hidden-lg-and-up v-btn v-btn--icon v-btn--round theme--light v-size--default")
    recu = (By.XPATH, "//span[contains(text(),'Recu')]")
    encuestas = (By.XPATH, "//span[contains(text(),'Encuestas')]")
    finalizados = (By.XPATH, "//span[contains(text(),'Finalizados')]")
    abandono = (By.XPATH, "//span[contains(text(),'Abandono')]")