# Pruebas de QA — Mantenimiento Inteligente

**Responsable de QA:** Jesús Alejandro Trujillo Castro
**Fecha de las pruebas:** 04/10/2026
**Versión probada:** rama `main` del repositorio
**Entorno:** Windows, Python 3.12.7 en entorno virtual (`.venv`), navegador web

## 1. Alcance

Se prueba la aplicación web (`app.py`) que recibe 8 variables de una máquina y muestra el riesgo de mantenimiento: **Bajo, Medio o Alto**.

Rangos permitidos por los campos de la aplicación:

| Campo | Mínimo | Máximo |
|---|---|---|
| Horas de operación | 0 | 50000 |
| Edad de la máquina (años) | 0 | 50 |
| Mantenimientos realizados | 0 | 50 |
| Meses desde el último mantenimiento | 0 | 60 |
| Temperatura (°C) | 0 | 150 |
| Nivel de vibración | 0 | 20 |
| Fallas previas | 0 | 30 |
| Horas desde el último mantenimiento | 0 | 10000 |

## 2. Casos de prueba

> Nota: la columna "Resultado esperado" es una hipótesis razonable. Se verifica ejecutando la app; la columna "Resultado obtenido" se llena con lo que realmente aparece.

### 2.1 Instalación y arranque

| ID | Caso | Pasos | Resultado esperado | Resultado obtenido | ¿Pasó? |
|---|---|---|---|---|---|
| QA-01 | Instalación en limpio | Clonar el repo, crear entorno virtual y ejecutar `pip install -r requirements.txt` | Se instalan las dependencias sin errores | Con Python 3.14.7 falló (pandas 2.2.3 no tiene instalador para esa versión y pide compilar con Visual Studio). Con Python 3.12.7 se instaló sin errores | Sí, con Python 3.12 |
| QA-02 | Arranque de la app | Ejecutar `streamlit run app.py` | Se abre la app en `http://localhost:8501` con el título "Mantenimiento Inteligente" | La app abrió en el navegador en `http://localhost:8501` | Sí |

### 2.2 Predicciones

| ID | Caso | Entradas (horas oper. / edad / mant. / meses / temp. / vibración / fallas / horas desde mant.) | Resultado esperado | Resultado obtenido | ¿Pasó? |
|---|---|---|---|---|---|
| QA-03 | Valores por defecto | 5000 / 5 / 4 / 6 / 70 / 4.0 / 1 / 1000 | Muestra una de las tres categorías | Riesgo de mantenimiento: MEDIO | Sí |
| QA-04 | Máquina nueva y bien mantenida | 500 / 1 / 5 / 1 / 55 / 1.5 / 0 / 200 | Riesgo Bajo (tendencia) | Riesgo de mantenimiento: BAJO | Sí |
| QA-05 | Máquina desgastada | 40000 / 20 / 2 / 36 / 120 / 15.0 / 12 / 9000 | Riesgo Alto (tendencia) | Riesgo de mantenimiento: ALTO | Sí |
| QA-06 | Máquina en condición intermedia | 20000 / 10 / 6 / 12 / 85 / 8.0 / 4 / 4000 | Riesgo Medio (tendencia) | Riesgo de mantenimiento: ALTO (distinto de la hipótesis inicial, que era Medio; ver E-02) | No |
| QA-07 | Todos los valores en el mínimo | 0 / 0 / 0 / 0 / 0 / 0 / 0 / 0 | La app responde con una categoría sin errores | Riesgo de mantenimiento: BAJO, sin errores | Sí |
| QA-08 | Todos los valores en el máximo | 50000 / 50 / 50 / 60 / 150 / 20 / 30 / 10000 | La app responde con una categoría sin errores | Riesgo de mantenimiento: ALTO, sin errores; muestra el mensaje de revisión recomendada | Sí |
| QA-09 | Repetir la misma entrada | Repetir QA-03 tres veces | Siempre el mismo resultado | Riesgo de mantenimiento: MEDIO, igual que en QA-03 | Sí |

### 2.3 Validación de entradas

| ID | Caso | Pasos | Resultado esperado | Resultado obtenido | ¿Pasó? |
|---|---|---|---|---|---|
| QA-10 | Valor negativo | Escribir -5 en "Horas de operación" | El campo no acepta el valor o lo ajusta al mínimo | El campo muestra el mensaje "El valor debe ser superior o igual a 0" y no acepta el valor | Sí |
| QA-11 | Valor sobre el máximo | Escribir 60000 en "Horas de operación" | El campo no acepta el valor o lo ajusta al máximo | El campo muestra el mensaje "El valor debe ser inferior o igual a 50000" y no acepta el valor | Sí |
| QA-12 | Decimal en campo entero | Escribir 2.5 en "Fallas previas" | El campo no acepta el decimal | Aparece el aviso "Press Enter to apply" y, al aplicar, el valor 2.5 se convierte en 2 | Sí |
| QA-13 | Campo vacío | Borrar el contenido de un campo y pulsar el botón | La app no se rompe | Al borrar el contenido, el campo recupera automáticamente un valor y la app no se rompe | Sí |
| QA-14 | Sin pulsar el botón | Cambiar valores sin pulsar "Predecir" | No se muestra resultado nuevo hasta pulsar el botón | El resultado no cambia hasta pulsar el botón | Sí |

### 2.4 Interfaz

| ID | Caso | Pasos | Resultado esperado | Resultado obtenido | ¿Pasó? |
|---|---|---|---|---|---|
| QA-15 | Colores y mensajes | Obtener un resultado de cada categoría | Bajo en verde, Medio en amarillo, Alto en rojo, con su mensaje | Los tres niveles se muestran con su color (Bajo verde, Medio amarillo, Alto rojo) y su mensaje | Sí |

## 3. Errores encontrados y corregidos

| ID | Descripción del error | Caso donde se detectó | Cómo se corrigió | Estado |
|---|---|---|---|---|
| E-01 | La instalación falla con Python 3.14.7: `pandas==2.2.3` no tiene instalador para esa versión y pip intenta compilarlo, lo que exige Visual Studio | QA-01 | Se creó un entorno virtual con Python 3.12.7 y la instalación funcionó | Resuelto en el entorno de pruebas. Pendiente: actualizar la documentación, que dice "Python 3.10 o superior", a "3.10 a 3.13" |
| E-02 | Con las entradas de QA-06 (20000 / 10 / 6 / 12 / 85 / 8.0 / 4 / 4000) el modelo responde ALTO, y la hipótesis inicial era MEDIO. No es un fallo confirmado: el resultado esperado era una estimación | QA-06 | Sin corrección: se informa al desarrollador principal para que revise si el criterio del modelo es el deseado | Observación abierta, pendiente de revisión por el desarrollador |
| E-03 | Los campos numéricos muestran el aviso "Press Enter to apply" en inglés, mientras el resto de la interfaz está en español | QA-12 | Sin corrección: es un texto propio de Streamlit | Menor, sin corregir |

(Si no se encontraron errores, escribir "Sin errores encontrados" y la fecha.)

## 4. Conclusión

Se ejecutaron los 15 casos de prueba. **14 pasaron** y **1 no coincidió** con lo esperado (QA-06, ver E-02). Hallazgos principales:

- La instalación falla con Python 3.14 y funciona con Python 3.12 (E-01). Se recomienda indicar en la documentación "Python 3.10 a 3.13".
- Los campos rechazan valores fuera de rango con su mensaje y manejan decimales y campos vacíos sin romper la aplicación.
- La aplicación funciona correctamente en el entorno probado (Windows, Python 3.12.7). Quedan dos observaciones menores para el equipo (E-02 y E-03).