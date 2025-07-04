# Librerias

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 0. Configuaración general
sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# 1. Cargar datos
df = pd.read_csv('data.csv', sep=';')

# 2. Resumen general
print(f"Observaciones: {df.shape[0]}, Variables: {df.shape[1]}")
print("\nPrimeras filas:")
print(df.head())

# 3. Tipos de variables
print("\nTipos de variables:\n", df.dtypes.value_counts())

# 4. Valores faltantes
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({'Nulos': missing, 'Porcentaje': missing_pct})
missing_df = missing_df[missing_df['Nulos'] > 0].sort_values('Porcentaje', ascending=False)
print("\nValores faltantes:")
print(missing_df)

# 5. Duplicados
print("\nDuplicados:", df.duplicated().sum())

# 6. Estadísticas descriptivas
print("\nEstadísticas descriptivas de variables numéricas:")
print(df.describe().T)

# 7. Variable objetivo (Target)
if 'Target' in df.columns:
    target_counts = df['Target'].value_counts()
    target_pct = df['Target'].value_counts(normalize=True) * 100
    print("\nDistribución variable objetivo:")
    print(pd.DataFrame({'Cantidad': target_counts, 'Porcentaje': target_pct.round(1)}))

    plt.figure(figsize=(7,5))
    bars = sns.countplot(x='Target', data=df, order=target_counts.index, color='skyblue')
    for i, v in enumerate(target_counts):
        bars.text(i, v + 2, f'{v} ({target_pct.iloc[i]:.1f}%)', ha='center', fontsize=12, fontweight='bold')
    plt.title('Distribución de la variable objetivo')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.show()

# 8. Histogramas para variables clave
for col in ['Age at enrollment', 'Admission grade']:
    if col in df.columns:
        plt.figure(figsize=(7,5))
        sns.histplot(df[col], bins=20, kde=True, color='royalblue')
        plt.title(f'Distribución de {col}')
        plt.xlabel(col)
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()

# 9. Correlaciones fuertes (|r| > 0.6)
corr = df.select_dtypes(include=['number']).corr()
mask_strong = (corr.abs() > 0.6) & (corr.abs() < 1)

strong_corrs = (
    corr.where(mask_strong)
    .stack()
    .reset_index()
    .rename(columns={'level_0': 'Variable 1', 'level_1': 'Variable 2', 0: 'Correlación'})
)
# Quita duplicados reversos (A-B y B-A)
strong_corrs['key'] = strong_corrs.apply(lambda row: '-'.join(sorted([row['Variable 1'], row['Variable 2']])), axis=1)
strong_corrs = strong_corrs.drop_duplicates('key').drop('key', axis=1)
strong_corrs = strong_corrs.reindex(strong_corrs['Correlación'].abs().sort_values(ascending=False).index)

if not strong_corrs.empty:
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
    print("\nNo hay pares de variables con correlación fuerte (>|0.6|).")
