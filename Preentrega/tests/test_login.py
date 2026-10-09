import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com")

        usuario = driver.find_element (By.ID, "user-name")
        password = driver.find_element (By.ID,"password")
        login_boton = driver.find_element (By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_boton.click()

        assert "/inventory.html" in driver.current_url

        

    finally:
        driver.quit()