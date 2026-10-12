# Daniel Nieves NC=1343
import pandas as pd

# 1. Crear un dataset de ejemplo simular a un CSV
datos = {
    'distancia_km': [2.5, 4.0, 1.2, 5.8, 3.1],
    'trafico_nivel': [1, 3, 1, 3, 2],        # 1: Bajo, 2: Medio, 3: Alto
    'edad_repartidor': [22, 35, 19, 28, 40],
    'tiempo_entrega_min': [15, 32, 10, 42, 25] # Lo que queremos predecir
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))


datos15 = {
    'distancia_km': [1.4, 3.6, 5.4, 2.1, 4.3],
    'trafico_nivel': [1, 3, 2, 1, 3],
    'edad_repartidor': [25, 41, 29, 35, 26],
    'tiempo_entrega_min': [11, 33, 42, 15, 40]
}
print("Daniel Nieves NC=1343")