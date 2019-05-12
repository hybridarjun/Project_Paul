from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv('total.csv', usecols=range(1,12))
data = data.sample(frac=1).reset_index(drop=True)
y = data['result']
X = data.drop('result', 1)
y = y.to_numpy()
X = X.to_numpy()
X = preprocessing.scale(X)

clf = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=0)
clf.fit(X, y)

a = X[:1, :]

print(clf.predict(a))

print(clf.predict_proba(a))
print(clf.score(X, y))


print(clf.feature_importances_)

#print(clf.predict([[0, 0, 0, 0]]))
