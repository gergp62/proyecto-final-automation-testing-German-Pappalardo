import csv
import json
import os
from pathlib import Path

# Definimos la ruta base al directorio 'data' de forma dinámica
# Esto funciona sin importar en qué PC se corre el test
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"

def get_csv_data(filename):
    """
    Lee un archivo CSV y retorna una lista de diccionarios.
    """
    csv_path = DATA_DIR / filename
    data_list = []
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_list.append(row)
    return data_list

def get_json_data(filename):
    """
    Lee un archivo JSON y retorna la estructura de datos (lista o dict).
    """
    json_path = DATA_DIR / filename
    with open(json_path, mode='r', encoding='utf-8') as file:
        return json.load(file)