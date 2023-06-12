from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import r2_score
import xgboost as xgb
import pandas as pd
import dill 
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
dill.dump(column_order, open('column_order.pkl', 'wb'))


x = ct.fit_transform(x)
dill.dump(ct, open('ct.pkl', 'wb'))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

XGBR = xgb.XGBRegressor()

XGBR.fit(x_train, y_train)

y_pred = XGBR.predict(x_test)

dill.dump(XGBR, open('model.pkl', 'wb'))
