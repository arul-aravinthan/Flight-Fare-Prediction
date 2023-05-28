from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import r2_score
import xgboost as xgb
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer

#Creating the model
df = pd.read_csv('flights.csv')
df = df.drop(['Unnamed: 0', 'flight'], axis=1)

ct = ColumnTransformer([
    ('labelencoder', OneHotEncoder(), ['airline', 'source_city', 'departure_time', 'stops', 'arrival_time', 'destination_city', 'class']),
    ('standardscaler', StandardScaler(), ['duration', 'days_left'])])



x = df.drop(['price'], axis=1)
y = df['price']
y = y

column_order = x.columns
joblib.dump(column_order, 'column_order.pkl')


x = ct.fit_transform(x)
joblib.dump(ct, 'ct.pkl')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

XGBR = xgb.XGBRegressor()

XGBR.fit(x_train, y_train)

y_pred = XGBR.predict(x_test)

joblib.dump(XGBR, 'model.pkl')
