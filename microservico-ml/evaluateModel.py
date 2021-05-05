from tensorflow import keras
import pandas as pd
import numpy as np 
from numpy import vstack
import matplotlib.pyplot as plt

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error

from math import sqrt

import tensorflow as tf
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical 
from pickle import load

df = pd.read_csv('auto_final.csv') 

target = df[['mpg']] 
predictors = df[['cylinders','displacement','horsepower','weight','acceleration','year','originL']]

X = predictors.values
y = target.values

aux=X[:3].copy()
print('SC 1', X[:3])
scaler = load(open('scaler.pkl', 'rb'))
X = scaler.transform(X)
print('SC 2', X[:3])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)

model = keras.models.load_model('autoModel.h5')

results = model.evaluate(X_test, y_test)
print("test loss, test acc:", results)

y_pred=predictions = model.predict(X[:3])
print(y_test[:3],y_pred)

print('aux 1', aux)
y_pred=predictions = model.predict(aux)
print(y_test[:3],y_pred)

aux = scaler.transform(aux)
print('aux 2', aux)

y_pred=predictions = model.predict(aux)
print(y_test[:3],y_pred)