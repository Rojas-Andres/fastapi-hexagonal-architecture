# Proyecto de Arquitectura Hexagonal con FastAPI

Este proyecto implementa una arquitectura hexagonal utilizando FastAPI para manejar la lógica de negocio y las interacciones con la infraestructura. A continuación se detalla cómo está estructurado el proyecto y la función de cada componente.

## Arquitectura Hexagonal

La arquitectura hexagonal, también conocida como arquitectura de puertos y adaptadores, busca separar la lógica de negocio de los detalles de implementación tecnológica, como bases de datos y APIs externas. Esto permite que la lógica de negocio sea independiente de las tecnologías específicas, facilitando su mantenimiento y evolución.

### Componentes Principales

#### 1. Dominio (Domain)

El dominio representa el núcleo de la aplicación y contiene la lógica de negocio pura. Incluye entidades, casos de uso, y puertos. En este proyecto, el dominio está dividido en dos módulos principales: `users` y `auth`.

- **Entidades (Entities)**: Representan los objetos de negocio. Por ejemplo, `User` en `users/models.py`.
- **Casos de Uso (Use Cases)**: Representan las operaciones del negocio. Por ejemplo, `UserService` en `users/services.py`.
- **Puertos (Ports)**: Definen las interfaces que deben implementar los adaptadores para interactuar con el dominio. Por ejemplo, `UserRepository` en `users/ports/repository.py`.

#### 2. Aplicación (Application)

La capa de aplicación contiene la lógica que coordina las interacciones entre el dominio y la infraestructura. En este proyecto, se incluye en los servicios dentro de los módulos `users` y `auth`.

- **Servicios (Services)**: Orquestan las operaciones del dominio y las interacciones con los adaptadores. Por ejemplo, `AuthService` en `auth/services.py`.

#### 3. Infraestructura (Infrastructure)

La infraestructura contiene los detalles de implementación tecnológica. En este proyecto, incluye adaptadores para bases de datos y APIs.

- **Adaptadores de Base de Datos (Database Adapters)**: Implementan los puertos definidos en el dominio para interactuar con la base de datos. Por ejemplo, `SQLAlchemyUserRepository` en `database/repository/user_repository.py`.
- **Adaptadores de API (API Adapters)**: Exponen la funcionalidad de la aplicación a través de endpoints HTTP. Por ejemplo, los endpoints definidos en `api/v1/endpoints/`.

### Estructura del Proyecto

```plaintext
my_hexagonal_app/
├── alembic/                   # Directorio de migraciones de Alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       └── <migration_files>.py
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada de FastAPI
│   ├── core/                  # Núcleo de la aplicación
│   │   ├── __init__.py
│   │   ├── users/             # Módulo de usuarios
│   │   │   ├── __init__.py
│   │   │   ├── models.py      # Entidades de negocio
│   │   │   ├── services.py    # Casos de uso
│   │   │   └── ports/         # Puertos
│   │   │       ├── __init__.py
│   │   │       └── repository.py
│   │   ├── auth/              # Módulo de autenticación
│   │   │   ├── __init__.py
│   │   │   ├── models.py      # Entidades de negocio
│   │   │   ├── services.py    # Casos de uso
│   │   │   ├── schemas.py     # Esquemas de datos
│   │   │   └── ports/         # Puertos
│   │   │       └── repository.py
│   ├── adapters/              # Adaptadores de infraestructura
│   │   ├── __init__.py
│   │   ├── database/          # Adaptadores de base de datos
│   │   │   ├── __init__.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   └── user_models.py
│   │   │   ├── repository/
│   │   │       ├── __init__.py
│   │   │       ├── user_repository.py
│   │   ├── api/               # Adaptadores de API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   └── auth.py
│   │   │   └── dependencies.py
│   ├── email/                 # Adaptadores de servicios externos
│   │   ├── __init__.py
│   │   └── notification.py
└── README.md
``` 

## Descripción de Archivos y Directorios
### Alembic
- alembic/env.py: Configuración de Alembic para manejar las migraciones de la base de datos.

### Core
- users/models.py: Define la entidad User.
- users/services.py: Define UserService, que contiene la lógica de negocio para usuarios.
- users/ports/repository.py: Define UserRepository, la interfaz para los adaptadores de repositorio de usuarios.
- auth/models.py: Define las entidades relacionadas con la autenticación, como Token.
- auth/services.py: Define AuthService, que contiene la lógica de negocio para la autenticación.
- auth/schemas.py: Define los esquemas de datos para las solicitudes y respuestas de autenticación.

### Adapters
- database/models/user_models.py: Define el modelo de base de datos para User.
- database/repository/user_repository.py: Implementa UserRepository utilizando SQLAlchemy.
- api/v1/endpoints/auth.py: Define los endpoints de autenticación.
- api/v1/endpoints/users.py: Define los endpoints para la gestión de usuarios.
- email/notification.py: Implementa el servicio de notificaciones por correo electrónico.

## Correr el proyecto local
- Instalar virtualenv
    - virtualenv venv
- Activar el entorno virtual
- Instalar requirements local
    - pip install -r requirements_local.txt
- Ejecutar migraciones
    - alembic upgrade heads
- correr proyecto local
    - uvicorn app.main:app --reload --port 8000
- Correr el proyecto en modo debug
    - Tener instalado python en vscode y ejecutarlo con F5 esto ayudara a ejecutar el codigo en modo debug
#### En models de adaptadores de la base de datos cree 3 modelos para validar que los entendiera alembic