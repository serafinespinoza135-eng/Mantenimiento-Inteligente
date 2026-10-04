import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ==========================================
# 1. CARGAR DATASET
# ==========================================

dataset = pd.read_csv("dataset_maquinas.csv")

print("Dataset cargado correctamente.")
print(f"Total de registros: {len(dataset)}")


# ==========================================
# 2. SEPARAR VARIABLES
# ==========================================

# Variables que utilizará el modelo
variables_entrada = [
    "horas_operacion",
    "edad_maquina",
    "mantenimientos_realizados",
    "meses_ultimo_mantenimiento",
    "temperatura",
    "vibracion",
    "fallas_previas",
    "horas_desde_ultimo_mantenimiento"
]

# Variable que queremos predecir
variable_objetivo = "riesgo_mantenimiento"

X = dataset[variables_entrada]
y = dataset[variable_objetivo]


# ==========================================
# 3. DIVIDIR DATOS
# ==========================================

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nDatos divididos:")
print(f"Datos de entrenamiento: {len(X_entrenamiento)}")
print(f"Datos de prueba: {len(X_prueba)}")


# ==========================================
# 4. CREAR MODELO
# ==========================================

modelo = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)


# ==========================================
# 5. ENTRENAR MODELO
# ==========================================

print("\nEntrenando modelo...")

modelo.fit(
    X_entrenamiento,
    y_entrenamiento
)

print("Modelo entrenado correctamente.")


# ==========================================
# 6. REALIZAR PREDICCIONES
# ==========================================

predicciones = modelo.predict(X_prueba)


# ==========================================
# 7. EVALUAR MODELO
# ==========================================

precision = accuracy_score(
    y_prueba,
    predicciones
)

print("\n==========================================")
print(" RESULTADOS DEL MODELO")
print("==========================================")

print(f"\nPrecisión: {precision * 100:.2f}%")


print("\nReporte de clasificación:")
print(
    classification_report(
        y_prueba,
        predicciones
    )
)


print("Matriz de confusión:")
print(
    confusion_matrix(
        y_prueba,
        predicciones
    )
)


# ==========================================
# 8. GUARDAR MODELO
# ==========================================

joblib.dump(
    modelo,
    "modelo_riesgo.pkl"
)

print("\n==========================================")
print(" MODELO GUARDADO")
print("==========================================")

print("Archivo generado: modelo_riesgo.pkl")