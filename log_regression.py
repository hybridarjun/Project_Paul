from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv('13.csv', usecols=range(1,12))
y = data['result']
X = data.drop('result', 1)
y = y.to_numpy()
X = X.to_numpy()
X = preprocessing.scale(X)
clf = LogisticRegression(random_state=0, solver='lbfgs', max_iter=300,
                         multi_class='multinomial').fit(X, y)

a = X[5:10, :]
print(clf.predict(a))

print(clf.predict_proba(a))
print(clf.score(X, y))

print('ge')
