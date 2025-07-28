import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def describe_df(df):
    print(df.describe().T)

def plot_histogram(df, column):
    plt.figure(figsize=(8, 4))
    df[column].hist(bins=30)
    plt.title(f'Histograma de {column}')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

def plot_target_distribution(df, target_col='Target'):
    if target_col in df.columns:
        target_counts = df[target_col].value_counts()
        target_pct = df[target_col].value_counts(normalize=True) * 100
        print("\nDistribución variable objetivo:")
        print(pd.DataFrame({'Cantidad': target_counts, 'Porcentaje': target_pct.round(1)}))

        plt.figure(figsize=(7,5))
        bars = sns.countplot(x=target_col, data=df, order=target_counts.index, color='skyblue')
        for i, v in enumerate(target_counts):
            bars.text(i, v + 2, f'{v} ({target_pct.iloc[i]:.1f}%)', ha='center', fontsize=12, fontweight='bold')
        plt.title('Distribución de la variable objetivo')
        plt.xlabel('Estado')
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()

def plot_violinplots(df, target_col='Target'):    
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    numerical_cols = [col for col in numerical_cols if col.lower() != target_col.lower()]

    for col in numerical_cols:
        plt.figure(figsize=(8, 5))
        sns.violinplot(data=df, x=target_col, y=col, hue=target_col, inner='quartile', palette='Pastel1', legend=False)
        plt.title(f'Diagrama de violín: {col} vs {target_col}')
        plt.xlabel(target_col)
        plt.ylabel(col)
        plt.tight_layout()
        plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def plot_strong_correlations(df, threshold=0.6):
    # Solo columnas numéricas
    num_df = df.select_dtypes(include=['number'])
    if num_df.shape[1] < 2:
        print("\nNo hay suficientes variables numéricas para mostrar correlación.")
        return
    corr = num_df.corr()
    # Encuentra pares con correlación fuerte
    strong_corrs = (
        corr.stack()
        .reset_index()
        .rename(columns={0: 'Correlación', 'level_0': 'Variable 1', 'level_1': 'Variable 2'})
    )
    strong_corrs = strong_corrs[
        (strong_corrs['Variable 1'] != strong_corrs['Variable 2']) &
        (strong_corrs['Correlación'].abs() > threshold)
    ]

    if not strong_corrs.empty:
        strong_corrs['key'] = strong_corrs.apply(lambda row: '-'.join(sorted([row['Variable 1'], row['Variable 2']])), axis=1)
        strong_corrs = strong_corrs.drop_duplicates('key').drop('key', axis=1)
        strong_corrs = strong_corrs.reindex(strong_corrs['Correlación'].abs().sort_values(ascending=False).index)
        print("\nPares de variables con correlaciones fuertes (>|0.6|):")
        print(strong_corrs)
        # Visualización solo de las variables correlacionadas fuertemente
        top_vars = list(set(strong_corrs['Variable 1'].tolist() + strong_corrs['Variable 2'].tolist()))
        corr_top = corr.loc[top_vars, top_vars]
        plt.figure(figsize=(min(1.5*len(top_vars),12), min(1.5*len(top_vars),12)))
        sns.heatmap(corr_top, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5, square=True)
        plt.title('Correlación fuerte entre variables seleccionadas')
        plt.tight_layout()
        plt.show()
    else:
        print("\nNo hay pares de variables con correlación fuerte (>|0.6|). Mostrando heatmap de TODAS las correlaciones.")
        # Solo muestra si hay al menos 2 variables numéricas
        if corr.shape[1] < 2:
            print("Tampoco hay suficientes variables numéricas para el heatmap.")
            return
        plt.figure(figsize=(min(1.5*len(corr.columns),12), min(1.5*len(corr.columns),12)))
        sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5, square=True)
        plt.title('Heatmap de correlaciones entre todas las variables numéricas')
        plt.tight_layout()
        plt.show()
