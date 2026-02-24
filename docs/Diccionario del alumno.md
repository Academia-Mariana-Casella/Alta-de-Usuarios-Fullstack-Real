# Diccionario del alumno

Glosario rapido de terminos tecnicos usados en este proyecto Fullstack.

## Backend (Django)

- `AbstractBaseUser`: Clase base de Django para autenticacion. Incluye `password`, `last_login` y metodos como `set_password` y `check_password`.
- `PermissionsMixin`: Mixin de Django que agrega permisos, grupos y `is_superuser`.
- `AUTH_USER_MODEL`: Setting para indicar que modelo de usuario usa Django en el proyecto.
- `Serializer`: Componente de DRF para validar/transformar datos de entrada y salida.
- `View` o `Controller`: Capa que recibe la request HTTP y devuelve la response.
- `Service`: Capa de aplicacion donde vive la logica de negocio.
- `Repository`: Abstraccion para acceder a la persistencia (DB) sin acoplar la logica al ORM.
- `DTO (Data Transfer Object)`: Objeto para transportar datos entre capas.
- `Migration`: Archivo que versiona cambios de esquema de base de datos.
- `CORS`: Politica del navegador para controlar que origenes pueden consumir la API.

## Frontend (Vue)

- `Componente`: Bloque reutilizable de UI (template + logica + estilos).
- `Composable`: Funcion reutilizable de Vue para encapsular logica reactiva (ej: `useUserRegistration`).
- `Props`: Datos que un componente padre envia a un componente hijo.
- `Emit`: Evento que un componente hijo envia al padre.
- `State`: Estado interno/reactivo que controla la interfaz.
- `Binding`: Enlace entre estado y vista (ej: `v-model`).

## API y arquitectura

- `Endpoint`: URL de la API que expone una accion o recurso.
- `Request`: Peticion HTTP que envia el cliente al servidor.
- `Response`: Respuesta HTTP que devuelve el servidor.
- `Validacion`: Reglas para asegurar que los datos son correctos antes de procesarlos.
- `Error de negocio`: Error por incumplir reglas del dominio (ej: email repetido).
- `Desacoplamiento`: Separar responsabilidades para facilitar mantenimiento y testeo.

