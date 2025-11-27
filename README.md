# 🚀 Proyecto de Automatización Híbrida (UI & API) con Pytest

Este proyecto implementa un *framework* de automatización de pruebas **híbrido** (Interfaz de Usuario y API) utilizando **Python** y **Pytest**. El objetivo es validar la funcionalidad crítica de la aplicación web **SauceDemo** (UI) y probar un *mock* de servicio API externo (**ReqRes**).

## 💡 Propósito y Características Destacadas

El framework está diseñado para demostrar las mejores prácticas en automatización, cubriendo un ecosistema completo de pruebas:

*   **Arquitectura POM (Page Object Model):** Código modular y reutilizable para las pruebas de UI (SauceDemo).
*   **Service Object Pattern:** Lógica separada y clara para las pruebas de API.
*   **Data Driven Testing (DDT):** Las pruebas de Login y Catálogo utilizan datos externos cargados desde archivos **CSV** y **JSON**.
*   **Flujos E2E y Encadenamiento:** Cobertura de flujos completos de compra (UI) y flujos encadenados de creación/eliminación de recursos (API).
*   **Reporting Profesional:** Generación de reportes detallados en HTML con **capturas de pantalla automáticas** en caso de fallo.
*   **Logging:** Sistema de registro detallado (`execution.log`) para facilitar la depuración de los pasos de ejecución.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Rol |
| :--- | :--- |
| **Python 3.12+** | Lenguaje de programación principal. |
| **Pytest** | Marco de pruebas (framework) principal para la ejecución y gestión de fixtures. |
| **Selenium** | Automatización de la Interfaz de Usuario (UI). |
| **Requests** | Manejo de peticiones HTTP (pruebas de API). |
| **Pytest-HTML** | Plugin para la generación de reportes avanzados. |
| **WebDriver Manager** | Gestión automática del *driver* del navegador (Chrome). |

---

## 📂 Estructura del Proyecto

La estructura sigue el patrón de separación de responsabilidades:

```text
proyecto-final-automation-testing
├── data/                    # Archivos de datos externos (DDT)
│   ├── inventory.json       # Datos de productos para el Catálogo.
│   └── users.csv            # Usuarios y contraseñas para Login.
├── pages/                   # Módulos del Page Object Model (UI)
│   ├── login_page.py        # Page Object para Login.
│   ├── inventory_page.py    # Page Object para Inventario.
│   └── ...                  # (Otros Page Objects)
├── services/                # Módulos del Service Object Pattern (API)
│   └── reqres_service.py    # Lógica de la API ReqRes.
├── Tests/                   # Archivos de Tests
│   ├── test_api_reqres.py   # Tests del backend.
│   ├── test_login.py        # Tests de login (incluye DDT).
│   └── ...                  # (Otros tests de UI)
├── utils/                   # Utilidades del Framework
│   └── data_loader.py       # Lógica para leer CSV/JSON.
├── conftest.py              # Configuraciones globales (Fixtures, Hooks, Logging).
├── screenshots/             # Carpeta de salida para capturas de fallo.
├── execution.log            # Archivo de registro generado.
├── requirements.txt         # Lista de dependencias del proyecto.
└── README.md                # Este documento.
```

---

## ⚙️ ¿Cómo Instalar las Dependencias?

Asegúrate de tener **Python 3.12** o superior instalado. Luego, usa `pip` para instalar todas las librerías necesarias ejecutando el siguiente comando en la raíz del proyecto:

```bash
pip install -r requirements.txt
```

---

## ▶️ ¿Cómo Ejecutar las Pruebas?

Las pruebas se ejecutan utilizando el comando `pytest` con marcadores (`-m`) para seleccionar los flujos deseados.

### 1. Ejecución Completa con Reporte y Logging (Recomendado)

Este comando ejecuta todos los tests de UI y API, genera el reporte HTML e inicia el sistema de logging:

```bash
pytest -v --html=reporte_final_ejecucion.html --self-contained-html
```

### 2. Ejecución Selectiva por Marcador

Puedes ejecutar grupos específicos de pruebas utilizando los marcadores definidos en `pytest.ini`:

| Comando | Descripción |
| :--- | :--- |
| `pytest -m api -v` | Ejecuta solo las pruebas de la API (backend). |
| `pytest -m login -v` | Ejecuta solo las pruebas de Login (incluyendo DDT). |
| `pytest -m smoke -v` | Ejecuta solo el conjunto de pruebas críticas. |
| `pytest -m regression -v` | Ejecuta todas las pruebas de regresión. |

---

## 📊 ¿Cómo Interpretar los Reportes Generados?

### Reporte HTML (`reporte_final_ejecucion.html`)
Este archivo se genera en la raíz del proyecto tras la ejecución.
*   **Estado:** Muestra claramente el resultado de cada prueba (`PASSED`, `FAILED`, `ERROR`).
*   **Evidencia:** Si una prueba de UI falla, la **captura de pantalla** se adjunta directamente en la sección "Extra" del reporte HTML, además de guardarse en la carpeta `screenshots/`.
*   **Tiempos:** Indica la duración de cada test y la duración total de la ejecución.

### Archivo de Logging (`execution.log`)
Este archivo contiene el historial detallado de la ejecución.
*   **Formato:** Muestra la fecha, el nivel (`INFO`, `WARNING`, `ERROR`), el módulo y el mensaje.
*   **Uso en Depuración:** Si una prueba falla, revisa el `execution.log` para ver el último paso exitoso registrado por el Page Object o la fixture antes del error.