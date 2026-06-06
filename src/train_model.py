# Entrenamiento del modelo de regresion logistica
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression

# Leer dataset
datos = pd.read_csv("data/intrusiones.csv")

# Variables independientes
X = datos[
    [
        "duracion",
        "paquetes",
        "bytes",
        "errores"
    ]
]

# Variable objetivo
y = datos["intrusion"]

# Crear modelo
modelo = LogisticRegression()

# Entrenar modelo
modelo.fit(X, y)

# Guardar modelo entrenado
joblib.dump(
    modelo,
    "models/modelo.pkl"
)

print("Modelo entrenado y guardado correctamente.")