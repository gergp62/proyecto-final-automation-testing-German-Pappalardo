# Proyecto de Automatización POM (Entrega Final) - Saucedemo

Este proyecto implementa una suite de pruebas automatizadas para [saucedemo.com](https://www.saucedemo.com/) utilizando el patrón **Page Object Model (POM)**.

## 🎯 Propósito del Proyecto

El objetivo es demostrar una estructura de automatización robusta, escalable y mantenible, cubriendo los flujos críticos de la aplicación:
* Login (válido e inválido)
* Navegación y verificación del Catálogo de Productos
* Flujo completo de "Añadir al Carrito"

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Framework de Pruebas:** Pytest
* **Automatización de Navegador:** Selenium WebDriver
* **Patrón de Diseño:** Page Object Model (POM)
* **Reportes:** `pytest-html`
* **Control de Versiones:** Git y GitHub

---

## ⚙️ Configuración e Instalación

### 1. Requisitos Previos
* Python 3.8+
* Google Chrome

### 2. Clonar el Repositorio
```bash
git clone https://github.com/gergp62/proyecto-final-automation-testing-German-Pappalardo
```

### 3. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de Pruebas

### Ejecutar Todos los Tests
```bash
pytest -v
```

### Generar Reporte HTML
Para ejecutar todos los tests y generar un reporte visual:
```bash
pytest -v -s --html=reporte.html --self-contained-html
```

### Ejecutar por Marcadores (Markers)
El proyecto usa marcadores de `pytest` para agrupar pruebas.

**Ejecutar solo los tests "smoke" (flujo crítico):**
```bash
pytest -m smoke -v
```

**Ejecutar solo los tests de "login":**
```bash
pytest -m login -v
```

**Marcadores disponibles:**
* `smoke`: Flujo principal (login, agregar al carrito).
* `regression`: (Añadir a más tests para una suite completa).
* `login`: Tests de la página de Login.
* `catalog`: Tests de la página de Inventario/Catálogo.
* `cart`: Tests de la página de Carrito.