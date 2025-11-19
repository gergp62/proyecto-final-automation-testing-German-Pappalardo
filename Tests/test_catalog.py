import pytest
from pages import InventoryPage

# Todos los tests en este archivo requieren un login previo
pytestmark = pytest.mark.usefixtures("usuario_logueado")

@pytest.mark.catalog
def test_verificar_elementos_ui_presentes(driver):
    """
    Verifica que elementos clave de la UI estén presentes.
    (Título, Menú y Filtros)

    """
    inventory_page = InventoryPage(driver)
    
    assert inventory_page.obtener_titulo_pagina() == "Products"
    assert inventory_page.es_boton_menu_visible(), "El botón de menú no es visible"
    assert inventory_page.es_filtro_visible(), "El filtro de productos no es visible"


@pytest.mark.smoke
@pytest.mark.catalog
def test_verificar_presencia_productos(driver):
    """
    Comprueba que existan productos visibles en la página.
    
    """
    inventory_page = InventoryPage(driver)
    assert inventory_page.obtener_cantidad_productos() > 0, "No se encontraron productos"

@pytest.mark.catalog
def test_obtener_info_primer_producto(driver):
    """
    Lista nombre/precio del primer producto.
    
    """
    inventory_page = InventoryPage(driver)
    info = inventory_page.obtener_info_primer_producto()
    
    print(f"\n[Info] Primer producto: {info['nombre']} | Precio: {info['precio']}")
    assert info["nombre"] == "Sauce Labs Backpack"
    assert info["precio"] == "$29.99"