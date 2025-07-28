import sys
from pathlib import Path
import pandas as pd
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import tempfile
from sklearn.preprocessing import LabelEncoder

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("exp_comparacion_modelos")

# Ajustar el path para encontrar src/
CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.nombre_paquete.training.model_utils import get_model
from src.nombre_paquete.evaluation.metrics import get_classification_metrics, get_confusion

# MLflow experiment
mlflow.set_experiment("exp_comparacion_modelos")

# Cargar dataset balanceado
df_bal = pd.read_csv(ROOT_DIR / "scripts" / "preprocessing" / "data_balanced.csv")
X = df_bal.drop(columns=["Target"])
y = df_bal["Target"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

modelos = [
    {"name": "RandomForest", "params": {"random_state": 42}},
    {"name": "LogisticRegression", "params": {"max_iter": 1000, "random_state": 42}},
    {"name": "SVM", "params": {"probability": True, "random_state": 42}},
    {"name": "KNeighbors", "params": {}},
    {"name": "XGBoost", "params": {"random_state": 42, "use_label_encoder": False, "eval_metric": 'mlogloss'}},
]

le = LabelEncoder()
le.fit(y_train)  

for modelo_cfg in modelos:
    nombre = modelo_cfg["name"]
    params = modelo_cfg["params"]
    with mlflow.start_run(run_name=nombre):
        print(f"Entrenando modelo: {nombre}")
        modelo = get_model(nombre, **params)
        # --- SOLO XGBoost requiere codificación ---
        if nombre == "XGBoost":
            y_train_enc = le.transform(y_train)
            y_test_enc = le.transform(y_test)
            modelo.fit(X_train, y_train_enc)
            y_pred = modelo.predict(X_test)
            # Convierte las predicciones numéricas a string para métricas y reporting
            y_pred_labels = le.inverse_transform(y_pred)
            report = get_classification_metrics(y_test, y_pred_labels)
            cm = get_confusion(y_test, y_pred_labels, labels=le.classes_)
        else:
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
            report = get_classification_metrics(y_test, y_pred)
            cm = get_confusion(y_test, y_pred, labels=modelo.classes_)
        mlflow.log_param("modelo", nombre)
        mlflow.log_metrics({
            "accuracy": report["accuracy"],
            "f1_macro": report["macro avg"]["f1-score"],
            "recall_macro": report["macro avg"]["recall"],
        })
        mlflow.sklearn.log_model(modelo, "model")
        # Matriz de confusión
        plt.figure(figsize=(6,6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=le.classes_ if nombre == "XGBoost" else modelo.classes_,
                    yticklabels=le.classes_ if nombre == "XGBoost" else modelo.classes_)
        plt.title(f"Matriz de Confusión: {nombre}")
        plt.xlabel("Predicho")
        plt.ylabel("Real")
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_img:
            plt.savefig(tmp_img.name)
            plt.close()
            mlflow.log_artifact(tmp_img.name, artifact_path="confusion_matrix")
        print(f"{nombre} terminado y registrado en MLflow\n")