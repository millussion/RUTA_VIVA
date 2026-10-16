# Historical Data Ingest

Descarga los archivos originales de `elemento/nyc-yellow-taxi-trip-data` con
KaggleHub y los deja en la capa local Bronze. No convierte ni agrega los CSV:
la unificación de esquemas, validación, cuarentena y modelo Gold corresponden
a los jobs de Spark.

## Requisitos de Kaggle

Configura `KAGGLE_API_TOKEN` en el entorno de ejecución o instala las
credenciales oficiales en `~/.kaggle/kaggle.json`. Debes tener acceso al
dataset en Kaggle. No guardes ni subas credenciales al repositorio.

## Ejecución local

Desde la raíz del repositorio:

```powershell
$env:KAGGLE_API_TOKEN = "<token de Kaggle>"
uv run python services/historical-data-ingest/app/data-ingest.py
```

La ruta por defecto es `data/bronze/nyc-yellow-taxi-trip-data/`. Puedes
establecer `RAW_DATA_DIR` para elegir otro directorio local o un volumen
montado. La carpeta contiene los archivos descargados sin modificar y
`_source_manifest.json`, con el dataset de origen, la hora de ingesta y los
nombres y tamaños de los archivos.

## Uso del contenedor

Construye la imagen desde la raíz del repositorio para que Docker pueda leer el
Dockerfile y copiar la aplicación. En ejecución, pasa `KAGGLE_API_TOKEN` como
secreto del entorno y monta un volumen en `/data`; el contenedor escribe en
`/data/bronze/nyc-yellow-taxi-trip-data/`.

La carpeta Bronze tiene una estructura adecuada para sincronizarla luego a una
ruta como `s3://<bucket>/bronze/nyc-yellow-taxi-trip-data/`. La carga a S3 no
está implementada todavía.

## Relación con el modelo analítico

Este servicio solo ingiere la fuente histórica de viajes (F1). Los archivos
originales son entrada para Spark y no son todavía `FACT_TRIP` ni las demás
tablas Gold. Para completar ese modelo se deben integrar fuentes adicionales
como clima histórico, reglas tarifarias, auditoría de tarifas y eventos, y
definir cómo calcular las métricas que no vienen en el dataset de viajes.
