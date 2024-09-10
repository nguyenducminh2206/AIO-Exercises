from datasets import load_dataset
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer


iris_X, iris_y = datasets.load_iris(return_X_y=True)

# Split datasets (Train: 8 - Test: 2)
X_train, X_test, y_train, y_test = train_test_split(
    iris_X,
    iris_y,
    test_size=0.2,
    random_state=42
)

# Scale the features
scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

# Initialize and train the kNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, y_train)

# Predict and evaluate
y_pred = knn_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(accuracy)

# IMDB dataset
imdb = load_dataset('imdb')
imdb_train, imdb_test = imdb['train'], imdb['test']

# Convert text to vector using BoW
vectorizer = CountVectorizer(max_features=1000)

X_train = vectorizer.fit_transform(imdb_train['text']).toarray()
X_test = vectorizer.transform(imdb_test['text']).toarray()

y_train = np.array(imdb_train['label'])
y_test = np.array(imdb_test['label'])

# Scale the features 
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

# Build kNN Classifier
knn_class = KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree')
knn_class.fit(X_train, y_train)

# Predict and evaluate
y_predict = knn_class.predict(X_test)
imdb_accuracy = accuracy_score(y_test, y_pred)
print(imdb_accuracy)