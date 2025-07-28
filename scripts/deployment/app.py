import gradio as gr
import requests
import pandas as pd
import mlflow.sklearn
import shap

API_URL = "http://localhost:8000/predict"
MLFLOW_TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "rf_optuna_tuning"

df = pd.read_csv("scripts/preprocessing/data_balanced.csv")
feature_names = [col for col in df.columns if col != "Target"]

default_values = {
    "Marital status": 1,
    "Application mode": 15,
    "Application order": 1,
    "Course": 9254,
    '"Daytime/evening attendance\t"': 1,
    "Previous qualification": 1,
    "Previous qualification (grade)": 160,
    "Nacionality": 1,
    "Mother's qualification": 1,
    "Father's qualification": 3,
    "Mother's occupation": 3,
    "Father's occupation": 3,
    "Admission grade": 142.5,
    "Displaced": 1,
    "Educational special needs": 0,
    "Debtor": 0,
    "Tuition fees up to date": 0,
    "Gender": 1,
    "Scholarship holder": 0,
    "Age at enrollment": 19,
    "International": 0,
    "Curricular units 1st sem (credited)": 0,
    "Curricular units 1st sem (enrolled)": 6,
    "Curricular units 1st sem (evaluations)": 6,
    "Curricular units 1st sem (approved)": 6,
    "Curricular units 1st sem (grade)": 14,
    "Curricular units 1st sem (without evaluations)": 0,
    "Curricular units 2nd sem (credited)": 0,
    "Curricular units 2nd sem (enrolled)": 6,
    "Curricular units 2nd sem (evaluations)": 6,
    "Curricular units 2nd sem (approved)": 6,
    "Curricular units 2nd sem (grade)": 13.66666667,
    "Curricular units 2nd sem (without evaluations)": 0,
    "Unemployment rate": 13.9,
    "Inflation rate": -0.3,
    "GDP": 0.79
}


n_cols = 3
cols = [feature_names[i::n_cols] for i in range(n_cols)]

# Carga el mejor modelo desde MLflow (igual que haces en el backend)
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
def load_latest_model(experiment_name):
    client = mlflow.tracking.MlflowClient()
    exp = client.get_experiment_by_name(experiment_name)
    runs = client.search_runs(exp.experiment_id, order_by=["metrics.f1_macro DESC"])
    best_run = runs[0]
    model_uri = f"runs:/{best_run.info.run_id}/model"
    return mlflow.sklearn.load_model(model_uri)

model = load_latest_model(EXPERIMENT_NAME)
explainer = shap.TreeExplainer(model)

def predict_fn(*args):
    inputs = dict(zip(feature_names, args))
    sample = {"inputs": [inputs]}
    try:
        resp = requests.post(API_URL, json=sample)
        if resp.status_code == 200:
            prediction = resp.json()
            predict_fn.last_input = inputs
            y_pred = prediction["predictions"][0]
            class_names = list(model.classes_)
            # Mapear índice a nombre, si aplica
            if isinstance(y_pred, int):
                last_class = class_names[y_pred]
            else:
                last_class = y_pred
            predict_fn.last_class = last_class
            return prediction
        else:
            predict_fn.last_input = None
            predict_fn.last_class = None
            return {"error": f"Status {resp.status_code}: {resp.text}"}
    except Exception as e:
        predict_fn.last_input = None
        predict_fn.last_class = None
        return {"error": str(e)}

predict_fn.last_input = None
predict_fn.last_class = None

def show_shap():
    if predict_fn.last_input is None or predict_fn.last_class is None:
        return "Haz una predicción primero.", None
    X_pred = pd.DataFrame([predict_fn.last_input])
    shap_values = explainer.shap_values(X_pred)
    class_names = list(model.classes_)
    try:
        class_idx = class_names.index(predict_fn.last_class)
    except ValueError:
        return f"No se pudo encontrar la clase {predict_fn.last_class} en {class_names}.", None

    import matplotlib.pyplot as plt
    plt.clf()

    # --- Empareja dimensiones: crea un dict de feature->valor SHAP ---
    shap_dict = dict(zip(X_pred.columns, shap_values[class_idx][0]))
    # Si alguna feature no está en shap_dict (no usada), su valor será 0
    shap_full = [shap_dict.get(feat, 0) for feat in X_pred.columns]

    fig, ax = plt.subplots(figsize=(10, max(4, len(X_pred.columns)//2)))
    ax.barh(list(X_pred.columns)[::-1], shap_full[::-1], 
            color=['red' if v > 0 else 'blue' for v in shap_full[::-1]])
    plt.title(f"Importancia de caracteristicas: {predict_fn.last_class}", fontsize=14)
    plt.xlabel("SHAP value (impact on model output)")
    plt.tight_layout(pad=2)
    plt.subplots_adjust(left=0.35)
    return f"Importancia para la clase '{predict_fn.last_class}' (todas las variables)", plt.gcf()


with gr.Blocks(title="Demo Dropout Prediction con SHAP") as demo:
    with gr.Tab("Predicción"):
        gr.Markdown("# Demo de Predicción de Dropout")
        with gr.Row():
            input_columns = []
            for col_feats in cols:
                with gr.Column():
                    col_inputs = [
                        gr.Number(label=feat, value=default_values.get(feat, None))
                        for feat in col_feats
                    ]
                    input_columns.extend(col_inputs)
            with gr.Column():
                btn = gr.Button("Predecir")
                output_box = gr.JSON(label="Predicción")
                btn.click(
                    predict_fn,
                    inputs=input_columns,
                    outputs=output_box
                )

    with gr.Tab("Interpretabilidad (SHAP)"):
        gr.Markdown("## Importancia de los features (SHAP)")
        shap_text = gr.Textbox(label="Mensaje")
        shap_plot = gr.Plot()
        show_btn = gr.Button("Mostrar SHAP de la última predicción")
        show_btn.click(
            show_shap,
            inputs=[],
            outputs=[shap_text, shap_plot]
        )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
