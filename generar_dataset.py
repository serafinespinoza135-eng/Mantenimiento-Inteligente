import random
import pandas as pd


def generar_maquina(id_maquina, riesgo):
    """
    Genera los datos de una máquina industrial según
    el nivel de riesgo especificado.
    """

    if riesgo == "Bajo":
        horas_operacion = random.randint(500, 4500)
        edad_maquina = random.randint(1, 5)
        mantenimientos_realizados = random.randint(3, 8)
        meses_ultimo_mantenimiento = random.randint(1, 5)
        temperatura = round(random.uniform(50, 72), 2)
        vibracion = round(random.uniform(1, 4), 2)
        fallas_previas = random.randint(0, 1)
        horas_desde_ultimo_mantenimiento = random.randint(100, 900)

    elif riesgo == "Medio":
        horas_operacion = random.randint(3500, 9000)
        edad_maquina = random.randint(3, 9)
        mantenimientos_realizados = random.randint(2, 6)
        meses_ultimo_mantenimiento = random.randint(4, 10)
        temperatura = round(random.uniform(65, 85), 2)
        vibracion = round(random.uniform(3.5, 7), 2)
        fallas_previas = random.randint(1, 3)
        horas_desde_ultimo_mantenimiento = random.randint(700, 1800)

    else:  # Alto
        horas_operacion = random.randint(8000, 15000)
        edad_maquina = random.randint(7, 15)
        mantenimientos_realizados = random.randint(0, 3)
        meses_ultimo_mantenimiento = random.randint(9, 18)
        temperatura = round(random.uniform(80, 100), 2)
        vibracion = round(random.uniform(6.5, 10), 2)
        fallas_previas = random.randint(3, 6)
        horas_desde_ultimo_mantenimiento = random.randint(1600, 3000)

    return {
        "id_maquina": id_maquina,
        "horas_operacion": horas_operacion,
        "edad_maquina": edad_maquina,
        "mantenimientos_realizados": mantenimientos_realizados,
        "meses_ultimo_mantenimiento": meses_ultimo_mantenimiento,
        "temperatura": temperatura,
        "vibracion": vibracion,
        "fallas_previas": fallas_previas,
        "horas_desde_ultimo_mantenimiento": horas_desde_ultimo_mantenimiento,
        "riesgo_mantenimiento": riesgo
    }


def generar_dataset():
    """
    Genera un dataset sintético equilibrado de 100 máquinas.
    """

    datos = []

    # 33 máquinas con riesgo bajo
    for i in range(1, 34):
        datos.append(
            generar_maquina(f"M{i:03d}", "Bajo")
        )

    # 34 máquinas con riesgo medio
    for i in range(34, 68):
        datos.append(
            generar_maquina(f"M{i:03d}", "Medio")
        )

    # 33 máquinas con riesgo alto
    for i in range(68, 101):
        datos.append(
            generar_maquina(f"M{i:03d}", "Alto")
        )

    # Mezclar los registros para que las categorías
    # no aparezcan agrupadas por orden.
    random.shuffle(datos)

    return pd.DataFrame(datos)


if __name__ == "__main__":

    dataset = generar_dataset()

    dataset.to_csv(
        "dataset_maquinas.csv",
        index=False,
        encoding="utf-8"
    )

    print("======================================")
    print(" DATASET GENERADO CORRECTAMENTE")
    print("======================================")

    print(f"\nTotal de máquinas: {len(dataset)}")

    print("\nDistribución de riesgos:")
    print(
        dataset["riesgo_mantenimiento"]
        .value_counts()
        .sort_index()
    )

    print("\nPrimeros registros:")
    print(dataset.head())

    print("\nArchivo generado:")
    print("dataset_maquinas.csv")