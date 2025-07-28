import sys
from pathlib import Path
import pandas as pd
import mlflow
import mlflow.sklearn

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.nombre_paquete.training.optuna_tuning import run_xgb_optuna

import mlflow
mlflow.set_tracking_uri("http://localhost:5000")

# Cargar datos balanceados
df_bal = pd.read_csv(ROOT_DIR / "scripts" / "preprocessing" / "data_balanced.csv")
X = df_bal.drop(columns=["Target"])
y = df_bal["Target"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

study = run_xgb_optuna(X_train, y_train, X_test, y_test, n_trials=50)

print("Mejores hiperparámetros XGBoost:", study.best_params)
print("Mejor f1_macro:", study.best_value)
