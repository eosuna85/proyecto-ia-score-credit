# Nombre del Proyecto: “Score Credit IA: Aplicación de la IA para la Asignación Rápida y Segura de Créditos por Medio del Score Crediticio”

## Descripción
Desarrollar un sistema que incorpore la inteligencia artificial para identificar usuarios de forma rápida y segura, sujetos aptos para el crédito.

## Objetivos del Problema
- **Desarrollar un modelo de inteligencia artificial:** Analizar el historial financiero y de transacciones de los usuarios.
- **Entrenar el modelo:** Utilizar datos históricos de crédito del usuario y posible riesgo de crédito.
- **Implementar el modelo:** Crear un sistema automatizado que pueda procesar las solicitudes de crédito en tiempo real.
- **Evaluar el rendimiento:** Medir precisión, sensibilidad y especificidad en la detección de fraudes en las solicitudes de crédito.

## Antecedentes
Este proyecto es parte del trabajo grupal de Inteligencia Artificial en la formación de "Tecnólogas sin Experiencia en IA" del programa Mil Mujeres IA.

## Características
- **Exploración de Datos:** Análisis inicial de los datos para comprender su estructura y características.
- **Modelado:** Creación y entrenamiento del modelo de inteligencia artificial utilizando algoritmos de aprendizaje supervisado.
    link Notebook:https://colab.research.google.com/drive/1azy8Y43SFtTsQgd7iL8x1RTmz-tOQxM9
- **Despliegue de API:** Implementación de un servicio web para el procesamiento de solicitudes de crédito en tiempo real a través de una API construida con FastAPI.

## Tecnologías Utilizadas
- **Lenguaje de Programación:** Python
- **Frameworks y Librerías:** 
  - FastAPI
  - Scikit-learn
  - Pandas
  - Numpy
  - Joblib
- **Entorno de Desarrollo:** 
  - Google Colab
  - Visual Studio Code

## Instalación y Configuración
1. Clona el repositorio:
    ```sh
    git clone https://github.com/eosuna85/proyecto-ia-score-credit
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd proyecto-ia-score-credit
    ```
3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso
1. Entrena el modelo ejecutando el script `train_model.py`.
2. Inicia el servidor FastAPI:
    ```sh
    uvicorn main:app --reload
    ```
3. Accede a la API en `http://127.0.0.1:8000`.

## Estructura del Proyecto
    proyecto-ia-score-credit/
    ├── .venv/
    ├── app/
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── main.py
    │   ├── model/
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   └── decision_tree_model.pkl
    │   ├── templates/
    │   │   └── index.html
    │   └── static/
    │       ├── css/
    │       │   └── styles.css
    │       └── js/
    │           └── script.js
    └── requirements.txt



## Colaboradores

- Nombre del contacto: Evelyn Marrero
- Email: alemusita@hotmail.com

- Nombre del contacto: Claudia Acosta
- Email: evelyn.mar54@gmail.com

- Nombre del contacto: Erika Osuna
- Email: erika.osuna85@gmail.com

