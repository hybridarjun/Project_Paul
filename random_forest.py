from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn import preprocessing

data = pd.read_csv('total.csv', usecols=range(1,12))
data = data.sample(frac=1).reset_index(drop=True)
X_train = data.drop('result',1).iloc[:901,:]
X_test = data.drop('result',1).iloc[901:,:]
y_train = data['result'].iloc[:901]
y_test = data['result'].iloc[901:]
y_train = y_train.to_numpy()
X_train= X_train.to_numpy()
X_train = preprocessing.scale(X_train)
clf = RandomForestClassifier(n_estimators=200, max_depth=20,
                             random_state=0)
clf.fit(X_train,y_train)


print(pd.DataFrame(clf.predict_proba(X_test)))
print(clf.score(X_test, y_test))


print(clf.feature_importances_)

#print(clf.predict([[0, 0, 0, 0]]))
