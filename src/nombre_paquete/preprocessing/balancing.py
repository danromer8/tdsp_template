from imblearn.over_sampling import SMOTE
from collections import Counter

def balance_classes(df, target_col="Target", method="smote", random_state=42):

    X = df.drop(columns=[target_col])
    y = df[target_col]

    smote = SMOTE(random_state=42)
    X_bal, y_bal = smote.fit_resample(X, y)


    print("Distribución antes:", Counter(y))
    print("Distribución después:", Counter(y_bal))

    return X_bal, y_bal
