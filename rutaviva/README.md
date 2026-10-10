# RutaViva Movilidad
Paso que se han seguid para la construir de la api
1. instalar las dependencias fastapi y luego correr el uv pip install -r requirement.txt
2. dentro de multiper_api crear el core de la api con sus respectivas configuracions
app/core/config.py
3. Archivo: app/core/database.py · Depende de: Tarea 2 (settings)
4. Archivo: app/routers/health.py · Depende de: Tarea 3 (get_db)
5. Archivo: app/models/zone_state.py · Depende de: Tarea 3 (Base)
6. Archivo: app/schemas/multiplier.py · Depende de: nada
7. Archivo: app/repositories/zone_state_repo.py · Depende de: Tarea 5 (ZoneState)
8. Archivos: app/services/multiplier_service.py, app/routers/multiplier.py · Depende de: Tareas 2, 6 y 7
9. Archivo: app/main.py · Depende de: Tareas 4 y 8 (routers). Crea también los __init__.py vacíos en app/ y en cada subcarpeta.
10. Creacion de modulos scripts dentro de app para validar la insepcion de la base de datos y verifacar con el comando python -m scripts.inspect_db