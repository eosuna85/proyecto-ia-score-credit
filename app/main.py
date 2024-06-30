from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np


app = FastAPI()

# Mount the static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Ruta al modelo pickle
model_path = 'app/model/decision_tree_model.pkl'
model = joblib.load(model_path)

# Set up the templates directory
templates = Jinja2Templates(directory="app/templates")

# Definir la ruta raíz para renderizar un template HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para manejar la predicción
@app.post("/predict")
async def predict(request: Request):
    try:
        data = await request.json()

        # Procesar los datos para el modelo
        existing_customer = 1 if data['existingCustomer'] == 'Yes' else 0
        employment_profile = data['employmentProfile']
        
        # Crear el array de características para el modelo
        features = [
            int(data['age']),
            float(data['income']),
            int(data['loanTenure']),
            int(data['profileScore']),
            float(data['ltvRatio']),
            existing_customer,
            1 if employment_profile == 'Freelancer' else 0,
            1 if employment_profile == 'Salaried' else 0,
            1 if employment_profile == 'Self-Employed' else 0,
            1 if employment_profile == 'Student' else 0,
            1 if employment_profile == 'Unemployed' else 0
        ]

        # Realizar la predicción
        prediction = model.predict([features])[0]

        # Retornar el resultado de la predicción como JSON
        return {"prediction": prediction}

    except KeyError as e:
        return {"error": f"Missing data: {str(e)}"}, 400
    except Exception as e:
        return {"error": str(e)}, 500
