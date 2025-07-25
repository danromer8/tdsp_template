# 📦 Despliegue de Modelos

## 🏗️ Infraestructura

- **Nombre del modelo:** `Student Dropout Prediction`
- **Plataforma de despliegue:** `FastAPI` (ejecutado desde Jupyter Notebook y expuesto mediante `pyngrok`)
- **Requisitos técnicos:**
  - Entorno: Google Colab o Jupyter Notebook
  - Lenguaje: Python 3.10+
  - Bibliotecas utilizadas:
    - `fastapi`
    - `uvicorn`
    - `scikit-learn`
    - `joblib`
    - `pyngrok`
    - `pandas`
    - `psutil`, `subprocess`, `signal`, `os`, `time`
- **Requisitos de seguridad:**
  - Túnel temporal HTTPS generado con ngrok
  - Validación de entrada con `Pydantic` en FastAPI
  - No se implementó autenticación o control de acceso (opcional para producción)

## 🧭 Diagrama de Arquitectura

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1Q9IPtLlwXwvOz7lgJH0g-_aHqHl5KgqU" width="50%">
</div>

**Descripción:**  
El cliente accede al endpoint `/predict` a través de un túnel seguro abierto por ngrok. FastAPI recibe el JSON, lo transforma en `DataFrame`, lo pasa al modelo RandomForest, y retorna las predicciones en formato JSON.

---

## 💻 Código de Despliegue

- **Código principal:** `main.py` (generado automáticamente en el notebook con `%%writefile`)
- **Ruta del modelo serializado:** `/content/model.joblib`
- **Estructura esperada del input:** JSON con una lista bajo el campo `"inputs"` que representa las observaciones a predecir
- **Salida esperada del endpoint `/predict`:**
  ```json
  {
    "predictions": [0, 1],
    "prob_dropout": [0.05, 0.55]
  }
  ```

- **Inicio del servidor y túnel:**
  ```python
  uvicorn.run(app, host="0.0.0.0", port=8000)
  ngrok.connect(8000, "http")
  ```

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1_9qIp9zYfwA5nhPbfjEa1jqsOYhYJbyE" width="80%">
</div>

<div align="center">
<img src="https://drive.google.com/uc?export=view&id=1yH8Jz0fVgZ9sw8qdjQDTsHbLpmnkTvZG" width="80%">
</div>

---

## 📄 Documentación del Despliegue

### 🧩 Instrucciones de instalación

```python
!pip install fastapi uvicorn scikit-learn joblib pyngrok
```

> Nota: Esta instalación se ejecuta dentro del mismo notebook.

---

### ⚙️ Instrucciones de configuración

- No se requiere configuración adicional, salvo definir el `auth_token` de ngrok en:
  ```python
  from pyngrok import conf
  conf.get_default().auth_token = "YOUR_NGROK_TOKEN"
  ```

---

### 🚀 Instrucciones de uso

1. Entrenar el modelo y guardarlo como `model.joblib`.
2. Escribir el archivo `main.py` con el código FastAPI.
3. Iniciar `uvicorn` desde el notebook (en background con `subprocess`).
4. Abrir túnel `ngrok` y obtener la URL pública.
5. Consumir el endpoint desde Postman, navegador, o `requests`.

```python
# Ejemplo de consumo con requests
import requests, json
resp = requests.post(f"{public_url}/predict", json=sample)
print(resp.json())
```

- Acceso a documentación Swagger: `https://<ngrok-id>.ngrok-free.app/docs`

---

### 🔧 Instrucciones de mantenimiento

- Reiniciar el túnel `ngrok` al cerrar sesión.
- Guardar una copia del modelo si se actualiza.
- Verificar que el PID de `uvicorn` no esté duplicado para evitar errores de puerto.
- Agregar autenticación si se considera para despliegue real.

