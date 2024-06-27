document.getElementById('predictionForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const employmentProfile = document.getElementById('employmentProfile');
    if (employmentProfile.value === "") {
        alert("Por favor, seleccione un perfil de empleo válido.");
        return;  // Detiene el envío del formulario si no se ha seleccionado una opción válida
    }

    const formData = new FormData(event.target);
    const formObject = Object.fromEntries(formData.entries());

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formObject)
    })
    .then(response => response.json())
    .then(data => {
        const resultElement = document.getElementById('predictionResult');
        if (data.prediction) {
            resultElement.textContent = `Predicted Credit Score: ${data.prediction}`;
        } else if (data.error) {
            resultElement.textContent = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        const resultElement = document.getElementById('predictionResult');
        resultElement.textContent = `Error: ${error}`;
    });
});

document.getElementById('botonBorrar').addEventListener('click', function () {
    // Reset the form
    document.getElementById('predictionForm').reset();
    // Clear the prediction result
    document.getElementById('predictionResult').textContent = '';
});