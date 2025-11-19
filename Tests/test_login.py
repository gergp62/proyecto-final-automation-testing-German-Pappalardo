import pytest
from pages import LoginPage, InventoryPage

@pytest.mark.smoke
@pytest.mark.login
def test_login_exitoso(driver, credenciales_validas):
    """
    Prueba el login exitoso con credenciales válidas.
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