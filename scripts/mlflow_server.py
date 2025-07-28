import os
import subprocess
import time
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("No se encontró python-dotenv. Variables de entorno solo por el sistema o consola.")

# Si tienes src/nombre_paquete/utils/paths.py, úsalo:
try:
    from src.nombre_paquete.utils.paths import ROOT_DIR, MLRUNS_DIR, TRACKING_DB
except ImportError:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    MLRUNS_DIR = ROOT_DIR / "mlruns"
    TRACKING_DB = ROOT_DIR / "tracking.db"

MLFLOW_PORT = int(os.getenv("MLFLOW_PORT", 5000))

# Usa variables de entorno, o defaults a tu estructura de proyecto
MLFLOW_BACKEND = os.getenv("MLFLOW_BACKEND", f"sqlite:///{TRACKING_DB}")
MLFLOW_ARTIFACT = os.getenv("MLFLOW_ARTIFACT", f"file:{MLRUNS_DIR}")

def launch_mlflow():
    print(f"\nLanzando MLflow en http://localhost:{MLFLOW_PORT}")
    print(f"  - Tracking: {MLFLOW_BACKEND}")
    print(f"  - Artefactos: {MLFLOW_ARTIFACT}\n")
    mlflow_proc = subprocess.Popen([
        "mlflow", "ui",
        "--backend-store-uri", MLFLOW_BACKEND,
        "--default-artifact-root", MLFLOW_ARTIFACT,
        "--port", str(MLFLOW_PORT)
    ])
    # Esperar a que el servidor arranque
    time.sleep(5)
    return mlflow_proc

if __name__ == "__main__":
    mlflow_proc = launch_mlflow()
    try:
        print("MLflow UI disponible en: http://localhost:{0}".format(MLFLOW_PORT))
        print("Ctrl+C para detener el servicio.")
        mlflow_proc.wait()
    except KeyboardInterrupt:
        print("\nDeteniendo MLflow...")
        mlflow_proc.terminate()


