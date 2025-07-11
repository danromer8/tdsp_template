# Reporte de Datos

Este documento recoge los principales hallazgos del análisis exploratorio realizado sobre el conjunto de datos de estudiantes.

---

## 1. Resumen general de los datos

- **Observaciones**: 4 424 registros.  
- **Variables**: 34 numéricas (por ejemplo, edad, nota de admisión, unidades curriculares) y 10 categóricas (‘Target’, género, beca, nacionalidad, etc.).  
- **Tipos de variables**  
  - *Numéricas continuas*: `Age at enrollment`, `Admission grade`, tasas macroeconómicas, etc.  
  - *Numéricas discretas*: conteos de unidades curriculares (enrolled, credited, approved, evaluations).  
  - *Categóricas binarias*: `Displaced`, `International`, `Debtor`, etc.  
  - *Categóricas multiclase*: `Target` (Graduate, Dropout, Enrolled), `Course`, nivel de estudios de padres.  
- **Valores faltantes**: No se detectaron valores nulos en las variables principales (cada variable numérica tiene recuento = 4 424).  
- **Duplicados**: Ningún registro duplicado identificado tras inspección con `df.duplicated().sum() = 0`.

---

## 2. Resumen de calidad de los datos

| Tipo de problema    | Cantidad       | % sobre total | Acción tomada         |
|---------------------|----------------|---------------|-----------------------|
| Valores faltantes   |       0        |      0 %      | —                     |
| Valores extremos    | Varios outliers en notas ≥ 160 y edades ≥ 50 | < 1 % | Se mantuvieron (pueden ser estudiantes maduros o con altas calificaciones). |
| Errores tipográficos| 0 variables    | 0 %           | —                     |
| Duplicados          | 0              | 0 %           | —                     |

---

## 3. Variable objetivo

- **Nombre**: `Target`  
- **Clases**:  
  - Graduate: 2 209 (49.9 %)  
  - Dropout: 1 421 (32.1 %)  
  - Enrolled:   794 (17.9 %)  
- **Comentario**: desequilibrio moderado. Más de la mitad de los alumnos finalizan (Graduate), mientras que la clase minoritaria (Enrolled) representa menos del 20 %.  

---

## 4. Variables individuales

### 4.1 Age at enrollment  
- **Resumen**: media 23.3 años (std 7.6), rango [17–70].  
- **Distribución**: fuerte concentración entre 18–22 años y larga cola hacia edades mayores.  
- **Relación con `Target`**: los Graduate tienden a matricularse más jóvenes que los Dropout y Enrolled.  

<details>
<summary>Ver histograma de edad</summary>

</details>

---

### 4.2 Admission grade  
- **Resumen**: media 127.0 (std 14.5), rango [95–190].  
- **Distribución**: casi normal, ligero sesgo a la derecha, pico alrededor de 125.  
- **Relación con `Target`**: los Graduate presentan notas de admisión ligeramente superiores en promedio.  

<details>
<summary>Ver distribución de nota de admisión</summary>

</details>

---

### 4.3 Unidades curriculares (1er y 2º semestre)  
- *Credited*, *Enrolled*, *Evaluations*, *Approved*, *Grade*  
- Correlación muy alta entre métricas homólogas de ambos semestres (r ≥ 0.75).  
- Pocos valores faltantes; algunos outliers en número de créditos.

---

## 5. Ranking de variables

Para priorizar las variables más predictivas de `Target` se usaron dos enfoques:

1. **Correlación de Pearson** con la clase *Dropout* (codificada como dummy):  
   - Top‐3 continuas: `Curricular units 1st sem (grade)`, `Curricular units 2nd sem (grade)`, `Admission grade`.  
2. **Importancia en un Random Forest** (20 % test, semilla fija):  
   - Variables más relevantes:  
     1. `Curricular units 2nd sem (approved)`  
     2. `Age at enrollment`  
     3. `Admission grade`

---

## 6. Relación entre variables explicativas y variable objetivo

- **Matriz de correlación**  
  ![Matriz de correlación](./figures/corr_matrix.png)  
  Destaca fuertes correlaciones entre calificaciones y unidades de crédito; las variables socio‐económicas (ocupación de padres, nacionalidad) muestran baja relación lineal.

- **Diagramas de violín**  
  Se generaron para cada variable numérica frente a `Target` evidenciando algunos comportamientos entre variables y las subclases de la variable Target

Permiten visualizar la dispersión y mediana de cada grupo.

Scatter plots
Algunas parejas de variables (e.g., Admission grade vs. Curricular units 1st sem (grade)) muestran agrupamientos claros según la clase.

---

## 7.Próximos pasos

Balancear la variable objetivo (SMOTE, submuestreo).

Probar escalado/normalización en variables con rangos dispares.

Evaluar modelos con selección automática de características (Lasso, XGBoost).

Validar hallazgos en un conjunto de validación independiente.
  
  
 


