import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import kagglehub


DATASET_HANDLE = "elemento/nyc-yellow-taxi-trip-data"
DATASET_DIRECTORY = "./data/nyc-yellow-taxi-trip-data"
PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_RAW_DATA_DIR = PROJECT_ROOT / "data" / "bronze"
logger = logging.getLogger("historical-data-ingest")


def ingest_kaggle_dataset(raw_data_dir: Path | None = None) -> Path:
    """Descarga los archivos originales a Bronze, listos para sincronizarlos con S3."""
    configured_raw_dir = os.getenv("RAW_DATA_DIR")
    bronze_dir = raw_data_dir or (
        Path(configured_raw_dir) if configured_raw_dir else DEFAULT_RAW_DATA_DIR
    )
    destination = bronze_dir / DATASET_DIRECTORY
    destination.mkdir(parents=True, exist_ok=True)

    downloaded_dir = Path(
        kagglehub.dataset_download(
            DATASET_HANDLE,
            output_dir=str(destination),
            force_download=False,
        )
    )
    if not downloaded_dir.is_dir():
        raise RuntimeError(
            f"Kaggle no devolvió un directorio de datos válido: {downloaded_dir}"
        )

    files = sorted(path for path in downloaded_dir.rglob("*") if path.is_file())
    if not files:
        raise RuntimeError(
            f"Kaggle no devolvió archivos para el dataset {DATASET_HANDLE}."
        )

    manifest: dict[str, Any] = {
        "source": "kaggle",
        "dataset": DATASET_HANDLE,
        "ingested_at_utc": datetime.now(timezone.utc).isoformat(),
        "files": [
            {
                "path": path.relative_to(downloaded_dir).as_posix(),
                "size_bytes": path.stat().st_size,
            }
            for path in files
        ],
    }
    manifest_path = downloaded_dir / "_source_manifest.json"
    temporary_manifest = manifest_path.with_suffix(".json.tmp")
    temporary_manifest.write_text(
        json.dumps(manifest, indent=2),
        encoding="utf-8",
    )
    temporary_manifest.replace(manifest_path)

    logger.info(
        "Dataset descargado desde Kaggle: %s archivos en %s",
        len(files),
        downloaded_dir,
    )
    return downloaded_dir


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    output_path = ingest_kaggle_dataset()
    print(f"Archivos Bronze listos para sincronizar con S3: {output_path}")
