import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito_exitoso():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver,10)
    
    try:
             #Abrir pagina
                driver.get("https://www.saucedemo.com")
        
                #Testing de login existoso


                usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
                
                password = driver.find_element (By.ID,"password")
                login_boton = driver.find_element (By.ID,"login-button")
        
            
                password.send_keys("secret_sauce")
                login_boton.click()
                print(driver.find_element(By.TAG_NAME, "body").text)
        
                assert "/inventory.html" in driver.current_url

            #tesing de agregar al carrito producto
            
                primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

                nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

                addproduct = primer_producto.find_element (By.ID,"add-to-cart-sauce-labs-backpack")
                addproduct.click()

                contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

                assert contador_carrito.text == "1"

                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

                producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))

                assert producto_carrito.text == nombre_producto


    finally: driver.quit()