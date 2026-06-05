import joblib

modelo = joblib.load(
    "models/modelo.pkl"
)

def predecir(
    duracion,
    paquetes,
    bytes_,
    errores
):

    datos = [[
        duracion,
        paquetes,
        bytes_,
        errores
    ]]

    probabilidad = modelo.predict_proba(
        datos
    )[0][1]

    return probabilidad