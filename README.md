# Proyecto Backend - Postulación SCESI

## Problemática

Actualmente el proceso de postulación a la Sociedad Científica de Estudiantes de Sistemas e Informática se gestiona mediante un grupo de WhatsApp: los postulantes deben llenar un formulario que se va difundiendo por diversos grupos de WhatsApp o sale en redes sociales, y se los agrega al grupo oficial de postulantes (con subgrupos por área). Ahí se comparten links de Google Meet y formularios de tareas/exámenes, y cuando alguien no pasa una etapa hay que buscarlo manualmente para eliminarlo del grupo. Es un proceso desordenado, poco profesional y poco eficiente: hay que buscar entre mensajes viejos para encontrar un link o una tarea, y unirse/salir de grupos constantemente.

## Cómo la resuelve

Este proyecto es el backend de un sistema que reemplaza ese flujo con una estructura ordenada y centralizada, dándole más formalidad al proceso. El proceso de selección de SCESI se divide en 4 etapas: Linux, Git-Github, Servidores y Proyecto-Final. Solo en la etapa de Proyecto-Final los postulantes se dividen por áreas (Backend, Web, IA, etc).

- User: postulantes, tutores y administradores. Cada usuario tiene un rol (admin, tutor, user), una etapa actual (stage_id) y una bandera sigue_postulando que indica si sigue en el proceso o fue eliminado.
- Stage: una de las 4 etapas fijas del proceso de selección. Puede tener varios tutores asignados.
- Area: área de postulación, solo aplicable dentro de la etapa Proyecto-Final. Puede tener varios tutores asignados.
- Session: espacio dentro de una etapa (y opcionalmente un área, si la etapa es Proyecto-Final) donde el tutor comparte un enlace o un aviso, reemplazando lo que antes se mandaba por WhatsApp.
- Submission: entrega de un postulante para una sesión específica (link a su repo, doc de una tarea, etc). Un usuario solo puede tener una submission por sesión.

## Instalación

1. Clonar el repositorio:
```
git clone <url-del-repo>
cd Proyecto-Backend
```
2. Instalar dependencias con uv:
```
uv sync
```
3. Crear el archivo .env en base a .env.example:
```
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432
DB_NAME=
ALLOWED_ORIGINS=["http://localhost:3000","http://localhost:8080","http://localhost"]
SECRET_KEY=
ALGORITHM=HS256
HOURS_SESSION=24
```
## Ejecución
```
uv run fastapi dev main.py
```
Las tablas se crean automáticamente al iniciar la aplicación (no se requieren migraciones manuales).

Documentación interactiva disponible en:
```
http://127.0.0.1:8000/docs
```
## Endpoints

### Health
- GET /health-check/ — verifica que la API está corriendo.

### User
- GET /user/ — lista todos los usuarios.
- POST /user/ — registra un nuevo usuario (queda como role=user por defecto).
- GET /user/{id} — obtiene un usuario por id.
- PATCH /user/{id} — actualiza datos de un usuario (rol, etapa, área, etc).
- DELETE /user/{id} — elimina un usuario.

### Stage
- GET /stage/ — lista todas las etapas.
- POST /stage/ — crea una nueva etapa.
- GET /stage/{id} — obtiene una etapa por id.
- PATCH /stage/{id} — actualiza una etapa.
- DELETE /stage/{id} — elimina una etapa.
- POST /stage/{stage_id}/tutors/{user_id} — asigna un tutor a una etapa.
- DELETE /stage/{stage_id}/tutors/{user_id} — quita un tutor de una etapa.

### Area
- GET /area/ — lista todas las áreas.
- POST /area/ — crea una nueva área.
- GET /area/{id} — obtiene un área por id.
- PATCH /area/{id} — actualiza un área.
- DELETE /area/{id} — elimina un área.
- POST /area/{area_id}/tutors/{user_id} — asigna un tutor a un área.
- DELETE /area/{area_id}/tutors/{user_id} — quita un tutor de un área.

### Session
- GET /session/ — lista todas las sesiones.
- POST /session/ — crea una sesión (asociada a una etapa, y opcionalmente a un área).
- GET /session/{id} — obtiene una sesión por id.
- PATCH /session/{id} — actualiza una sesión.
- DELETE /session/{id} — elimina una sesión.

### Submission
- GET /submission/ — lista todas las entregas.
- POST /submission/ — un postulante sube su entrega para una sesión.
- GET /submission/{id} — obtiene una entrega por id.
- PATCH /submission/{id} — actualiza el link de una entrega.

### Auth
- POST /auth — login, devuelve un JWT.