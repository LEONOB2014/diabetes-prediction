import pickle
import numpy as np

from flask import Flask, request, jsonify



with open('./models/model_gbc.pkl', 'rb') as f_in:
    model = pickle.load(f_in)

def predict_single(patient, model):
    y_pred = model.predict_proba(patient)[:, 1]
    return y_pred[0]


app = Flask('diabetes')


@app.route('/predict', methods=['POST'])
def predict():
    patient = request.get_json()

    prediction = predict_single(patient, model)
    diabetes_int = prediction >= 0.5
    
    result = {
        'diabetes_probability': float(prediction),
        'diabetes_intervention': bool(diabetes_int),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)