# 02 - Manual Backend (Alta de Usuarios)

Manual para explicar en clase todo el backend que programamos en Django.

## 1. Objetivo del backend

Implementar el alta de usuarios con buenas practicas de arquitectura:

- endpoint de registro
- validaciones de negocio
- persistencia en base de datos
- codigo desacoplado y mantenible

Campos del alta:

- `email`
- `password`
- `repeat_password`

Reglas:

- email obligatorio y con formato valido
- password obligatoria y valida segun Django
- `password` y `repeat_password` deben coincidir
- email no debe estar repetido

## 2. Arquitectura aplicada

Usamos una separacion por capas dentro de `apps/users`:

- `presentation`: capa HTTP (controllers)
- `application`: caso de uso (services, dto, exceptions)
- `domain`: contratos y reglas de dominio (repositories, validators)
- `infrastructure`: implementacion concreta (ORM de Django)

Estructura:

```text
backend/
  config/
    settings.py
    urls.py
    middleware/cors.py
  apps/users/
    models.py
    urls.py
    presentation/controllers/user_registration_controller.py
    application/services/user_registration_service.py
    application/dto/user_registration_dto.py
    application/exceptions.py
    domain/repositories/user_repository.py
    domain/validators/user_registration_validator.py
    infrastructure/repositories/django_user_repository.py
    migrations/0001_initial.py
```

## 3. Configuracion global del backend

Archivo: `backend/config/settings.py`

Puntos importantes:

- `INSTALLED_APPS` incluye `apps.users.apps.UsersConfig`
- `AUTH_USER_MODEL = "users.User"` para usar un modelo custom
- `AUTH_PASSWORD_VALIDATORS` habilita validadores de password de Django
- `CORS_ALLOWED_ORIGINS` permite el frontend local (`localhost:5173`)

Archivo: `backend/config/urls.py`

- ruta admin: `/admin/`
- rutas users: `/api/users/`

Archivo: `backend/config/middleware/cors.py`

- middleware simple para manejar CORS
- responde `OPTIONS` con `204`
- agrega headers CORS cuando el origen esta permitido

## 4. Modelo de usuario

Archivo: `backend/apps/users/models.py`

Se definio un modelo `User` custom:

- hereda de [`AbstractBaseUser`](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser) y [`PermissionsMixin`](https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin)
- usa `email` como identificador principal (`USERNAME_FIELD = "email"`)
- campos: `email`, `is_staff`, `is_active`, `date_joined`

Manager custom `UserManager`:

- normaliza email
- hashea password con `set_password`
- provee `create_user` y `create_superuser`

Resultado:

- autenticacion basada en email
- estructura de usuario lista para evolucionar en un ABM real

## 5. Dominio: contratos y validaciones

### 5.1 Interface del repositorio

Archivo: `domain/repositories/user_repository.py`

Contrato abstracto:

- `exists_by_email(email) -> bool`
- `create(email, password) -> Any`

El service depende de esta interface, no del ORM directo.

### 5.2 Validadores de dominio

Archivo: `domain/validators/user_registration_validator.py`

Funciones:

- `validate_email_value(email)`
- `validate_password_value(password)`

Validaciones implementadas:

- email requerido + formato valido
- password requerida + reglas de password de Django

## 6. Application: caso de uso de registro

### 6.1 DTO de entrada

Archivo: `application/dto/user_registration_dto.py`

`UserRegistrationDTO` encapsula:

- `email`
- `password`
- `repeat_password`

Metodo `from_dict(payload)`:

- parsea y normaliza entrada
- evita errores por campos faltantes

### 6.2 Excepcion de validacion

Archivo: `application/exceptions.py`

`DomainValidationError` contiene errores por campo, por ejemplo:

```python
{"email": "Email is already in use."}
```

### 6.3 Service principal

Archivo: `application/services/user_registration_service.py`

Metodo: `register(dto)`

Flujo:

1. valida email
2. valida password
3. verifica igualdad de passwords
4. verifica email duplicado
5. si hay errores -> lanza `DomainValidationError`
6. si todo esta bien -> crea usuario via repository
7. devuelve `{"id": ..., "email": ...}`

Este archivo concentra la logica de negocio del alta.

## 7. Infrastructure: repositorio concreto

Archivo: `infrastructure/repositories/django_user_repository.py`

Implementa la interface `UserRepository` con Django ORM:

- `exists_by_email`: usa `email__iexact`
- `create`: usa `create_user(...)` del modelo

Ventaja:

- si cambia la persistencia, se modifica esta capa y no todo el sistema

## 8. Presentation: controller y endpoint

Archivo: `apps/users/urls.py`

- define endpoint `POST /api/users/register/`

Archivo: `presentation/controllers/user_registration_controller.py`

Responsabilidades:

- parsear JSON del request
- construir DTO
- llamar al service
- devolver respuesta HTTP

Respuestas:

- `201` exito:

```json
{
  "success": true,
  "data": { "id": 1, "email": "usuario@correo.com" }
}
```

- `400` JSON invalido:

```json
{
  "success": false,
  "message": "Invalid JSON payload."
}
```

- `400` error de negocio:

```json
{
  "success": false,
  "errors": {
    "repeat_password": "Passwords do not match."
  }
}
```

## 9. Endpoint documentado

Metodo y ruta:

- `POST /api/users/register/`

Request body:

```json
{
  "email": "usuario@correo.com",
  "password": "Password123!",
  "repeat_password": "Password123!"
}
```

Errores comunes:

- email invalido
- password debil
- passwords distintas
- email ya registrado

## 10. Flujo completo de punta a punta

1. Frontend envia `POST /api/users/register/`.
2. Controller parsea JSON.
3. Controller crea DTO.
4. Service ejecuta validaciones de dominio.
5. Service consulta si el email ya existe.
6. Service crea usuario con repository si todo esta correcto.
7. Controller responde `201` o `400`.

## 11. Migraciones y base de datos

Archivo: `apps/users/migrations/0001_initial.py`

Crea la tabla inicial de usuarios con:

- campos del modelo `User`
- relaciones de permisos y grupos

Comandos:

```powershell
cd backend
python manage.py makemigrations users
python manage.py migrate
```

## 12. Como explicarlo en una clase (orden sugerido)

1. Modelo `User` custom y manager.
2. Interface `UserRepository`.
3. Implementacion `DjangoUserRepository`.
4. Validator de dominio.
5. DTO y excepcion.
6. Service de registro.
7. Controller HTTP.
8. URL del endpoint.
9. Pruebas de casos felices y casos de error.

## 13. Ejercicios para estudiantes

1. Agregar campo `full_name` al registro.
2. Crear endpoint `GET /api/users/` para listado.
3. Crear endpoint de edicion de usuario.
4. Crear endpoint de baja logica (`is_active = False`).
5. Agregar tests unitarios del `UserRegistrationService`.

## 14. Resumen

El backend no esta armado solo para "que funcione". Esta preparado para crecer:

- capas separadas
- reglas de negocio centralizadas
- endpoint claro y consistente
- base solida para completar el ABM de usuarios
