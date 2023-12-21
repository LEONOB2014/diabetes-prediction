import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline

import pickle

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
             'Income': 9.0}



def predict(patient=patient):
    with open('./models/model_gbc.pkl', 'rb') as f_in:
        model = pickle.load(f_in)

    patient = pd.DataFrame(patient, index=[0])
    best_model = model.best_estimator_
    y_prob = best_model.predict_proba(patient)[0][1]
    risk = y_prob >= 0.5
    
    result = {
        'diabetes_probability': float(y_prob),
        'diabetes_intervention': bool(risk),
    }

    print(f"diabetes_probability: {y_prob}, diabetes_intervention: {risk}")
    


if __name__ == '__main__':
    predict(patient)