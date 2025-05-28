from pages.actions.login_actions import LoginActions
from pages.actions.menu_sidebar_actions import MenuSidebarActions
from pages.actions.recu_actions import RecuActions
from pages.pages_objects.recu_page import RecuPage



def test_generar_recu(driver):
    login = LoginActions(driver)
    #login.load("https://gicu-beta.uneatlantico.es/login")
    login.load("https://gicu-app-release-quality.ctdesarrollo.org/login")
    login.type_user("maria.sanchez@funiber.org")
    login.type_password("aHGYpUoRxg")
    login.click_second_button_to_login()
    login.user_is_logged()
    menu = MenuSidebarActions(driver)
    menu.click_origenes_de_datos()
    menu.go_to_recu()

    recu= RecuActions(driver)
    recu.click_generar_button()
    recu.type_titulo("RECU DETALLADO DE MASTERS 2023-2024")
    recu.generar_nuevo_recu("2024-2025", "RECU Detallado de Masters", "SpreadSheet Loader", "Manual",
                            r"C:\Users\Maria Sanchez\Downloads\RECUS\RECU Detallado Master 23-24.xlsx")
    recu.click_confirmar_generar_button()


    #RecuPage.select_periodo()











    #recu.generar_nuevo_recu(
        #titulo="QA Autotest Recu",
        #notas="Este es un test automatizado",
        #periodo="2023-2024",
        #tipo="Parcial",
        #estrategia="Estandar",
        #modo="Automático"
    #)


    # Aquí podrías validar que el nuevo recu aparece en la lista
    # (con un assert que busque el texto por ejemplo)

