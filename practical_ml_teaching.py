import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm 
from sklearn.linear_model import LinearRegression 

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Open'] * 100.0
df['Change_PCT'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'Change_PCT', 'Adj. Volume']]

forecast_col = 'Adj. Close'


df['label'] = df[forecast_col]

forecast_out = 3

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())

X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)


clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
