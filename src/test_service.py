import requests
import json

patient = {'HighBP': 1.0,
 'HighChol': 1.0,
 'CholCheck': 1.0,
 'BMI': 35.0,
 'Smoker': 0.0,
 'Stroke': 0.0,
 'HeartDiseaseorAttack': 0.0,
 'PhysActivity': 1.0,
 'Fruits': 0.0,
 'Veggies': 1.0,
 'HvyAlcoholConsump': 1.0,
 'AnyHealthcare': 1.0,
 'NoDocbcCost': 0.0,
 'GenHlth': 2.0,
 'MentHlth': 0.0,
 'PhysHlth': 0.0,
 'DiffWalk': 0.0,
 'Sex': 1.0,
 'Age': 5.0,
 'Education': 4.0,
 'Income': 9.0
 }

url = 'http://localhost:9696/predict'
response = requests.post(url, json=patient)
result = response.json()

print(json.dumps(result, indent=2))