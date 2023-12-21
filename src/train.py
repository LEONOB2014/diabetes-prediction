
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline

import pickle

def train_model():

    df = pd.read_csv('./data/df_train.csv')
    target = "Diabetes_binary"
    X = df.drop(columns=target)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = make_pipeline(
        SimpleImputer(),
        GradientBoostingClassifier()
    )
    params = {
        "simpleimputer__strategy": ["mean", "median"],
        "gradientboostingclassifier__max_depth": range(2, 5),
        "gradientboostingclassifier__n_estimators": range(20, 31, 5)
    }
    model = GridSearchCV(clf, param_grid=params, cv=5, n_jobs=-1, verbose=1)
    # Fit model to over-sampled training data
    model.fit(X_train, y_train)
    best_model = model.best_estimator_
    with open("./models/model_gbc2.pkl", "wb") as f:
        pickle.dump(best_model, f)


if __name__ == '__main__':
    train_model()