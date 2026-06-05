from flask import Flask, render_template, request

from src.predict import predecir

app = Flask(__name__)
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
        if resultado >= 50:
            estado = "INTRUCION DETECTADA"
        else:
            estado = "TRAFICO NORMAL"
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