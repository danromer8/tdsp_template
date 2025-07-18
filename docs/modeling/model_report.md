# Reporte del Modelo Final

## Resumen Ejecutivo
El modelo final es un **Random Forest** que mejora el desempeño respecto al baseline de Regresión Logística.  
- **Accuracy:** 0.88  
- **Precision:** 0.86  
- **Recall:** 0.74  
- **F1-score:** 0.80  

La ganancia más significativa se observa en la identificación de la clase “Abandono” (recall pasa de 0.70 a 0.74), lo que permitirá capturar un mayor número de estudiantes en riesgo.

## Descripción del Problema
Se busca predecir la **deserción universitaria** a partir de datos académicos, demográficos y socioeconómicos de 4.424 estudiantes.  
- **Contexto:** Universidad con alta variabilidad en perfiles de ingreso y desempeño.  
- **Objetivo:** Identificar proactivamente a los alumnos con riesgo de abandono para implementar acciones de retención.  
- **Justificación:** Reducir la tasa de deserción mejora la eficiencia institucional y el éxito académico.

## Descripción del Modelo
El modelo final es un **Random Forest** entrenado con 500 árboles y profundidad máxima optimizada por validación cruzada.  
- **Metodología:**  
  1. Preprocesamiento: imputación de faltantes, encoding de categorías y escalado de variables numéricas.  
  2. Balanceo de clases: combinación de undersampling de la clase mayoritaria y oversampling sintético (SMOTE).  
  3. Selección de hiperparámetros mediante Grid Search con validación estratificada.  
  4. Evaluación en conjunto de test independiente (20 % de los datos).

## Evaluación del Modelo

### Métricas globales
| Métrica    | Valor |
|------------|:-----:|
| Accuracy   | 0.88  |
| Precision  | 0.86  |
| Recall     | 0.74  |
| F1-score   | 0.80  |

### Detalle por clase
- **No abandono (0):**  
  - Precision: 0.88  
  - Recall: 0.95  
  - F1-score: 0.91  

- **Abandono (1):**  
  - Precision: 0.86  
  - Recall: 0.74  
  - F1-score: 0.80  

### Variables más importantes
1. total_approved  
2. Curricular units 2nd sem (approved)  
3. mean_grade  
4. Curricular units 2nd sem (grade)  
5. Curricular units 1st sem (approved)  
6. Tuition fees up to date  
7. Curricular units 1st sem (grade)  
8. Age at enrollment  
9. Admission grade  
10. Previous qualification (grade)  

## Conclusiones y Recomendaciones
- **Puntos fuertes:**  
  - Aumento de la sensibilidad al abandono (recall = 0.74).  
  - Excelente desempeño en la detección de no abandono (recall = 0.95).  
  - Variables académicas dominantes, facilitando la interpretación.

- **Limitaciones:**  
  - Aún quedan falsos negativos (~26% de abandonos no detectados).  
  - Dependencia de la calidad de registros académicos y pagos.

- **Recomendaciones de aplicación:**  
  1. **Intervenciones focalizadas** en estudiantes con bajo rendimiento en segundo semestre.  
  2. **Alertas tempranas** para mayores de edad al ingreso y con atrasos en matrícula.  
  3. **Acompañamiento académico** personalizado y seguimiento de indicadores críticos.
