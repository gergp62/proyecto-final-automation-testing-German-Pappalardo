import pytest
from pages import InventoryPage, CartPage

# Todos los tests en este archivo requieren un login previo
pytestmark = pytest.mark.usefixtures("usuario_logueado")

@pytest.mark.smoke
@pytest.mark.cart
def test_agregar_producto_al_carrito(driver):
    """
    Prueba añadir un producto y verifica el contador del carrito.
    
    """
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    
    assert inventory_page.obtener_cantidad_badge_carrito() == "1", "El contador no se actualizó"

@pytest.mark.cart
def test_verificar_producto_en_pagina_carrito(driver):
    """
    Prueba el flujo completo de agregar y navegar al carrito.
    
    """
    inventory_page = InventoryPage(driver)
    info_producto = inventory_page.obtener_info_primer_producto()
    inventory_page.agregar_primer_producto()
    
    # Navegación
    cart_page = inventory_page.ir_al_carrito()
    
    # Verificación en la nueva página
    assert cart_page.esta_en_pagina_carrito(), "No se redirigió a la página del carrito"
    assert cart_page.obtener_nombre_producto_en_carrito(info_producto["nombre"]), "El producto no está en el carrito"