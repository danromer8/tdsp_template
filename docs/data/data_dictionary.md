# Diccionario de datos

## Base de datos 1

Tabla principal del proyecto. Contiene información demográfica, académica y socioeconómica de estudiantes universitarios, utilizada para predecir el abandono estudiantil.

| Variable                                       | Descripción                              | Tipo de dato | Rango/Valores posibles                | Fuente de datos                 |
| ---------------------------------------------- | ---------------------------------------- | ------------ | ------------------------------------- | ------------------------------- |
| Marital status                                 | Estado civil del estudiante              | Categórica   | 1=Soltero, 2=Casado, 3=Otro           | Kaggle: Student Dropout Dataset |
| Application mode                               | Modalidad de aplicación                  | Categórica   | 1=En línea, 2=Presencial, ...         | Kaggle: Student Dropout Dataset |
| Application order                              | Orden de aplicación                      | Numérica     | 1, 2, 3, ...                          | Kaggle: Student Dropout Dataset |
| Course                                         | Código del programa académico            | Numérica     | 171, 9254, 9070, ...                  | Kaggle: Student Dropout Dataset |
| Daytime/evening attendance                     | Asistencia diurna/nocturna               | Categórica   | 1=Diurna, 0=Nocturna                  | Kaggle: Student Dropout Dataset |
| Previous qualification                         | Nivel educativo previo                   | Categórica   | 1=Secundaria, 2=Preuniversitario, ... | Kaggle: Student Dropout Dataset |
| Previous qualification (grade)                 | Nota promedio en formación previa        | Numérica     | 0 - 200                               | Kaggle: Student Dropout Dataset |
| Nacionality                                    | Nacionalidad del estudiante              | Categórica   | 1=Local, 2=Extranjero, ...            | Kaggle: Student Dropout Dataset |
| Mother's qualification                         | Nivel educativo de la madre              | Categórica   | 1=Básico, 2=Secundaria, ...           | Kaggle: Student Dropout Dataset |
| Father's qualification                         | Nivel educativo del padre                | Categórica   | 1=Básico, 2=Secundaria, ...           | Kaggle: Student Dropout Dataset |
| Mother's occupation                            | Ocupación de la madre                    | Categórica   | 1=Desconocido, 2=Empleado, ...        | Kaggle: Student Dropout Dataset |
| Father's occupation                            | Ocupación del padre                      | Categórica   | 1=Desconocido, 2=Empleado, ...        | Kaggle: Student Dropout Dataset |
| Admission grade                                | Nota de admisión a la universidad        | Numérica     | 0 - 200                               | Kaggle: Student Dropout Dataset |
| Displaced                                      | Estudiante desplazado                    | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Educational special needs                      | Necesidades educativas especiales        | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Debtor                                         | Si tiene deuda con la universidad        | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Tuition fees up to date                        | Pago de matrícula al día                 | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Gender                                         | Género del estudiante                    | Binaria      | 1=Masculino, 0=Femenino               | Kaggle: Student Dropout Dataset |
| Scholarship holder                             | Beneficiario de beca                     | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Age at enrollment                              | Edad al matricularse                     | Numérica     | 16 - 60                               | Kaggle: Student Dropout Dataset |
| International                                  | Estudiante internacional                 | Binaria      | 1=Sí, 0=No                            | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (credited)            | Créditos matriculados primer semestre    | Numérica     | 0 - 60                                | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (enrolled)            | Créditos inscritos primer semestre       | Numérica     | 0 - 60                                | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (evaluations)         | Evaluaciones primer semestre             | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (approved)            | Materias aprobadas primer semestre       | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (grade)               | Nota promedio primer semestre            | Numérica     | 0 - 20                                | Kaggle: Student Dropout Dataset |
| Curricular units 1st sem (without evaluations) | Materias sin evaluar primer semestre     | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (credited)            | Créditos matriculados segundo semestre   | Numérica     | 0 - 60                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (enrolled)            | Créditos inscritos segundo semestre      | Numérica     | 0 - 60                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (evaluations)         | Evaluaciones segundo semestre            | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (approved)            | Materias aprobadas segundo semestre      | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (grade)               | Nota promedio segundo semestre           | Numérica     | 0 - 20                                | Kaggle: Student Dropout Dataset |
| Curricular units 2nd sem (without evaluations) | Materias sin evaluar segundo semestre    | Numérica     | 0 - 10                                | Kaggle: Student Dropout Dataset |
| Unemployment rate                              | Tasa de desempleo nacional               | Numérica     | 0 - 100 (%)                           | Kaggle: Student Dropout Dataset |
| Inflation rate                                 | Tasa de inflación nacional               | Numérica     | 0 - 100 (%)                           | Kaggle: Student Dropout Dataset |
| GDP                                            | Producto Interno Bruto nacional          | Numérica     | 0 - 1,000,000+                        | Kaggle: Student Dropout Dataset |
| Target                                         | Variable objetivo: estado del estudiante | Categórica   | "Dropout", "Graduate", "Enrolled"     | Kaggle: Student Dropout Dataset |


