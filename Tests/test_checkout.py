import pytest
from pages import InventoryPage

# Usamos la fixture para empezar ya logueados
pytestmark = pytest.mark.usefixtures("usuario_logueado")

@pytest.mark.smoke
def test_flujo_completo_compra_e2e(driver):
    """
    Prueba E2E: Agregar producto, ir al carrito, llenar datos y finalizar compra.
    """
    # 1. Estamos en Inventario (gracias a la fixture) - Agregamos producto
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    
    # 2. Ir al Carrito
    cart_page = inventory_page.ir_al_carrito()
    assert cart_page.esta_en_pagina_carrito()
    
    # 3. Iniciar Checkout
    checkout_page = cart_page.clic_checkout()
    
    # 4. Llenar formulario de envío
    checkout_page.completar_formulario("German", "Pappalardo", "1234")
    
    # 5. Finalizar Compra (Click en Finish)
    checkout_page.finalizar_compra()
    
    # 6. Validar mensaje de éxito
    mensaje_exito = checkout_page.obtener_mensaje_final()
    
    print(f"\n[Info] Mensaje final obtenido: {mensaje_exito}")
    
    assert mensaje_exito == "Thank you for your order!", "El mensaje de éxito no es correcto"