from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    
    # --- Locators (Privados) ---
    _URL = "https://www.saucedemo.com/"
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    # --- Constructor ---
    def __init__(self, driver):
        self.driver = driver

    # --- Métodos de Acción (Encadenables) ---
    
    def abrir(self):
        """Navega a la página de login."""
        self.driver.get(self._URL)
        return self # Retorna self para encadenar métodos

    def ingresar_usuario(self, usuario):
        """Ingresa el nombre de usuario."""
        self.driver.find_element(*self._USERNAME_INPUT).send_keys(usuario)
        return self

    def ingresar_password(self, password):
        """Ingresa la contraseña."""
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(password)
        return self

    def clic_login(self):
        """Hace clic en el botón de login."""
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        # Al hacer clic, la página cambia, así que no retornamos 'self'
        
        
    def realizar_login(self, usuario, password):
        """Realiza el flujo de login completo."""
        self.ingresar_usuario(usuario).ingresar_password(password).clic_login()
        # Retorna una nueva Page Object si el login es exitoso
        if "inventory.html" in self.driver.current_url:
            from .inventory_page import InventoryPage
            return InventoryPage(self.driver)
        return self # O retorna self si el login falló

    # --- Métodos de Verificación (No usan Assert) ---
    
    def obtener_mensaje_error(self):
        """Retorna el texto del mensaje de error."""
        try:
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        except NoSuchElementException:
            return None