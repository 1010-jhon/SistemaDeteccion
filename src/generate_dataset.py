# Generacion del dataset sintetico para deteccion de intrucciones 
import pandas as pd
import random

datos = []

# Generacion de trafico normal
for _ in range(700):
    datos.append([
        random.randint(5, 30),        # duración
        random.randint(50, 300),      # paquetes
        random.randint(500, 10000),   # bytes
        random.randint(0, 1),         # errores
        0                             # normal
    ])

# Generacion de trafico de intrusiones
for _ in range(300):
    datos.append([
        random.randint(1, 15),         # duración
        random.randint(400, 1000),     # paquetes
        random.randint(20000, 80000),  # bytes
        random.randint(2, 10),         # errores
        1                              # intrusión
    ])

df = pd.DataFrame(
    datos,
    columns=[
        "duracion",
        "paquetes",
        "bytes",
        "errores",
        "intrusion"
    ]
)
# Mezclar registros aleatoriamente
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(
    "data/intrusiones.csv",
    index=False
)

print("Dataset generado correctamente.")