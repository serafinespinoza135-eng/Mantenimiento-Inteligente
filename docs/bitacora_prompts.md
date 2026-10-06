# Bitácora de Prompts — Mantenimiento Inteligente

## 1. Datos generales

**Proyecto:** Mantenimiento Inteligente  
**Rama de Inteligencia Artificial:** Aprendizaje Automático (Machine Learning)  
**Tipo de proyecto:** Clasificación multiclase  
**Lenguaje:** Python  
**Interfaz:** Streamlit  
**Modelo:** Random Forest Classifier  

---

# 2. Objetivo de la bitácora

Esta bitácora registra los prompts utilizados como apoyo durante el desarrollo del proyecto **Mantenimiento Inteligente**.

Los prompts fueron utilizados para obtener orientación sobre la estructura del proyecto, generación de código, creación de datos sintéticos, entrenamiento del modelo, pruebas, interfaz gráfica y documentación.

El código y las propuestas obtenidas mediante Inteligencia Artificial fueron revisados, ejecutados y adaptados por el equipo.

---

# 3. Registro de prompts
# Bitácora de Prompts — Cuestionamientos del proyecto Mantenimiento Inteligente

## 1. Definición del proyecto

**Cuestionamiento:**

> ¿Sobre qué proyecto podemos trabajar para la actividad "Explorando las ramas de la Inteligencia Artificial"?

**Contexto:**  
Se definió trabajar con mantenimiento de máquinas industriales.

---

## 2. Nombre del proyecto

**Cuestionamiento:**

> ¿Qué nombre podemos utilizar para el proyecto de mantenimiento de máquinas industriales?

**Resultado:**  
Se seleccionó el nombre **Mantenimiento Inteligente**.

---

## 3. Rama de Inteligencia Artificial

**Cuestionamiento:**

> ¿Qué rama de Inteligencia Artificial sería adecuada para un proyecto de mantenimiento de máquinas industriales?

**Resultado:**  
Se seleccionó **Aprendizaje Automático (Machine Learning)**.

---

## 4. Resultados del sistema

**Cuestionamiento:**

> ¿Qué resultados puede manejar el sistema para clasificar el riesgo de mantenimiento?

**Resultado:**  
Se definieron tres categorías:

- Bajo
- Medio
- Alto

---

## 5. Variables del proyecto

**Cuestionamiento:**

> ¿Qué variables recomiendas para un sistema de mantenimiento inteligente de máquinas industriales?

**Resultado:**  
Se seleccionaron:

- `horas_operacion`
- `edad_maquina`
- `mantenimientos_realizados`
- `meses_ultimo_mantenimiento`
- `temperatura`
- `vibracion`
- `fallas_previas`
- `horas_desde_ultimo_mantenimiento`

---

## 6. Generación del dataset

**Cuestionamiento:**

> ¿Cómo podemos generar un dataset sintético para el proyecto de mantenimiento de máquinas industriales utilizando las ocho variables seleccionadas y los resultados Bajo, Medio y Alto?

**Resultado:**  
Se generó un dataset sintético de 100 máquinas industriales.

---

## 7. Distribución del dataset

**Cuestionamiento:**

> El dataset generado tiene demasiados registros de riesgo Medio y pocos registros de Bajo. ¿Cómo podemos corregirlo para tener una distribución más equilibrada?

**Resultado:**  
Se ajustó el dataset para obtener:

- Bajo: 33
- Medio: 34
- Alto: 33

---

## 8. Algoritmo de Machine Learning

**Cuestionamiento:**

> ¿Qué algoritmo de aprendizaje automático podemos utilizar para clasificar las máquinas industriales en Bajo, Medio y Alto?

**Resultado:**  
Se seleccionó **Random Forest Classifier**.

---

## 9. Entrenamiento del modelo

**Cuestionamiento:**

> ¿Cómo podemos entrenar un modelo utilizando el dataset de máquinas industriales y las ocho variables seleccionadas?

**Resultado:**  
Se utilizó una división de 80 % para entrenamiento y 20 % para pruebas.

---

## 10. Evaluación del modelo

**Cuestionamiento:**

> ¿Cómo podemos evaluar si el modelo está clasificando correctamente los niveles Bajo, Medio y Alto?

**Resultado:**  
Se utilizaron precisión, reporte de clasificación y matriz de confusión.

---

## 11. Interpretación de la precisión

**Cuestionamiento:**

> El modelo obtuvo una precisión de 100 %. ¿Qué significa este resultado y cómo debemos interpretarlo?

**Resultado:**  
Se determinó que el 100 % corresponde al conjunto de prueba del dataset sintético utilizado para el prototipo y no representa una precisión garantizada sobre máquinas industriales reales.

---

## 12. Predicción de una máquina nueva

**Cuestionamiento:**

> ¿Cómo podemos crear un programa que permita introducir los datos de una máquina y obtener como resultado Bajo, Medio o Alto?

**Resultado:**  
Se desarrolló un programa de predicción utilizando el modelo entrenado.

---

## 13. Casos de prueba

**Cuestionamiento:**

> ¿Qué datos podemos utilizar para probar una máquina con riesgo Bajo, una con riesgo Medio y una con riesgo Alto?

**Resultado:**  
Se definieron tres casos de prueba para comprobar las tres categorías de salida.

---

## 14. Interfaz gráfica

**Cuestionamiento:**

> ¿Cómo podemos crear una interfaz web sencilla para introducir las ocho variables de una máquina industrial y mostrar el nivel de riesgo?

**Resultado:**  
Se seleccionó **Streamlit** para desarrollar la interfaz del prototipo.

---

## 15. Funcionamiento de la interfaz

**Cuestionamiento:**

> ¿Cómo podemos comprobar que la interfaz de Streamlit funciona correctamente con los casos Bajo, Medio y Alto?

**Resultado:**  
Se probaron los tres casos desde la interfaz y los resultados coincidieron con los resultados esperados.

---

## 16. Validación general del prototipo

**Cuestionamiento:**

> ¿El prototipo ya funciona correctamente después de comprobar la generación de datos, entrenamiento, predicción e interfaz?

**Resultado:**  
Se comprobó que el flujo completo funciona correctamente:

```text
Datos
  ↓
Entrenamiento
  ↓
Modelo
  ↓
Entrada de una máquina
  ↓
Predicción
  ↓
Bajo / Medio / Alto
```

---

## Nota

Esta bitácora contiene únicamente los **cuestionamientos relacionados con las decisiones, funcionamiento y desarrollo del proyecto**. No incluye solicitudes de redacción de documentos, archivos, README, comandos de GitHub ni otras tareas administrativas.

