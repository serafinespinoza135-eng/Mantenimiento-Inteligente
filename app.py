
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib


# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(
    page_title="Mantenimiento Inteligente",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==========================================
# EFECTO GLOBAL DEL CURSOR
# ==========================================

components.html("""
<script>
(function () {
    try {
        const doc = window.parent.document;
        const win = window.parent;

        if (doc.getElementById("global-cursor-glow")) {
            return;
        }

        const style = doc.createElement("style");

        style.textContent = `
            #global-cursor-glow {
                position: fixed;
                width: 380px;
                height: 380px;
                left: 0;
                top: 0;
                border-radius: 50%;
                pointer-events: none;
                z-index: 999;
                opacity: 0;

                background: radial-gradient(
                    circle,
                    rgba(80, 165, 220, 0.28) 0%,
                    rgba(57, 127, 182, 0.13) 35%,
                    transparent 70%
                );

                filter: blur(18px);
                transition: opacity 0.35s ease;
                will-change: transform;
            }

            @media (pointer: coarse),
                   (prefers-reduced-motion: reduce) {
                #global-cursor-glow {
                    display: none !important;
                }
            }
        `;

        doc.head.appendChild(style);

        const glow = doc.createElement("div");
        glow.id = "global-cursor-glow";
        doc.body.appendChild(glow);

        let mouseX = -500;
        let mouseY = -500;
        let currentX = -500;
        let currentY = -500;

        const reducedMotion = win.matchMedia(
            "(prefers-reduced-motion: reduce)"
        );

        const coarsePointer = win.matchMedia(
            "(pointer: coarse)"
        );

        doc.addEventListener("pointermove", function (event) {
            if (
                event.pointerType !== "mouse" ||
                reducedMotion.matches ||
                coarsePointer.matches
            ) {
                return;
            }

            mouseX = event.clientX;
            mouseY = event.clientY;
            glow.style.opacity = "1";
        });

        doc.addEventListener("pointerout", function (event) {
            if (!event.relatedTarget) {
                glow.style.opacity = "0";
            }
        });

        function animate() {
            currentX += (mouseX - currentX) * 0.10;
            currentY += (mouseY - currentY) * 0.10;

            glow.style.transform =
                "translate(" +
                (currentX - 190) + "px, " +
                (currentY - 190) + "px)";

            win.requestAnimationFrame(animate);
        }

        animate();

    } catch (error) {
        console.warn("Error en el efecto del cursor:", error);
    }
})();
</script>
""", height=0, scrolling=False)


# ==========================================
# ESTILOS INDUSTRIALES
# ==========================================

