# Manual Frontend - Alta de Usuarios (Vue.js)

Este manual explica, paso a paso, el frontend que ya programamos para el alta de usuarios.
Esta escrito para estudiantes que estan haciendo su primer proyecto fullstack.

## 1) Objetivo del modulo

Construir una pantalla de registro con estos campos:

- email
- password
- repeatPassword

Reglas clave:

- validar en frontend antes de llamar al backend
- mostrar errores por campo
- enviar datos al endpoint `POST /api/users/register/`
- mostrar mensaje de exito si el usuario se crea
- mantener codigo modular y escalable

## 2) Arquitectura elegida (modular)

En vez de poner toda la logica en un solo `.vue`, se separo por responsabilidades.

```text
frontend/src/
  config/
    api.js                              # URL base del backend
  modules/users/
    pages/
      UserRegistrationPage.vue          # Contenedor de la feature
    components/
      UserRegistrationForm.vue          # Componente visual/presentacional
    composables/
      useUserRegistration.js            # Estado + caso de uso del registro
    services/
      userService.js                    # Llamadas HTTP
    validators/
      userRegistrationValidator.js      # Reglas de validacion del formulario
```

Idea mental:

- `component`: "como se ve"
- `composable`: "como se comporta"
- `service`: "como habla con la API"
- `validator`: "que reglas de negocio local aplica"

## 3) Punto de entrada de la app

Archivo: `src/main.js`

Que hace:

1. crea la aplicacion Vue
2. carga `App.vue`
3. monta la app en `#app`

```js
createApp(App).mount("#app");
```

## 4) App principal

Archivo: `src/App.vue`

Que hace:

- Renderiza la pagina de alta:

```vue
<UserRegistrationPage />
```

No tiene logica de negocio. Solo compone la pantalla.

## 5) Configuracion de API

Archivo: `src/config/api.js`

```js
export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";
```

Por que esta separado:

- si cambia backend (dev/staging/prod), no hay que tocar todos los servicios
- evita "hardcodear" URLs en muchos archivos

## 6) Validador del formulario

Archivo: `src/modules/users/validators/userRegistrationValidator.js`

Responsabilidad:

- recibir objeto `form`
- devolver objeto `errors`

Reglas implementadas:

1. email obligatorio
2. email con formato valido (regex)
3. password obligatoria
4. password minimo 8 caracteres
5. repeatPassword obligatorio
6. password y repeatPassword deben coincidir

Contrato del validador:

- si todo esta bien: devuelve `{}`
- si hay errores: devuelve algo como:

```js
{
  email: "El e-mail es obligatorio.",
  repeatPassword: "Las contrasenas deben ser iguales."
}
```

## 7) Service HTTP

Archivo: `src/modules/users/services/userService.js`

Funcion principal:

```js
registerUser(payload)
```

Flujo:

1. hace `fetch` a `POST /api/users/register/`
2. envia JSON
3. si `response.ok === false`, lanza error con `error.errors`
4. si todo va bien, retorna `body.data`

Por que es importante:

- el componente/composable no conoce detalles de `fetch`
- si luego cambias a Axios, solo cambias esta capa

## 8) Composable del caso de uso

Archivo: `src/modules/users/composables/useUserRegistration.js`

Este es el cerebro del modulo.

Estado:

- `form` (email, password, repeatPassword)
- `errors`
- `isSubmitting`
- `successMessage`
- `serverError`

Funciones:

1. `updateField({ field, value })`
- actualiza campo en `form`
- limpia error de ese campo si existia

2. `submit()`
- limpia mensajes globales
- ejecuta validacion frontend
- si hay errores, corta flujo
- si no hay errores, llama a `registerUser(...)`
- en exito: muestra mensaje y limpia formulario
- en error backend: mapea errores del backend a nombres del frontend

3. `mapBackendErrors(backendErrors)`
- convierte `repeat_password` (backend) en `repeatPassword` (frontend)
- esto evita acoplar UI al formato interno de la API

## 9) Componente presentacional

Archivo: `src/modules/users/components/UserRegistrationForm.vue`

Regla de oro:

- este componente recibe estado por `props`
- emite eventos para acciones del usuario
- no maneja logica de negocio compleja

Props:

- `form`
- `errors`
- `isSubmitting`
- `serverError`
- `successMessage`

Eventos:

- `update-field`
- `submit`

Ejemplo de flujo de un input:

1. usuario escribe email
2. input dispara `@input`
3. se ejecuta `onInput("email", $event)`
4. componente emite `update-field`
5. el composable actualiza estado

## 10) Pagina contenedora

Archivo: `src/modules/users/pages/UserRegistrationPage.vue`

Esta pagina conecta capa visual con capa de logica:

1. importa `useUserRegistration()`
2. obtiene estado y funciones
3. pasa todo al formulario via props y eventos

Es el "pegamento" entre UI y caso de uso.

## 11) Flujo completo de datos (de punta a punta)

1. Usuario completa formulario
2. `UserRegistrationForm` emite `submit`
3. `UserRegistrationPage` llama `submit` del composable
4. Composable valida con `validateUserRegistrationForm`
5. Si pasa validacion: llama a `registerUser` (service)
6. Service pega al backend
7. Backend responde:
- exito: mostrar `successMessage`
- error de validacion: mapear y mostrar por campo

## 12) Por que este enfoque es "mundo real"

Si mañana agregas login, listado y edicion:

- reutilizas patron (page + component + composable + service + validator)
- cada capa cambia por separado
- testear es mas facil
- onboarding de nuevos devs es mas rapido

Si todo estuviera en un solo archivo `.vue`, cada cambio seria mas riesgoso.

## 13) Guion recomendado para explicarlo en clase (live coding)

1. Crear primero `validator` (reglas claras).
2. Crear `service` (contrato con backend).
3. Crear `composable` (estado + submit).
4. Crear `component` visual (inputs, errores, boton).
5. Crear `page` que conecta todo.
6. Integrar en `App.vue`.
7. Probar casos:
- exito
- passwords distintas
- email invalido
- email duplicado

## 14) Mini ejercicios para estudiantes

1. Agregar regla: password debe tener al menos 1 numero.
2. Agregar campo `name` y validarlo.
3. Deshabilitar boton si hay campos vacios.
4. Mostrar contador de caracteres de password.
5. Agregar spinner visual durante `isSubmitting`.

## 15) Resumen corto

El frontend del alta no solo "funciona":

- esta separado por capas
- tiene validacion local
- maneja errores de backend correctamente
- esta listo para crecer a un ABM completo sin rehacer todo
