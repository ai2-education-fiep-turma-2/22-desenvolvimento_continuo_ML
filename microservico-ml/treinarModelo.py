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

from pickle import dump

df = pd.read_csv('auto_final.csv') 

target = df[['mpg']] 
predictors = df[['cylinders','displacement','horsepower','weight','acceleration','year','originL']]

X = predictors.values
y = target.values

sc2 = StandardScaler()
X = sc2.fit_transform(X)
dump(sc2, open('scaler.pkl', 'wb'))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape); 
print(X_test.shape)

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X.shape[1]))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='relu'))

optimizer = tf.keras.optimizers.RMSprop()

model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])

model.fit(X_train, y_train, epochs=200, validation_split=0.3)
model.save('autoModel.h5')

version='1'

export_path='/home/silvio/serving/'+version

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)