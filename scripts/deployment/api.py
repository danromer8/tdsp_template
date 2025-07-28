from fastapi import FastAPI
from pydantic import create_model, BaseModel
from typing import List
import mlflow
import pandas as pd
import os

app = FastAPI(
    title="Student Dropout Prediction API",
    description="Devuelve etiqueta y probabilidad de abandono (batch o uno solo)",
    version="1.0.0"
)

# Configuración de MLflow (ajusta si usas otro server o experiment)
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

EXPERIMENT_NAME = "xgb_optuna_tuning" 
MODEL_STAGE = "None"  
MODEL_NAME = "XGboost.v1"  


# --------- 1. Descubre los features automáticamente ---------

# Carga el CSV solo para conocer los nombres de los features
df = pd.read_csv("scripts/preprocessing/data_balanced.csv")
feature_names = [col for col in df.columns if col != "Target"]
fields = {col: (float, ...) for col in feature_names}  # Ajusta tipo si tienes str o bool

# Autogenera la clase InputData
InputData = create_model("InputData", **fields)

class BatchInput(BaseModel):
    inputs: List[InputData]

# --------- 2. Carga el mejor modelo desde MLflow ---------
def load_latest_model(experiment_name):
    client = mlflow.tracking.MlflowClient()
    exp = client.get_experiment_by_name(experiment_name)
    if exp is None:
        raise Exception(f"Experimento '{experiment_name}' no existe.")
    runs = client.search_runs(exp.experiment_id, order_by=["metrics.f1_macro DESC"])
    if not runs:
        raise Exception("No hay runs en el experimento.")
    best_run = runs[0]
    model_uri = f"runs:/{best_run.info.run_id}/model"
    return mlflow.sklearn.load_model(model_uri)

model = load_latest_model(EXPERIMENT_NAME)

# --------- 3. Endpoint de predicción ---------
@app.post("/predict")
async def predict(data: BatchInput):
    df = pd.DataFrame([item.dict() for item in data.inputs])
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df)
        if proba.shape[1] == 2:  # Para clasificación binaria
            dropout_proba = proba[:, 1]
        else:  # Para multiclase, puedes reportar todas las probabilidades
            dropout_proba = proba.max(axis=1)
        preds = model.predict(df)
        return {"predictions": preds.tolist(),
                "prob_dropout": dropout_proba.round(3).tolist()}
    else:
        preds = model.predict(df)
        return {"predictions": preds.tolist()}

# --------- 4. Endpoint de prueba en / (opcional) ---------
@app.get("/")
def root():
    return {"status": "OK", "message": "API corriendo y lista para predecir"}
