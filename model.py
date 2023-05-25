from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score
import xgboost as xgb
import pandas as pd
import pickle

df = pd.read_csv('flights.csv')

df = df.drop(['Unnamed: 0', 'flight'], axis=1)

label_encoders = []
# Encode the categorical variables
for column in df.columns:
    if df[column].dtype == type(object):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders.append(le)

pickle.dump(label_encoders, open('label_encoders.pkl', 'wb'))

x = df.drop(['price'], axis=1)
y = df['price']

std = StandardScaler()
x = std.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

XGBR = xgb.XGBRegressor()
XGBR.fit(x_train, y_train)

y_pred = XGBR.predict(x_test)
print(r2_score(y_test, y_pred))

pickle.dump(XGBR, open('model.pkl', 'wb'))
print(df.head())
