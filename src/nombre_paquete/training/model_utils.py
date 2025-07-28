from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

def get_model(name, **kwargs):
    """
    Devuelve una instancia de modelo según el nombre.
    """
    models = {
        "RandomForest": RandomForestClassifier,
        "LogisticRegression": LogisticRegression,
        "SVM": SVC,
        "KNeighbors": KNeighborsClassifier,
        "XGBoost": XGBClassifier,
    }
    if name not in models:
        raise ValueError(f"Modelo '{name}' no soportado.")
    return models[name](**kwargs)
