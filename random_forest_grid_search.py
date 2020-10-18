from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans
import numpy as np
import sys


# Load Data -- It is going be the collection of alpha carbon distances in the different macrostates.
traj_total = np.load('../../featurized_trajs_1ns/raw/raw_tot.npy')
ncluster = 16
kmeans = KMeans(n_clusters=ncluster, random_state=0).fit(traj_total)
label = kmeans.labels_
label = np.reshape(label, (11880, 1))
dataset = np.load(str(sys.argv[1])+'_ttraj.npy')
labeled_dataset = np.concatenate((dataset, label), axis=1)
np.random.shuffle(labeled_dataset)
data = labeled_dataset[:, 0:2]
label = labeled_dataset[:, 2]

#Data split
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.33, random_state=42)

# Set the parameters by cross-validation
parameters = {'n_estimators': [5, 10, 15, 20, 25, 30], 'max_depth': [2,4,6,8,10,12]}
print("# Tuning hyper-parameters for accuracy")
print()

# Fit for all combination of parameters
clf = GridSearchCV(RandomForestClassifier(), parameters, cv=5, scoring='accuracy', n_jobs=-1)
clf.fit(X_train, y_train)

# Print results
print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print("Best accuracy score found on development set:")
print()
print(clf.best_score_)
print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"
          % (mean, std * 2, params))
print()

print("Detailed classification report:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
