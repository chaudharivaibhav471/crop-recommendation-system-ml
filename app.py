from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the model and label encoder
model = joblib.load('crop_prediction_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():
    try:
        # Get form data from frontend
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        pH = float(request.form['pH'])
        rainfall = float(request.form['rainfall'])

        # Prepare input for model
        input_data = [[N, P, K, temperature, humidity, pH, rainfall]]

        # Predict using the model
        prediction = model.predict(input_data)
        predicted_crop = label_encoder.inverse_transform(prediction)

        # Return the prediction
        return jsonify({'predicted_crop': predicted_crop[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

