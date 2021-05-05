import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('Auto2.csv') 
print(df.shape)
df.describe()

le = LabelEncoder()
df['originL']= le.fit_transform(df['origin'])

df=df.drop(columns = ['name','origin'])
df.to_csv('auto_final.csv')
