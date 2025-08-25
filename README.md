# Proyecto Multi-Tenant
Sistema web desarrollado con Django que implementa un modelo multi-tenant, permitiendo la gestión de múltiples clientes (tenants) dentro de una misma aplicación. Cada tenant mantiene su propia separación lógica de datos, con autenticación de usuarios, manejo de clientes y administración de productos.

## 🎯 Product Backlog
Desarrollar un sistema que permita:
 - Registrar y autenticar usuarios con control multi-tenant.
 - Administrar clientes (tenants) y asignarles usuarios/productos.
 - Gestionar productos con operaciones CRUD (crear, listar, actualizar y eliminar).
 - Asegurar separación de datos por cliente (aislamiento lógico).
 - Mantener la integridad de datos en una base centralizada.
 - Proporcionar una interfaz clara y usable.
 - Desplegar y validar avances en GitHub asegurando correcto funcionamiento.

## 🎯 Sprint Goal
El objetivo del sprint es implementar un sistema multi-tenant con Django, permitiendo manejar varios clientes con independencia de datos, autenticación de usuarios, gestión de productos y panel de administración básico.

## 👥 Roles Scrum
| Rol            | Integrante           | Función principal                                                                                                                         |
|----------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | Matias Sicha    | Facilita el marco de trabajo Scrum, asegura la correcta aplicación de la metodología ágil y elimina impedimentos.      |
| Product Owner  | Rodrigo Guerra      | Define los requisitos del sistema, prioriza el backlog y valida que el inventario y la agenda cumplan con los objetivos del proyecto.      |
| Developer 2    | Daniel Torres      | Desarrolla la interfaz de usuario en HTML y CSS, asegurando un diseño claro y usable para la gestión de inventario y agenda.   |
| Developer 3    | Juan Solis    | Implementa la lógica de autenticación y manejo de cuentas en Django. |
| Developer 4    | Josue Castillo  | Desarrolla la lógica de tenants y aislamiento de datos.     |
| Developer 5    | Kevin Yupanqui  | Diseña y gestiona la base de datos en SQLite, adaptando la estructura de tablas y asegurando integridad de datos. |

## 🎯 Características Principales
### ✅ **Funcionalidades CRUD**
 - Crear, listar, editar y eliminar productos.
 - Registrar y administrar clientes (tenants).
 - Autenticación de usuarios asociada a tenants.

### ✅ **Interfaz de Usuario**
 - Formularios claros con validación automática.
 - Listados organizados en tablas.
 - Plantillas HTML reutilizables para coherencia visual.

### ✅ **Características Técnicas**
 - Backend: Django 4.x
 - Base de datos: SQLite (configuración por defecto, adaptable a MySQL/PostgreSQL).
 - Frontend: HTML + CSS personalizados.
 - Arquitectura modular: apps independientes (accounts, clients, products, tenants).

## 🏗️ Estructura del Proyecto

```
multi_tenant_demo/
├── accounts/               # App para autenticación de usuarios
├── clients/                # Gestión de clientes (tenants)
├── products/               # Módulo de productos
├── tenants/                # Lógica multi-tenant
├── inventory_project/       # Configuración principal del proyecto Django
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # Rutas principales
│   └── wsgi.py / asgi.py
├── manage.py                # Script de gestión Django
├── db.sqlite3               # Base de datos SQLite (desarrollo)
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación
```
## 🔗 Enlace del Trello
 - https://trello.com/b/gHvb7XjJ/crum-multi-tennacy

## 🎥 Video explicativo (entregado por Drive):
- Nombre de la carpeta:
- Contenido:
  - 🎥 Video
  - 📄 Documentacion
  - 🔗 Link del Drive: https

## 🚀 Instalación y Configuración

### 1. **Clonar el repositorio**
```bash
git clone <URL_DEL_REPOSITORIO>
cd multi_tenant_demo
```

### 2. **Crear entorno virtual**
```bash
python -m venv venv
```

### 3. **Activar entorno virtual**
```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 5. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Ejecutar el servidor**
```bash
python manage.py runserver
```
