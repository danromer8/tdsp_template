# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline construido con Regresión Logística para la predicción de deserción universitaria.

## Descripción del modelo
El modelo baseline es un clasificador de **Regresión Logística** entrenado para establecer una línea base de desempeño. 

## Variables de entrada
Se emplearon 37 variables de entrada, que incluyen:
- **Variables demográficas**: estado civil, nacionalidad, asistencia diurna/vespertina.  
- **Variables académicas**: modo de solicitud de admisión, orden de solicitud, curso, número de asignaturas cursadas (acreditadas, inscritas, evaluadas, aprobadas), calificaciones previas.  
- **Variables socioeconómicas**: tasa de desempleo, tasa de inflación, PIB per cápita.  

## Variable objetivo
- **Abandono**: variable binaria donde  
  - `0` = No abandono  
  - `1` = Abandono  

## Evaluación del modelo

### Métricas de evaluación
Para evaluar el desempeño se consideraron:
- **Accuracy**: proporción de predicciones correctas.  
- **Precision**: proporción de verdaderos positivos sobre todas las predicciones positivas.  
- **Recall** (Sensibilidad): proporción de verdaderos positivos sobre todos los casos positivos reales.  
- **F1-score**: media armónica entre precision y recall.

### Resultados de evaluación

| Métrica    | Valor |
|------------|:-----:|
| Accuracy   | 0.86  |
| Precision  | 0.85  |
| Recall     | 0.70  |
| F1-score   | 0.77  |

#### Detalle por clase
- **Clase “No abandono” (0):**  
  - Precision: 0.87  
  - Recall: 0.94  
  - F1-score: 0.90  

- **Clase “Abandono” (1):**  
  - Precision: 0.85  
  - Recall: 0.70  
  - F1-score: 0.77  

## Análisis de los resultados
El modelo de Regresión Logística supera el umbral de éxito definido (75 % de accuracy), alcanzando un **86 %** de acierto global. La alta precision para la clase de abandono (0.85) indica que cuando el modelo predice abandono, lo hace con buena exactitud. Sin embargo, el **recall de 0.70** para esa misma clase revela que el modelo deja pasar el **30 %** de estudiantes que realmente abandonan (falsos negativos), lo cual puede ser crítico en un escenario de intervención temprana.

## Conclusiones
- La **línea base** de Regresión Logística muestra un desempeño sólido en precisión general y para la detección de no abandono.  
- Existen márgenes de mejora en la **sensibilidad** hacia los casos de abandono (recall = 0.70).  
- **Recomendaciones**:  
  1. Explorar modelos más complejos (Random Forest, Gradient Boosting, XGBoost).  
  2. Realizar ajuste fino de hiperparámetros y selección de características para incrementar la capacidad de detección de abandono. 
