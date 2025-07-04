# Definición de los datos

## Origen de los datos

La fuente principal de datos utilizada en este proyecto corresponde al dataset Student Dropout, Graduation, and Enrolment Data disponible públicamente en Kaggle.
El archivo de datos fue descargado en formato CSV y corresponde a un registro real/anónimo de estudiantes universitarios, con variables académicas, demográficas y socioeconómicas.

## Especificación de los scripts para la carga de datos

El script utilizado para la carga de datos es carga_datos.py, ubicado en la carpeta /src/ del repositorio.
Este script utiliza la librería pandas para leer los datos desde el archivo CSV, separar las columnas utilizando el delimitador ; y realizar una visualización inicial del contenido.

# src/carga_datos.
import pandas as pd

# Ruta de origen
ruta_origen = 'data_acquisition/data.csv'

# Carga del archivo con el delimitador correcto
df = pd.read_csv(ruta_origen, sep=';')
print(df.head())


## Referencias a rutas o bases de datos origen y destino

Ruta de datos origen:
/data_acquisition/data.csv

Ruta de datos destino:
/preprocessing/data_clean.csv (archivo que se generará después de la limpieza y transformación)

### Rutas de origen de datos

Ubicación del archivo de origen:
Carpeta /data_acquisition/ dentro del repositorio del proyecto, archivo data.csv.

Estructura del archivo de origen:
Formato: CSV (valores separados por punto y coma ;).
Cada fila corresponde a un estudiante.
Columnas: Estado civil, modalidad de aplicación, notas, edad, género, nivel educativo de padres, variables socioeconómicas, etc.

Los procedimientos principales de limpieza y transformación incluyen:

Separación de columnas utilizando el delimitador adecuado (sep=';').

Conversión de tipos de datos (numéricos y categóricos).

Manejo de valores nulos y datos atípicos.

Estandarización de variables categóricas.

Codificación de variables objetivo y predictoras para modelamiento.

Generación de un archivo limpio (data_clean.csv) en la carpeta /data/processed/.

Ejemplo de fragmento de código para limpieza:

# Limpieza de valores nulos
df_clean = df.dropna()

# Conversión de variables categóricas a tipo category
df_clean['Gender'] = df_clean['Gender'].astype('category')

# Guardar archivo procesado
df_clean.to_csv('data/processed/data_clean.csv', index=False)

### Base de datos de destino

Base de datos de destino:
Archivo CSV limpio y procesado, ubicado en /data/processed/data_clean.csv.

Estructura de la base de datos destino:
Igual a la de origen pero sin errores, sin duplicados, y con tipos de datos adecuados para análisis.

Procedimientos de carga y transformación:
El script carga_datos.py realiza la limpieza y transformación y guarda el resultado final en la carpeta correspondiente.
