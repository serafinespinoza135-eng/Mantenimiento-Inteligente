import streamlit as st
import pandas as pd
import joblib


# ==========================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ==========================================

st.set_page_config(
    page_title="Mantenimiento Inteligente",
    page_icon="🔧",
    layout="centered"
)


# ==========================================
# CARGAR MODELO
# ==========================================

@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_riesgo.pkl")


modelo = cargar_modelo()


# ==========================================
# TÍTULO
# ==========================================

st.title("🔧 Mantenimiento Inteligente")

st.write(
    "Sistema de predicción del riesgo de mantenimiento "
    "para máquinas industriales mediante Machine Learning."
)

st.divider()


# ==========================================
# DATOS DE LA MÁQUINA
# ==========================================

st.subheader("Datos de la máquina")

horas_operacion = st.number_input(
    "Horas de operación",
    min_value=0,
    max_value=50000,
    value=5000,
    step=100
)

edad_maquina = st.number_input(
    "Edad de la máquina (años)",
    min_value=0,
    max_value=50,
    value=5,
    step=1
)

mantenimientos_realizados = st.number_input(
    "Mantenimientos realizados",
    min_value=0,
    max_value=50,
    value=4,
    step=1
)

meses_ultimo_mantenimiento = st.number_input(
    "Meses desde el último mantenimiento",
    min_value=0,
    max_value=60,
    value=6,
    step=1
)

temperatura = st.number_input(
    "Temperatura de operación (°C)",
    min_value=0.0,
    max_value=150.0,
    value=70.0,
    step=0.5
)

vibracion = st.number_input(
    "Nivel de vibración",
    min_value=0.0,
    max_value=20.0,
    value=4.0,
    step=0.1
)

fallas_previas = st.number_input(
    "Fallas previas",
    min_value=0,
    max_value=30,
    value=1,
    step=1
)

horas_desde_ultimo_mantenimiento = st.number_input(
    "Horas desde el último mantenimiento",
    min_value=0,
    max_value=10000,
    value=1000,
    step=100
)


# ==========================================
# PREDICCIÓN
# ==========================================

st.divider()

if st.button(
    "🔍 Predecir riesgo de mantenimiento",
    use_container_width=True
):

    # Crear DataFrame con los datos introducidos
    datos = pd.DataFrame([
        {
            "horas_operacion": horas_operacion,
            "edad_maquina": edad_maquina,
            "mantenimientos_realizados": mantenimientos_realizados,
            "meses_ultimo_mantenimiento": meses_ultimo_mantenimiento,
            "temperatura": temperatura,
            "vibracion": vibracion,
            "fallas_previas": fallas_previas,
            "horas_desde_ultimo_mantenimiento":
                horas_desde_ultimo_mantenimiento
        }
    ])

    # Realizar predicción
    prediccion = modelo.predict(datos)[0]

    # ==========================================
    # MOSTRAR RESULTADO
    # ==========================================

    st.subheader("Resultado")

    if prediccion == "Bajo":

        st.success(
            "🟢 Riesgo de mantenimiento: BAJO"
        )

        st.write(
            "La máquina presenta características asociadas "
            "con un nivel bajo de riesgo de mantenimiento."
        )

    elif prediccion == "Medio":

        st.warning(
            "🟡 Riesgo de mantenimiento: MEDIO"
        )

        st.write(
            "La máquina presenta características que "
            "sugieren que debe considerarse una revisión."
        )

    else:

        st.error(
            "🔴 Riesgo de mantenimiento: ALTO"
        )

        st.write(
            "La máquina presenta características asociadas "
            "con un nivel alto de riesgo de mantenimiento. "
            "Se recomienda considerar una revisión."
        )