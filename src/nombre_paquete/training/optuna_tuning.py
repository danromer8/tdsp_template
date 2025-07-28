import mlflow
import mlflow.sklearn
import optuna
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

def optuna_objective_xgb(trial, X_train, y_train, X_test, y_test, le):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 400),
        "max_depth": trial.suggest_int("max_depth", 3, 20),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
        "gamma": trial.suggest_float("gamma", 0, 5),
        "random_state": 42,
        "use_label_encoder": False,
        "eval_metric": "mlogloss"
    }
    with mlflow.start_run(nested=True):
        clf = XGBClassifier(**params)
        clf.fit(X_train, le.transform(y_train))
        y_pred = clf.predict(X_test)
        score = f1_score(le.transform(y_test), y_pred, average="macro")
        mlflow.log_params(params)
        mlflow.log_metric("f1_macro", score)
        mlflow.sklearn.log_model(clf, "model")
    return score

def run_xgb_optuna(X_train, y_train, X_test, y_test, n_trials=30, experiment_name="xgb_optuna_tuning"):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    le.fit(y_train)
    mlflow.set_experiment(experiment_name)
    study = optuna.create_study(direction="maximize")
    study.optimize(lambda trial: optuna_objective_xgb(trial, X_train, y_train, X_test, y_test, le), n_trials=n_trials)
    return study
