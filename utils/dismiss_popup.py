from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def dismiss_password_alert(driver, timeout=5):
    """
    Acepta una alerta nativa del navegador si aparece.
    """
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Texto de la alerta: {alert.text}")
        alert.accept()
        print("✅ Alerta de navegador aceptada correctamente.")
    except TimeoutException:
        print("ℹ️ No apareció ninguna alerta nativa. Continuando el test.")
    except Exception as e:
        print(f"⚠️ Error inesperado al manejar la alerta: {e}")

