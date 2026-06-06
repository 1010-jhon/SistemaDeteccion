# Aplicaion web para deteccion de intrusiones 
from flask import Flask, render_template, request

from src.predict import predecir
# Crear aplicacion Flask
app = Flask(__name__)
# Historial de predicciones realizadas
historial = []

@app.route("/", methods=["GET", "POST"])
def inicio():

    resultado = None
    estado = None

    if request.method == "POST":

        duracion = float(
            request.form["duracion"]
        )

        paquetes = float(
            request.form["paquetes"]
        )

        bytes_ = float(
            request.form["bytes"]
        )

        errores = float(
            request.form["errores"]
        )
        # Realizar la prediccion
        probabilidad = predecir(
            duracion,
            paquetes,
            bytes_,
            errores
        )

        resultado = round(
            probabilidad * 100,
            2
        )
        # Clasificar trafico
        if resultado >= 50:
            estado = "INTRUCION DETECTADA"
        else:
            estado = "TRAFICO NORMAL"
        # Guardar historial
        historial.append({
        "duracion": duracion,
        "paquetes": paquetes,
        "bytes": bytes_,
        "errores": errores,
        "probabilidad": resultado,
        "estado": estado
})

    return render_template(
        "index.html",
        resultado=resultado,
        estado=estado,
        historial=historial
    )

if __name__ == "__main__":
    app.run(debug=True)