#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#import pytest

#@pytest.fixture(scope="function")
#def driver():
#    driver= webdriver.Chrome()
#    yield driver
#    driver.quit()


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")  # opcional: para correr sin abrir ventana

    driver = webdriver.Firefox(options=options)  # No necesitas especificar el path
    driver.maximize_window()
    yield driver
    driver.quit()