st.markdown("""
<style>

/* FONDO GENERAL */

.stApp {
    background:
        radial-gradient(
            ellipse at 90% 0%,
            rgba(36, 67, 99, 0.18),
            transparent 45%
        ),
        #0C1420;
    color: #E2E8F0;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #F1F5F9 !important;
    letter-spacing: -0.5px;
}

p {
    line-height: 1.65;
}

/* ENCABEZADO */

.header-panel {
    background: linear-gradient(
        115deg,
        #18283B,
        #111D2C
    );
    border: 1px solid #30445A;
    border-left: 4px solid #568AB7;
    border-radius: 12px;
    padding: 30px 34px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.6s ease-out both;
}

.header-panel::after {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    right: -110px;
    top: -145px;
    border: 1px solid rgba(134, 166, 196, 0.15);
    border-radius: 50%;
    pointer-events: none;
}

.header-eyebrow {
    font-size: 11px;
    font-weight: 700;
    color: #8CB7D9;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 12px;
}

.header-title {
    font-size: clamp(27px, 3.5vw, 36px);
    font-weight: 700;
    letter-spacing: -1px;
    color: #F1F5F9;
}

.header-description {
    color: #A3B4C8;
    font-size: 14px;
    margin-top: 12px;
    max-width: 650px;
}

/* SECCIONES */

.section-heading {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 28px 0 15px;
}

.section-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 30px;
    height: 30px;
    background: #21374B;
    border: 1px solid #35536C;
    color: #9CC2E0;
    border-radius: 7px;
    font-size: 12px;
    font-weight: 700;
}

.section-title {
    color: #E5EDF5;
    font-weight: 650;
    font-size: 18px;
}

/* CONTENEDORES */

[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
    transition:
        border-color 0.3s ease,
        box-shadow 0.3s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #42617E;
}

/* CAMPOS */

[data-testid="stWidgetLabel"] p {
    color: #B8C8DA;
    font-size: 13px;
    font-weight: 500;
}

[data-testid="stNumberInput"] input {
    background-color: #172638;
    color: #F1F5F9;
    font-weight: 500;
    border-radius: 7px;
    transition:
        background-color 0.25s ease,
        box-shadow 0.25s ease;
}

[data-testid="stNumberInput"] input:focus {
    background-color: #1C3046;
    box-shadow: 0 0 0 2px rgba(91, 145, 189, 0.20);
}

[data-testid="stNumberInput"] button {
    transition: background-color 0.2s ease;
}

[data-testid="stNumberInput"] button:hover {
    background-color: #2A425A;
}

/* BOTÓN PRINCIPAL */

div.stButton > button {
    background: linear-gradient(
        110deg,
        #315D83,
        #416F98
    );
    color: #FFFFFF;
    border: 1px solid #5983A5;
    border-radius: 8px;
    min-height: 52px;
    font-weight: 650;
    font-size: 14px;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

div.stButton > button:hover {
    background: linear-gradient(
        110deg,
        #416F98,
        #5182AB
    );
    color: #FFFFFF;
    border-color: #7198B9;
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
}

div.stButton > button:active {
    transform: translateY(0) scale(0.995);
}

/* RESULTADOS */

[data-testid="stAlert"] {
    border-radius: 10px;
    padding: 20px;
    border-width: 1px;
    animation: resultEntry 0.5s ease-out both;
}

/* SEPARADORES */

hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        #34495E,
        transparent
    );
    margin: 25px 0;
}

/* PIE DE PÁGINA */

.footer-panel {
    margin-top: 45px;
    padding: 25px 20px;
    border-top: 1px solid #293D50;
    color: #91A8BD;
    font-size: 12px;
    text-align: center;
    letter-spacing: 0.2px;
}

.footer-description {
    margin-top: 8px;
    color: #647C93;
    font-size: 11px;
}

/* ANIMACIONES */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes resultEntry {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ACCESIBILIDAD */

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation: none !important;
        transition: none !important;
    }
}

/* RESPONSIVO */

@media (max-width: 768px) {
    .block-container {
        padding-top: 1rem;
    }

    .header-panel {
        padding: 22px;
    }

    .header-title {
        font-size: 26px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# CARGA DEL MODELO ORIGINAL
# ==========================================

@st.cache_resource
def cargar_modelo():
    return joblib.load("modelo_riesgo.pkl")


modelo = cargar_modelo()


# ==========================================
# ENCABEZADO
# ==========================================

st.markdown("""
<div class="header-panel">
<div class="header-eyebrow">SISTEMA DE ANÁLISIS PREDICTIVO</div>
<div class="header-title">Mantenimiento Inteligente</div>
<div class="header-description">
Evaluación del riesgo de mantenimiento en maquinaria industrial mediante técnicas de Machine Learning.
</div>
</div>
""", unsafe_allow_html=True)

st.write(
    "Ingrese los datos de operación del equipo "
    "para realizar la evaluación de riesgo."
)


# ==========================================
# INFORMACIÓN GENERAL
# ==========================================

st.markdown("""
<div class="section-heading">
<span class="section-number">01</span>
<span class="section-title">Información general del equipo</span>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    col1, col2 = st.columns(2, gap="large")

    with col1:
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

    with col2:
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


# ==========================================
# CONDICIONES DE OPERACIÓN
# ==========================================

st.markdown("""
<div class="section-heading">
<span class="section-number">02</span>
<span class="section-title">Condiciones de operación</span>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    col3, col4 = st.columns(2, gap="large")

    with col3:
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

    with col4:
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
# EVALUACIÓN DE RIESGO
# ==========================================

st.markdown("""
<div class="section-heading">
<span class="section-number">03</span>
<span class="section-title">Evaluación de riesgo</span>
</div>
""", unsafe_allow_html=True)

st.write(
    "Una vez registrados los parámetros, "
    "puede realizar la evaluación del equipo."
)

if st.button(
    "Evaluar riesgo de mantenimiento",
    type="primary",
    use_container_width=True
):

    # Datos originales para el modelo
    datos = pd.DataFrame([{
        "horas_operacion": horas_operacion,
        "edad_maquina": edad_maquina,
        "mantenimientos_realizados": mantenimientos_realizados,
        "meses_ultimo_mantenimiento":
            meses_ultimo_mantenimiento,
        "temperatura": temperatura,
        "vibracion": vibracion,
        "fallas_previas": fallas_previas,
        "horas_desde_ultimo_mantenimiento":
            horas_desde_ultimo_mantenimiento
    }])

    # Predicción original
    prediccion = modelo.predict(datos)[0]

    st.markdown("""
<div class="section-heading">
<span class="section-number">04</span>
<span class="section-title">Resultado de la evaluación</span>
</div>
""", unsafe_allow_html=True)

    if prediccion == "Bajo":
        st.success("Nivel de riesgo: BAJO")
        st.write(
            "Las condiciones registradas indican un riesgo bajo. "
            "Se recomienda continuar con el mantenimiento programado."
        )

    elif prediccion == "Medio":
        st.warning("Nivel de riesgo: MEDIO")
        st.write(
            "Se identificaron condiciones que requieren seguimiento. "
            "Es recomendable programar una revisión del equipo."
        )

    else:
        st.error("Nivel de riesgo: ALTO")
        st.write(
            "Las condiciones registradas indican un riesgo elevado. "
            "Se recomienda realizar una inspección técnica."
        )


# ==========================================
# PIE DE PÁGINA CORREGIDO
# ==========================================

st.markdown("""
<div class="footer-panel">
<div>Mantenimiento Inteligente | Sistema de evaluación predictiva de maquinaria</div>
<div class="footer-description">Prototipo académico de análisis de riesgo</div>
</div>
""", unsafe_allow_html=True)
