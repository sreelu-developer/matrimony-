# Compare Algorithms
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import numpy as np

X = []
y = []
Xstring = []
ystring = []

disx = []
disy = []


def traing():
    training_data = np.loadtxt(r"C:\Users\user\PycharmProjects\matrimony\static\dataset.txt", dtype=str, delimiter="\t")
    for record in training_data:
        print(record)


        if record[0] != '':
            lis = []

            print(record)

            for i in range(0,len(record)-1):
                lis.append(int(record[i]))
            X.append(lis)
            ystring.append(record[-1])

            if record[-1] not in disy:
                disy.append(record[-1])


traing()
print("=====================================")

print(len(disx),disx)
print(disy)

for i in range(0,len(ystring)):
    yy=disy.index(ystring[i])
    y.append(yy)


for i in range(0,len(X)):
    print(len(X[i]),X[i],y[i])

print("=====================================")
# load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
# names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# dataframe = pandas.read_csv(url, names=names)
# array = dataframe.values
# X = array[:, 0:8]
Y = y
# prepare configuration for cross validation test harness
seed = 2
# prepare models
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = model_selection.KFold(n_splits=10)
    cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    str ="Accuracy of "
    msg = "%s %s: %f (%f)" % (str,name, cv_results.mean(), cv_results.std())
    print(msg)
# boxplot algorithm comparison
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()