# ABM Usuarios (Django + Vue)

Mini proyecto fullstack con arquitectura por capas para alta de usuarios.

## Estructura

```text
backend/
  config/                                # Configuracion Django + middleware
  apps/users/
    models.py                            # Modelo User (email como identificador)
    domain/                              # Reglas de dominio + interfaces
    application/                         # DTOs, errores y servicios
    infrastructure/repositories/         # Implementacion concreta con ORM
    presentation/controllers/            # Controladores HTTP
frontend/
  src/modules/users/
    components/                          # UI desacoplada
    composables/                         # Estado + casos de uso del modulo
    services/                            # Integracion HTTP
    validators/                          # Validacion de formulario
```

## Backend (Django)

1. Crear entorno virtual e instalar dependencias:

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

2. Crear migraciones y aplicar:

```bash
python manage.py makemigrations users
python manage.py migrate
```

3. Ejecutar servidor:

```bash
python manage.py runserver
```

API disponible:
- `POST /api/users/register/`

Payload:

```json
{
  "email": "usuario@correo.com",
  "password": "Password123!",
  "repeat_password": "Password123!"
}
```

## Frontend (Vue + Vite)

1. Instalar dependencias:

```bash
cd frontend
npm install
```

2. Configurar URL del backend (opcional):

```bash
copy .env.example .env
```

3. Levantar frontend:

```bash
npm run dev
```

## Decisiones de arquitectura

- Controller: capa HTTP (request/response, status codes).
- Service: orquesta caso de uso de registro.
- Repository: abstrae persistencia para testear y reemplazar implementacion.
- Validator de dominio: reglas de email/password centralizadas.
- Vue modular: componente presentacional + composable + service + validator.

