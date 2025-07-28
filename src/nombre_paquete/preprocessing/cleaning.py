import pandas as pd

def drop_missing(df, columns=None):
    """Elimina filas con datos faltantes en columnas especificadas o en todas si columns=None."""
    if columns:
        return df.dropna(subset=columns)
    return df.dropna()

def standardize_column_names(df):
    """Estandariza nombres de columnas (minúsculas, sin espacios)."""
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def clean_data(df):
    """Limpieza completa: puedes agregar aquí más pasos."""
    df = standardize_column_names(df)
    #df = drop_missing(df)
    return df
