
Sistema de Detección de Intrusiones

Descripción

Aplicación web desarrollada con Flask y Regresión Logística para detectar posibles intrusiones en tráfico de red.

Las variables utilizadas son:

- Duración
- Paquetes
- Bytes
- Errores

La salida del sistema es una probabilidad de intrusión y una clasificación del tráfico como normal o intrusivo.

Tecnologías utilizadas

- Python 3
- Flask
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- HTML
- CSS

Instalación

Clonar el repositorio:

git clone URL_DEL_REPOSITORIO

Entrar al proyecto:

cd SistemaDeteccion

Crear entorno virtual:

python -m venv venv

Activar entorno virtual:

Windows:

venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

Entrenamiento del modelo

python src/train_model.py

Ejecución de la aplicación

python app.py

Abrir en el navegador:

http://127.0.0.1:5000

Autor

Jhon
# SistemaDeteccion
Sistema web de detección de intrusiones usando Regresión Logística y Flask.
