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

## Rama de IA 
El proyecto utiliza Inteligencia Artificial mediante técnicas de Machine Learning para predecir el nivel de riesgo de mantenimiento de una máquina industrial.

El modelo analiza diferentes características relacionadas con el funcionamiento y el historial de la máquina, como las horas de uso, temperatura, vibración y número de fallas previas. A partir de estos datos, el sistema determina un nivel de riesgo de mantenimiento.

Los niveles de riesgo considerados por el sistema son:

- BAJO: la máquina presenta condiciones        normales  y un riesgo reducido.
- MEDIO: existen condiciones que requieren atención y seguimiento.
- ALTO: existe un riesgo elevado y se recomienda realizar una revisión o mantenimiento.

El modelo de Machine Learning se entrena utilizando un conjunto de datos de máquinas industriales y posteriormente se utiliza para realizar predicciones sobre nuevos datos.

## CASO DE USO 

El sistema está diseñado para apoyar el mantenimiento preventivo de máquinas industriales.

Por ejemplo, un responsable de mantenimiento puede introducir información de una máquina, como:

- Horas de uso. 
- Temperatura.
- Nivel de vibración.
- Número de fallas previas.

Con estos datos, el sistema genera una predicción del nivel de riesgo de mantenimiento.

Esto permite identificar máquinas que podrían requerir atención antes de que ocurra una falla grave, ayudando a reducir tiempos de inactividad y posibles costos de reparación.

## Flujo de sistema 

1. Se recopilan los datos de las máquinas.
2. Se genera o prepara el conjunto de datos.
3. Se entrena el modelo de Machine Learning.
4. El modelo aprende patrones relacionados con   el riesgo de mantenimiento.
5. El usuario proporciona los datos de una máquina.
6. El sistema procesa la información.
7. El modelo genera una predicción.
8. Se muestra el nivel de riesgo de mantenimiento

## Requisitos 

**Para ejecutar el proyecto se necesita:**

- Python 3.10 a 3.13.
- Git.
- Las dependencias especificadas en **requirements.txt**

## INSTALACIÓN 

Clonar el repositorio:

git clone https://github.com/serafinespinoza135-eng/Mantenimiento-Inteligente.git

Entrar al proyecto:

cd Mantenimiento-Inteligente

Crear un entorno virtual:

python -m venv .venv

Activar el entorno virtual en Windows:

.venv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt

Después de instalar las dependencias, se puede ejecutar la aplicación siguiendo las instrucciones indicadas en este README.

## FUENTES

- Python Software Foundation. (s. f.). *Python documentation.* https://docs.python.org/3/
- scikit-learn developers. (s. f.). *scikit-learn: Machine Learning in Python* https://scikit-learn.org/
- pandas development team. (s. f.). *pandas documentation.* https://pandas.pydata.org/docs/
- NumPy developers. (s. f.). *NumPy documentation.* https://numpy.org/doc/
- GitHub. (s. f.). *GitHub documentation.* https://docs.github.com/ 


