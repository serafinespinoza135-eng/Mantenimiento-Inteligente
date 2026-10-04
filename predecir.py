import joblib
import pandas as pd


# ==========================================
# 1. CARGAR MODELO
# ==========================================

modelo = joblib.load("modelo_riesgo.pkl")

print("==========================================")
print("       MANTENIMIENTO INTELIGENTE")
print("==========================================")
print("Sistema de predicción de mantenimiento")
print()


# ==========================================
# 2. SOLICITAR DATOS
# ==========================================

print("Ingresa los datos de la máquina:\n")

horas_operacion = float(
    input("Horas de operación: ")
)

edad_maquina = float(
    input("Edad de la máquina (años): ")
)

mantenimientos_realizados = float(
    input("Mantenimientos realizados: ")
)

meses_ultimo_mantenimiento = float(
    input("Meses desde el último mantenimiento: ")
)

temperatura = float(
    input("Temperatura de operación (°C): ")
)

vibracion = float(
    input("Nivel de vibración: ")
)

fallas_previas = float(
    input("Fallas previas: ")
)

horas_desde_ultimo_mantenimiento = float(
    input("Horas desde el último mantenimiento: ")
)


# ==========================================
# 3. CREAR DATOS PARA EL MODELO
# ==========================================

datos_maquina = pd.DataFrame([
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


# ==========================================
# 4. REALIZAR PREDICCIÓN
# ==========================================

prediccion = modelo.predict(datos_maquina)

riesgo = prediccion[0]


# ==========================================
# 5. MOSTRAR RESULTADO
# ==========================================

print()
print("==========================================")
print("             RESULTADO")
print("==========================================")

print(f"Riesgo de mantenimiento: {riesgo}")

print("==========================================")