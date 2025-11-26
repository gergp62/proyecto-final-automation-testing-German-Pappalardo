# services/reqres_service.py
import requests

class ReqResService:
    BASE_URL = "https://reqres.in/api"
    
    # Definición de los headers con la clave de la API
    HEADERS = {
        'x-api-key': 'reqres-free-v1',
        'Content-Type': 'application/json' 
    }

    def get_users(self, page=2):
        """Obtiene la lista de usuarios paginada (GET)."""
        endpoint = f"{self.BASE_URL}/users"
        params = {"page": page}
        # Incluir headers
        response = requests.get(endpoint, params=params, headers=self.HEADERS)
        return response

    def create_user(self, name, job):
        """Crea un nuevo usuario (POST)."""
        endpoint = f"{self.BASE_URL}/users"
        payload = {
            "name": name,
            "job": job
        }
        # Incluir headers
        response = requests.post(endpoint, json=payload, headers=self.HEADERS)
        return response

    def delete_user(self, user_id):
        """Elimina un usuario por ID (DELETE)."""
        endpoint = f"{self.BASE_URL}/users/{user_id}"
        # Incluir headers
        response = requests.delete(endpoint, headers=self.HEADERS)
        return response

    def register_user(self, email, password=None):
        """Intenta registrar un usuario (POST)."""
        endpoint = f"{self.BASE_URL}/register"
        payload = {"email": email}
        if password:
            payload["password"] = password
            
        # Incluir headers
        response = requests.post(endpoint, json=payload, headers=self.HEADERS)
        return response