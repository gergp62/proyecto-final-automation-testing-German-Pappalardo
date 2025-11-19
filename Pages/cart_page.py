from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PageLoadException(Exception):
    pass

class CartPage:

    # --- Locators ---
    _TITLE = (By.CLASS_NAME, "title")
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    # --- Constructor ---
    def __init__(self, driver):
        self.driver = driver
        # Verificación automática al instanciar
        if not self.esta_en_pagina_carrito():
            raise PageLoadException("No se está en la página del carrito.")

    # --- Métodos de Verificación ---
    
    def esta_en_pagina_carrito(self):
        """Verifica si la URL actual es la del carrito."""
        return "cart.html" in self.driver.current_url

    def obtener_nombre_producto_en_carrito(self, nombre_producto):
        """Busca un producto por nombre en el carrito."""
        items = self.driver.find_elements(*self._CART_ITEMS)
        for item in items:
            if item.find_element(*self._ITEM_NAME).text == nombre_producto:
                return True
        return False

    def clic_checkout(self):
        """Hace clic en Checkout y nos lleva a la página de información."""
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        # Importamos aquí para evitar referencias circulares
        from .checkout_page import CheckoutPage
        return CheckoutPage(self.driver)    