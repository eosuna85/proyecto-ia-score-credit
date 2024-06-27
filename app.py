from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Cargar el modelo
model = joblib.load('decision_tree_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

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

        return jsonify({'prediction': prediction})
    except KeyError as e:
        return jsonify({'error': f'Missing data: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)