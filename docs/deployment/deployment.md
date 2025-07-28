
markdown
Copiar
Editar
# 📦 Despliegue de Modelos

## 🏗️ Infraestructura

- **Nombre del modelo:** `Student Dropout Prediction`
- **Plataforma de despliegue:** `FastAPI` (desplegado localmente en entorno virtual)
- **Requisitos técnicos:**
  - Entorno: Jupyter Notebook o entorno Python 3.10+ con venv
  - Lenguaje: Python 3.10+
  - Bibliotecas utilizadas:
    - `fastapi`
    - `uvicorn`
    - `scikit-learn`
    - `mlflow`
    - `joblib`
    - `pandas`
    - `gradio` (para interfaz de usuario)
    - `matplotlib`, `shap`, `seaborn` (para visualización e interpretabilidad)
    - `psutil`, `subprocess`, `signal`, `os`, `time` (para utilidades)
- **Requisitos de seguridad:**
  - Acceso local restringido (localhost)
  - Validación de entrada con `Pydantic` en FastAPI
  - No se implementó autenticación ni control de acceso (opcional para producción)

---

## 🧭 Diagrama de Arquitectura

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1Q9IPtLlwXwvOz7lgJH0g-_aHqHl5KgqU" width="60%">
</div>

**Descripción:**  
El cliente (navegador o consumidor vía API) accede al endpoint `/predict` de FastAPI.  
FastAPI recibe el JSON, lo convierte en `DataFrame`, consulta el modelo (cargado desde MLflow o archivo local), y retorna la predicción en formato JSON.  
La interfaz de usuario (Gradio) también consume el endpoint local para realizar predicciones y mostrar interpretabilidad (SHAP).

---

## 💻 Código de Despliegue

- **Script principal de la API:**  
  `scripts/deployment/api.py`  
  (o `main.py` si se utiliza en notebook para prototipo)

- **Ruta del modelo serializado:**  
  - Desde MLflow (ruta automática)  
  - O desde archivo local (ejemplo: `mlruns/.../model`, `model.joblib`)

- **Estructura esperada del input:**  
  JSON con una lista bajo el campo `"inputs"` que representa las observaciones a predecir.

- **Salida esperada del endpoint `/predict`:**
  ```json
  {
    "predictions": ["Dropout", "Graduate"],
    "prob_dropout": [0.75, 0.10]
  }


- **Inicio del servidor local:**
  ```python
  uvicorn scripts.deployment.api:app --reload
  ```
Acceso en: http://localhost:8000/docs


<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1_9qIp9zYfwA5nhPbfjEa1jqsOYhYJbyE" width="80%">
</div>

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1yH8Jz0fVgZ9sw8qdjQDTsHbLpmnkTvZG" width="80%">
</div>

---

## 📄 Documentación del Despliegue

### 🧩 Instrucciones de instalación

Instalar dependencias en el entorno virtual del proyecto:

`pip install -r requirements.txt`

O, si se usan módulos sueltos:

`pip install fastapi uvicorn scikit-learn mlflow joblib pandas gradio matplotlib shap seaborn`

### ⚙️ Instrucciones de configuración

No se requiere configuración adicional.  
Si se consume modelo desde MLflow, verificar que el tracking server esté corriendo con:  
`python scripts/training/mlflow_server.py`

### 🚀 Instrucciones de uso

1. Entrenar y guardar el modelo con MLflow o `joblib`.
2. Colocar el modelo accesible para la API (`mlruns/.../model` o `model.joblib`).
3. Iniciar la API ejecutando:  
   `uvicorn scripts.deployment.api:app --reload`
4. (Opcional) Iniciar la interfaz Gradio ejecutando:  
   `python scripts/deployment/app.py`
5. Consumir el endpoint `/predict` desde Swagger UI (`http://localhost:8000/docs`), la aplicación Gradio (`http://localhost:7860`) o cualquier cliente REST, por ejemplo:

```python
import requests
resp = requests.post("http://localhost:8000/predict", json=sample)
print(resp.json())
```

### 🔧 Instrucciones de mantenimiento

- Si se actualiza el modelo, volver a guardar y reiniciar la API.
- Verificar que el puerto de `uvicorn` (por defecto 8000) esté disponible y libre.
- Para ambientes productivos: agregar autenticación, logging, y control de acceso según los estándares de la institución.
- Documentar el versionado del modelo en MLflow para trazabilidad y reproducibilidad.
- Mantener actualizadas las dependencias en el archivo `requirements.txt`.
- Realizar pruebas periódicas a la API usando Swagger UI o scripts automatizados para asegurar su correcto funcionamiento.
- Monitorear el consumo de recursos del servidor, especialmente si se implementa en ambientes compartidos.

### 📝 Observaciones

- El túnel `ngrok` fue usado únicamente para prototipos y acceso remoto temporal (Colab/Notebook).  
  En despliegues locales y productivos no es necesario.
- El despliegue actual está orientado a pruebas, demostraciones y validación de resultados en ambiente controlado.
- La interfaz Gradio permite probar el modelo de manera visual y ver la explicabilidad de cada predicción mediante gráficos SHAP.
- Para uso institucional o productivo se recomienda adicionar seguridad, versionado explícito de artefactos y un pipeline de CI/CD.

---

**Autores:**  
Daniel Enrique Romero Cantor  
Ivan Herney Hernandez  

