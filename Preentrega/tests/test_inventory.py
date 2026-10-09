import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory():
    driver = webdriver.Chrome()

    try:
        #Abrir pagina
        driver.get("https://www.saucedemo.com")

        #Testing de login ecistoso
        usuario = driver.find_element (By.ID, "user-name")
        password = driver.find_element (By.ID,"password")
        login_boton = driver.find_element (By.ID,"login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_boton.click()

        assert "/inventory.html" in driver.current_url

        #Testing de Titulo
        logo = driver.find_element (By.CLASS_NAME, "app_logo")

        assert logo.text == "Swag Labs"

        titulo  = driver.find_element (By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"


        #Testing de productos      
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0

        primer_producto = productos [0]

        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"

        #Testing menu de hamburguesa
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert filtro.is_displayed()
    

    finally:
        driver.quit()