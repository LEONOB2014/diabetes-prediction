from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline

import pickle


with open('./models/model_gbc2.pkl', 'rb') as f_in:
    model = pickle.load(f_in)