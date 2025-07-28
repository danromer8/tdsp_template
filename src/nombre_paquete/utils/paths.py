from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3] 

DATA_PATH = ROOT_DIR / "scripts" / "data_acquisition" / "data.csv"
EDA_DIR = ROOT_DIR / "scripts" / "eda"
PREPROCESSING_DIR = ROOT_DIR / "scripts" / "preprocessing"
TRAINING_DIR = ROOT_DIR / "scripts" / "training"
MLRUNS_DIR = ROOT_DIR / "mlruns"
TRACKING_DB = ROOT_DIR / "tracking.db"
