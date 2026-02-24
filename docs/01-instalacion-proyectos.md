# 01 - Instalacion de Proyectos

Guia paso a paso para levantar el proyecto fullstack (Django + Vue).

## 1. Requisitos previos

Instalar una sola vez:

- Python 3.10 o superior
- Node.js 18 o superior (incluye `npm`)

Verificar versiones:

```powershell
python --version
node --version
npm --version
```

## 2. Abrir el proyecto

En una terminal, ir a la carpeta raiz:

```powershell
cd abm-usuarios-vivo
```

## 3. Backend (Django)

Entrar a backend:

```powershell
cd backend
```

Crear entorno virtual:

```powershell
python -m venv .venv
```

Activar entorno virtual:

```powershell
.venv\Scripts\activate
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

Crear y aplicar migraciones:

```powershell
python manage.py makemigrations users
python manage.py migrate
```

Levantar backend:

```powershell
python manage.py runserver
```

Backend disponible en:

- `http://127.0.0.1:8000`

## 4. Frontend (Vue)

Abrir una segunda terminal y ejecutar:

```powershell
cd c:\Users\m_cas\Documents\__Bootcamps\abm-usuarios-vivo\frontend
npm install
copy .env.example .env
npm run dev
```

Frontend disponible en:

- `http://localhost:5173`

## 5. Prueba funcional del alta

1. Abrir `http://localhost:5173`.
2. Completar:
   - e-mail
   - contrasena
   - repetir contrasena
3. Probar casos:
   - contrasenas distintas -> debe mostrar error
   - e-mail invalido -> debe mostrar error
   - datos correctos -> debe registrar usuario

## 6. Checklist rapido

- Backend corriendo en `8000`
- Frontend corriendo en `5173`
- Migraciones ejecutadas
- Entorno virtual activo en la terminal de backend

## 7. Errores comunes y solucion

- `python` no reconocido:
  - reinstalar Python y marcar `Add Python to PATH`
- `npm` no reconocido:
  - reinstalar Node.js
- error de migraciones:
  - volver a ejecutar:
    ```powershell
    python manage.py makemigrations users
    python manage.py migrate
    ```
- frontend no conecta con backend:
  - revisar `frontend/.env`:
    ```env
    VITE_API_BASE_URL=http://127.0.0.1:8000
    ```
