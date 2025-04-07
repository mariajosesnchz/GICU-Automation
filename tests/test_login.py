from pages.actions.login_actions import LoginActions


def test_fill_form(driver):
    login = LoginActions(driver)
    #login.load("https://gicu-app-release-quality.ctdesarrollo.org/login")
    login.load("https://gicu-beta.uneatlantico.es/login")
    login.type_user("johndoe@example.com")
    #login.type_password("")
    login.click_second_button_to_login()
    login.user_is_logged()




