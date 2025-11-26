import pytest
from services.reqres_service import ReqResService

# Instanciamos el servicio (podría ser una fixture, pero así es simple y claro)
api = ReqResService()

@pytest.mark.api
def test_get_list_users():
    """
    Caso 1 (GET): Verificar código de estado y estructura de la respuesta.
    """
    response = api.get_users(page=2)
    
    # 1. Validar código de estado
    assert response.status_code == 200, "El código de estado no es 200"
    
    # 2. Validar estructura JSON
    data = response.json()
    assert "page" in data
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0
    
    # Validar contenido específico del primer usuario
    first_user = data["data"][0]
    assert "email" in first_user
    assert "first_name" in first_user

@pytest.mark.api
def test_create_user_post():
    """
    Caso 2 (POST): Crear usuario y validar que la respuesta contiene los datos enviados.
    """
    name_input = "German"
    job_input = "QA Automation"
    
    response = api.create_user(name_input, job_input)
    
    # Validar creación exitosa (201 Created)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == name_input
    assert data["job"] == job_input
    assert "id" in data
    assert "createdAt" in data

@pytest.mark.api
def test_register_unsuccessful():
    """
    Caso 3 (Negativo): Intentar registrar usuario sin password.
    Valida manejo de errores (400 Bad Request).
    """
    email = "sydney@fife"
    # No enviamos password para provocar el error
    response = api.register_user(email)
    
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"

@pytest.mark.api
def test_flujo_encadenado_crear_y_borrar():
    """
    Caso 4 (Encadenamiento): Crear un recurso y luego borrarlo usando su ID.
    Flujo: POST -> Extraer ID -> DELETE
    """
    # Paso 1: Crear usuario
    print("\n[Paso 1] Creando usuario...")
    response_create = api.create_user("TestUser", "Tester")
    assert response_create.status_code == 201
    
    # Paso 2: Extraer el ID de la respuesta del paso 1
    user_id = response_create.json()["id"]
    print(f"[Paso 2] Usuario creado con ID: {user_id}")
    assert user_id is not None
    
    # Paso 3: Usar ese ID para borrar el usuario
    print(f"[Paso 3] Borrando usuario {user_id}...")
    response_delete = api.delete_user(user_id)
    
    # Paso 4: Validar borrado (204 No Content)
    assert response_delete.status_code == 204