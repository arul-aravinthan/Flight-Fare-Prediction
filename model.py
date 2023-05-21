from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle

df = pd.read_csv('flights.csv')

df = df.drop(['Unnamed: 0', 'flight'], axis=1)


# Encode the categorical variables
le = LabelEncoder()
for column in df.columns:
    if df[column].dtype == type(object):
        df[column] = le.fit_transform(df[column])

# Split the data into features and label

x = df.drop(['price'], axis=1)
y = df['price']

std = StandardScaler()
x = std.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

RF = RandomForestRegressor()
RF.fit(x_train, y_train)

y_pred = RF.predict(x_test)
print(r2_score(y_test, y_pred))

pickle.dump(RF, open('model.pkl', 'wb'))

