import sys
from pathlib import Path
import matplotlib.pyplot as plt

CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent.parent  
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.nombre_paquete.utils.paths import DATA_PATH
from src.nombre_paquete.preprocessing.cleaning import clean_data
from src.nombre_paquete.visualization.eda import (
    describe_df, plot_target_distribution, plot_violinplots, plot_strong_correlations
)
import pandas as pd

def main():
    df = pd.read_csv(DATA_PATH , sep=';')   
    df_clean = clean_data(df)
    plot_target_distribution(df_clean, target_col='target')
    plot_violinplots(df_clean, target_col='target')
    plot_strong_correlations(df_clean, threshold=0.6)

if __name__ == "__main__":
    main()
    
    