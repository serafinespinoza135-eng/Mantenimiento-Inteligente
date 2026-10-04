## Problemática

En las máquinas industriales pueden presentarse fallas debido al uso constante, el desgaste de los componentes o la falta de mantenimiento. Cuando estos problemas no se detectan a tiempo pueden provocar paros inesperados, gastos de reparación y pérdida de tiempo.

El mantenimiento predictivo busca utilizar información sobre el funcionamiento de los equipos para detectar señales que indiquen un posible problema antes de que ocurra una falla. Algunos datos que pueden ayudar son las horas de operación, la temperatura, la vibración y el historial de fallas de la máquina.

Por esta razón, en este proyecto se busca utilizar datos de una máquina para estimar su nivel de riesgo y ayudar a identificar cuándo sería conveniente realizar una revisión.

## Descripción del proyecto

**Mantenimiento Inteligente** es un prototipo desarrollado en Python que permite estimar el riesgo de mantenimiento de una máquina industrial.

El usuario introduce información como las horas de operación, edad de la máquina, mantenimientos realizados, temperatura, vibración y fallas previas. Con estos datos, el sistema utiliza un modelo de aprendizaje automático para clasificar el riesgo de mantenimiento como **bajo, medio o alto**.

La aplicación fue desarrollada con Streamlit para facilitar el ingreso de los datos y mostrar el resultado de manera sencilla. El proyecto utiliza un dataset sintético creado por el equipo, por lo que su objetivo es académico y no sustituye una evaluación técnica realizada directamente sobre maquinaria industrial.

## Fuentes

- IBM. *¿Qué es el mantenimiento predictivo?*  
  https://www.ibm.com/mx-es/think/topics/predictive-maintenance

- Amazon Web Services. *What is Predictive Maintenance?*  
  https://aws.amazon.com/what-is/predictive-maintenance/
## Créditos y licencias

### Librerías utilizadas

El proyecto utiliza las siguientes librerías de código abierto:

- **Python** — Lenguaje de programación utilizado para el desarrollo del sistema.
- **Pandas** — Utilizada para la lectura, generación y manipulación de los datos.
- **NumPy** — Utilizada para operaciones y generación de datos numéricos.
- **Scikit-learn** — Utilizada para el entrenamiento, evaluación y predicción del modelo de Machine Learning.
- **Streamlit** — Utilizada para desarrollar la interfaz web del sistema.

Las versiones específicas de las librerías utilizadas se encuentran en el archivo `requirements.txt`.

### Dataset

El dataset utilizado en el proyecto es **sintético**, generado por el propio equipo mediante Python. No contiene información de máquinas industriales reales ni datos personales.

Archivo utilizado:

`dataset_maquinas.csv`

### Modelo

El modelo de Machine Learning fue desarrollado y entrenado por el equipo utilizando **Random Forest Classifier** mediante Scikit-learn.

Archivo generado:

`modelo_riesgo.pkl`

### Uso de Inteligencia Artificial generativa

Durante el desarrollo se utilizó Inteligencia Artificial generativa como herramienta de apoyo para:

- Proponer estructuras de código.
- Generar ejemplos y funciones.
- Apoyar en la creación del dataset sintético.
- Explicar errores y proporcionar alternativas de solución.
- Apoyar en la documentación del proyecto.

El código fue revisado, ejecutado, probado y adaptado por el equipo. Las decisiones sobre la problemática, variables, resultados, pruebas y funcionamiento final fueron realizadas por los integrantes del proyecto.

### Licencias

Las librerías utilizadas son dependencias de código abierto y se utilizan de acuerdo con sus respectivas licencias.

Las licencias y condiciones de uso de las dependencias deben consultarse en sus respectivos proyectos oficiales.

El código desarrollado específicamente para **Mantenimiento Inteligente** corresponde al trabajo del equipo.
