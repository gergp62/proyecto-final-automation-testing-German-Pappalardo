import pytest
from selenium import webdriver

# --- Fixture del Driver ---

@pytest.fixture(scope="function")
def driver():
    """
    Fixture principal que crea y destruye la instancia del driver.
    Scope 'function': Se ejecuta una vez por cada función de test.
    """
    chrome_options = webdriver.ChromeOptions()
    # Deshabilita el pop-up "Chrome está siendo controlado..."
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Deshabilita el pop-up de guardar contraseña
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    
    # Agregamos "headless" para ejecución en CI
    chrome_options.add_argument("--headless")
    
    driver_instance = webdriver.Chrome(options=chrome_options)
    driver_instance.maximize_window()
    driver_instance.implicitly_wait(5) # Espera implícita
    
    # Ceder el driver al test
    yield driver_instance
    
    # Cleanup (Teardown) - Se ejecuta después del test
    driver_instance.quit()

# --- Fixtures de Datos ---

@pytest.fixture(scope="session")
def credenciales_validas():
    """Retorna un diccionario con credenciales válidas."""
    return {"usuario": "standard_user", "password": "secret_sauce"}

@pytest.fixture(scope="session")
def credenciales_invalidas():
    """Retorna un diccionario con credenciales inválidas."""
    return {"usuario": "bad_user", "password": "bad_password"}

@pytest.fixture(scope="session")
def usuario_bloqueado():
    """Retorna credenciales de un usuario bloqueado."""
    return {"usuario": "locked_out_user", "password": "secret_sauce"}


# --- Fixture de Estado (Fixture que usa fixtures) ---

@pytest.fixture(scope="function")
def usuario_logueado(driver, credenciales_validas):
    """
    Fixture que entrega un driver ya logueado en la página de inventario.
    Muy útil para todos los tests que NO sean de login.
    """
    from pages.login_page import LoginPage
    
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"]
    )
    # Entrega el control al test (que ya está en inventory.html)
    yield driver
    # El cleanup (logout) no es necesario porque el driver se destruye