from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class InventoryPage:
    
    # --- Locators ---
    _TITLE = (By.CLASS_NAME, "title")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    _PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _PRODUCT_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")

    # --- Constructor ---
    def __init__(self, driver):
        self.driver = driver

    # --- Métodos de Verificación ---
    
    def esta_en_pagina_inventario(self):
        """Verifica si la URL actual es la de inventario."""
        return "inventory.html" in self.driver.current_url

    def obtener_titulo_pagina(self):
        """Retorna el texto del título de la página."""
        try:
            return self.driver.find_element(*self._TITLE).text
        except NoSuchElementException:
            return None
            
    def obtener_cantidad_productos(self):
        """Retorna el número de productos visibles."""
        return len(self.driver.find_elements(*self._PRODUCT_ITEMS))

    def obtener_cantidad_badge_carrito(self):
        """Retorna el número en el ícono del carrito."""
        try:
            return self.driver.find_element(*self._CART_BADGE).text
        except NoSuchElementException:
            return None # Retorna None si el badge no existe (carrito vacío)

    # --- Métodos de Acción ---
    
    def agregar_producto_por_nombre(self, nombre_producto):
        """Agrega un producto al carrito buscándolo por su nombre."""
        # Lógica más compleja para encontrar el producto y su botón
        pass # Por ahora lo dejamos simple

    def agregar_primer_producto(self):
        """Agrega el primer producto de la lista al carrito."""
        self.driver.find_element(*self._PRODUCT_ADD_TO_CART_BUTTON).click()
        return self
        
    def obtener_info_primer_producto(self):
        """Retorna el nombre y precio del primer producto."""
        nombre = self.driver.find_element(*self._PRODUCT_NAME).text
        precio = self.driver.find_element(*self._PRODUCT_PRICE).text
        return {"nombre": nombre, "precio": precio}
        
    def ir_al_carrito(self):
        """Hace clic en el ícono del carrito y retorna la CartPage."""
        self.driver.find_element(*self._CART_LINK).click()
        from .cart_page import CartPage
        return CartPage(self.driver)