# Prueba en limpio - Alan de la Luz Guillermo

## Entorno utilizado

- Sistema: Ubuntu 26.04 LTS
- Python utilizado: 3.12.15
- Entorno virtual: `.venv`

## Instalación

Se clonó el repositorio en una carpeta nueva y se creó un entorno virtual utilizando Python 3.12.

Las dependencias se instalaron correctamente mediante:

```bash
pip install -r requirements.txt

La instalación finalizó correctamente.
Ejecución
La aplicación se ejecutó mediante:
streamlit run app.py

La aplicación abrió correctamente en el navegador mediante Streamlit y la interfaz de Mantenimiento Inteligente funcionó correctamente.
Prueba QA-06
Se probaron los valores indicados para el caso QA-06:
- Vibración: 8.0
- Fallas previas: 4
- Horas de operación: 5000
- Edad de la máquina: 5 años
- Mantenimientos realizados: 4
- Meses desde el último mantenimiento: 6
- Temperatura: 70 °C
- Horas desde el último mantenimiento: 1000
Resultado obtenido
El modelo clasificó el riesgo de mantenimiento como:
MEDIO
El resultado obtenido fue diferente al hallazgo reportado inicialmente por QA, donde se había indicado que el resultado era ALTO. La prueba fue realizada nuevamente en un entorno limpio con Python 3.12.15 y el resultado obtenido fue MEDIO.
Conclusión
La instalación y ejecución del proyecto fueron correctas utilizando Python 3.12.15. El caso QA-06 fue reproducido y el modelo obtuvo el resultado MEDIO, por lo que no se realizaron modificaciones al modelo.
