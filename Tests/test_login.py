
import pytest
from pages import LoginPage, InventoryPage
from utils.data_loader import get_csv_data

# Cargamos los datos UNA sola vez al inicio
datos_usuarios = get_csv_data("users.csv")

# Convertimos la lista de diccionarios a una lista de tuplas para pytest
# Formato esperado: [("standard_user", "secret_sauce", "success"), ...]
lista_params_usuarios = [
    (user['username'], user['password'], user['expected_result']) 
    for user in datos_usuarios
]


@pytest.mark.smoke
@pytest.mark.login
def test_login_exitoso(driver, credenciales_validas):
    """
    Prueba el login exitoso con credenciales válidas.
    (Equivale a tu test_login_success)
    """
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(
        credenciales_validas["usuario"],
        credenciales_validas["password"]
    )
    
    inventory_page = InventoryPage(driver)
    assert inventory_page.esta_en_pagina_inventario(), "El login falló o no redirigió a inventario"
    assert inventory_page.obtener_titulo_pagina() == "Products", "El título de la página no es 'Products'"

@pytest.mark.login
def test_login_usuario_bloqueado(driver, usuario_bloqueado):
    """Prueba el mensaje de error para un usuario bloqueado."""
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(
        usuario_bloqueado["usuario"],
        usuario_bloqueado["password"]
    )
    
    mensaje_error = login_page.obtener_mensaje_error()
    assert mensaje_error is not None, "No se mostró ningún mensaje de error"
    assert "locked out" in mensaje_error, "El mensaje de error no es el esperado"


@pytest.mark.login
@pytest.mark.parametrize("usuario, password, resultado_esperado", lista_params_usuarios)
def test_login_data_driven(driver, usuario, password, resultado_esperado):
    """
    Test único que corre 4 veces (una por cada línea del CSV).
    Valida tanto casos positivos como negativos.
    """
    login_page = LoginPage(driver)
    login_page.abrir().realizar_login(usuario, password)
    
    if resultado_esperado == "success":
        inventory_page = InventoryPage(driver)
        assert inventory_page.esta_en_pagina_inventario(), f"El usuario {usuario} debería haber entrado pero falló."
        
    elif resultado_esperado == "locked_out":
        error_msg = login_page.obtener_mensaje_error()
        assert "locked out" in error_msg, f"El usuario {usuario} debería estar bloqueado."    