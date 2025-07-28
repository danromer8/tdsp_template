import sys
from pathlib import Path
import pandas as pd

# Rutas portables
CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.nombre_paquete.utils.paths import DATA_PATH
from src.nombre_paquete.preprocessing.balancing import balance_classes

def main():
    # Cargar datos crudos
    df = pd.read_csv(DATA_PATH, sep=';')

    # Balancear
    X_bal, y_bal = balance_classes(df, target_col="Target", method="smote")

    # Guardar nuevo dataset balanceado
    balanced_df = pd.DataFrame(X_bal, columns=[col for col in df.columns if col != "Target"])
    balanced_df["Target"] = y_bal
    output_path = ROOT_DIR / "scripts" / "preprocessing" / "data_balanced.csv"
    balanced_df.to_csv(output_path, index=False)
    print(f"Dataset balanceado guardado en: {output_path}")

if __name__ == "__main__":
    main()
