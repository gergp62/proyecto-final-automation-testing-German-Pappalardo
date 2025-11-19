from selenium.webdriver.common.by import By

class CheckoutPage:

    # --- Locators ---
    # Paso 1: Formulario
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _ZIP_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")

    # Paso 2: Resumen (Overview)
    _FINISH_BUTTON = (By.ID, "finish")

    # Paso 3: Completado
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    # --- Acciones ---

    def completar_formulario(self, nombre, apellido, codigo_postal):
        """Llena el formulario de envío y continúa."""
        self.driver.find_element(*self._FIRST_NAME).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME).send_keys(apellido)
        self.driver.find_element(*self._ZIP_CODE).send_keys(codigo_postal)
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        return self # Retorna self porque seguimos en el flujo de checkout

    def finalizar_compra(self):
        """Hace clic en el botón Finish en la pantalla de resumen."""
        self.driver.find_element(*self._FINISH_BUTTON).click()
        return self

    # --- Verificaciones ---

    def obtener_mensaje_final(self):
        """Obtiene el mensaje de éxito de la orden."""
        try:
            return self.driver.find_element(*self._COMPLETE_HEADER).text
        except:
            return None