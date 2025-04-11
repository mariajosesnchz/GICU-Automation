from pages.actions.login_actions import LoginActions
from pages.actions.menu_sidebar_actions import MenuSidebarActions
from utils.dismiss_popup import dismiss_password_alert


def test_click_origenes_de_datos(driver):
    login = LoginActions(driver)
    #login.load("https://gicu-app-release-quality.ctdesarrollo.org/login")
    login.load("https://gicu-beta.uneatlantico.es/login")
    login.type_user("johndoe@example.com")
    #login.type_password("")
    login.click_second_button_to_login()
    #dismiss_password_alert(driver)
    login.user_is_logged()

    menu = MenuSidebarActions(driver)
    menu.click_origenes_datos()



    #sidebar = MenuSidebarActions(driver)
    #sidebar.click_origenes_datos()