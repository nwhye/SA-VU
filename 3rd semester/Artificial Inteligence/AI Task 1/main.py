import pandas as pd
from sklearn import metrics
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
import numpy as np

from sklearn import tree
from sklearn import ensemble
from sklearn import svm
from sklearn import neighbors

dataset = pd.read_table('data.txt', delimiter='\t', header=None)

X = dataset.iloc[:, 1:8].values
y = dataset.iloc[:, 8:9].values

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=1)


scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
y_train = y_train.ravel()

# Decision Tree
dt_params_dict = {
    'criterion': ['gini', 'entropy', 'log_loss'],
    'max_depth': [None, *range(1, 20)],
    'min_samples_split': [*range(2, 10)]
}
dt_grid = model_selection.GridSearchCV(tree.DecisionTreeClassifier(), dt_params_dict, scoring='accuracy')
dt_grid.fit(X_train, y_train)
print("DT GSCV best parameters: ", dt_grid.best_params_)

y_train_pred = dt_grid.predict(X_train)
y_test_pred = dt_grid.predict(X_test)

acc_train = metrics.accuracy_score(y_train, y_train_pred)
print("\nDT acc_train: %f" % acc_train)
acc = metrics.accuracy_score(y_test, y_test_pred)
print("DT acc: %f" % acc)

recall_train = metrics.recall_score(y_train, y_train_pred, average=None, zero_division=0)
print("\nDT recall_train:", recall_train)
recall = metrics.recall_score(y_test, y_test_pred, average=None, zero_division=0)
print("DT recall: {0}".format(recall))

prec_train = metrics.precision_score(y_train, y_train_pred, average=None, zero_division=0)
print("\nDT precision_train: ", prec_train)
prec = metrics.precision_score(y_test, y_test_pred, average=None, zero_division=0)
print("DT precision: ", prec)

f1_train = metrics.f1_score(y_train, y_train_pred, average=None)
print("\nDT f1 train: ", f1_train)
f1 = metrics.f1_score(y_test, y_test_pred, average=None)
print("DT f1: ", f1)

conf_mat = metrics.confusion_matrix(y_test, y_test_pred)
print("\nDT conf_mat:")
print(conf_mat)

# Random Forest
rf_params_dict = {
    'criterion': ['gini', 'entropy', 'log_loss'],
    'max_depth': [None, *range(1, 8)]
}
rf_grid = model_selection.GridSearchCV(ensemble.RandomForestClassifier(), rf_params_dict, scoring='accuracy')
rf_grid.fit(X_train, y_train)
print("RF GSCV best parameters: ", rf_grid.best_params_)
y_train_pred = rf_grid.predict(X_train)
y_test_pred = rf_grid.predict(X_test)

acc_train = metrics.accuracy_score(y_train, y_train_pred)
print("\nRF acc_train: %f" % acc_train)
acc = metrics.accuracy_score(y_test, y_test_pred)
print("RF acc: %f" % acc)

recall_train = metrics.recall_score(y_train, y_train_pred, average=None)
print("\nRF recall_train:", recall_train)
recall = metrics.recall_score(y_test, y_test_pred, average=None)
print("RF recall:", recall)

prec_train = metrics.precision_score(y_train, y_train_pred, average=None, zero_division=0)
print("\nRF precision_train:", prec_train)
prec = metrics.precision_score(y_test, y_test_pred, average=None, zero_division=0)
print("RF precision:", prec)

f1_train = metrics.f1_score(y_train, y_train_pred, average=None)
print("\nRF f1 train:", f1_train)
f1 = metrics.f1_score(y_test, y_test_pred, average=None)
print("RF f1:", f1)

conf_mat = metrics.confusion_matrix(y_test, y_test_pred)
print("\nRF conf_mat:")
print(conf_mat)

# Support Vector Machines
svm_params_dict = {
    'C': [*np.arange(1.0, 2.1, 0.1)],
    'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
}
svm_grid = model_selection.GridSearchCV(svm.SVC(), svm_params_dict, scoring = 'accuracy', error_score='raise')
svm_grid.fit(X_train, y_train)
print("SVM GSCV best parameters: ", svm_grid.best_params_)
y_train_pred = svm_grid.predict(X_train)
y_test_pred = svm_grid.predict(X_test)

acc_train = metrics.accuracy_score(y_train, y_train_pred)
print("\nSVC acc_train:", acc_train )
acc = metrics.accuracy_score(y_test, y_test_pred)
print("SVC acc:", acc )

recall_train = metrics.recall_score(y_train, y_train_pred, average = None)
print("\nSVC recall_train:", recall_train )
recall = metrics.recall_score(y_test, y_test_pred, average = None)
print("SVC recall:", recall )

prec_train = metrics.precision_score(y_train, y_train_pred, average = None, zero_division = 0)
print("\nSVC precision_train:", prec_train )
prec = metrics.precision_score(y_test, y_test_pred, average = None, zero_division = 0)
print("SVC precision:", prec )

f1_train = metrics.f1_score(y_train, y_train_pred, average=None)
print("\nSVC f1 train:", f1_train )
f1 = metrics.f1_score(y_test, y_test_pred, average=None)
print("SVC f1:", f1 )

conf_mat = metrics.confusion_matrix(y_test, y_test_pred)
print("\nSVC conf_mat:")
print(conf_mat)

# k-Nearest Neighbours
knn_params_dict = {
    'n_neighbors': [*range(1, 20)]
}
knn_grid = model_selection.GridSearchCV(neighbors.KNeighborsClassifier(), knn_params_dict, scoring='accuracy')
knn_grid.fit(X_train, y_train)
print("kNN GSCV best parameters: ", knn_grid.best_params_)

y_train_pred = knn_grid.predict(X_train)
y_test_pred = knn_grid.predict(X_test)

acc_train = metrics.accuracy_score(y_train, y_train_pred)
print("\nkNN acc_train:", acc_train)
acc = metrics.accuracy_score(y_test, y_test_pred)
print("kNN acc:", acc)

recall_train = metrics.recall_score(y_train, y_train_pred, average=None)
print("\nkNN recall_train:", recall_train)
recall = metrics.recall_score(y_test, y_test_pred, average=None)
print("kNN recall:", recall)

prec_train = metrics.precision_score(y_train, y_train_pred, average=None, zero_division=0)
print("\nkNN precision_train:", prec_train)
prec = metrics.precision_score(y_test, y_test_pred, average=None, zero_division=0)
print("kNN precision:", prec)

f1_train = metrics.f1_score(y_train, y_train_pred, average=None)
print("\nkNN f1 train:", f1_train)
f1 = metrics.f1_score(y_test, y_test_pred, average=None)
print("kNN f1:", f1)

conf_mat = metrics.confusion_matrix(y_test, y_test_pred)
print("\nkNN conf_mat:")
print(conf_mat)
