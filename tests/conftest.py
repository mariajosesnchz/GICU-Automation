from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    driver= webdriver.Chrome()
    yield driver
    #driver.quit()