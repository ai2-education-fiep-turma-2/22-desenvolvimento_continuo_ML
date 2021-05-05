from tensorflow import keras
import numpy as np
import sys

Xpred=np.zeros(7)

pos=0

for i in sys.argv[1:]:
    Xpred[pos]=int(i)
    pos=pos+1

Xpred = Xpred.reshape(1,7)

model = keras.models.load_model('autoModel.h5')
predictions = model.predict(Xpred)
print(predictions)