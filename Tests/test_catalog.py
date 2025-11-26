import pytest
from pages import InventoryPage
from utils.data_loader import get_json_data


# Cargamos datos del JSON
productos_esperados = get_json_data("inventory.json")

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


@pytest.mark.catalog
def test_validar_datos_productos_json(driver):
    """
    Valida que los productos definidos en el JSON existan en la web
    con su precio correcto.
    """
    inventory_page = InventoryPage(driver)
    
    # Obtenemos info real del primer producto (esto se podría mejorar para buscar cualquiera)
    info_real = inventory_page.obtener_info_primer_producto()
    
    # Comparamos contra el primer producto de nuestro JSON
    producto_json = productos_esperados[0]
    
    print(f"\nValidando producto: {producto_json['name']}")
    
    assert info_real['nombre'] == producto_json['name']
    assert info_real['precio'] == producto_json['price']    