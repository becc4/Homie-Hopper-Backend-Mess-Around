'''
Organizing user data from users.json
'''

# Import required libraries
import json

# Global variables
email_list = []
username_list = []
snapchat_list = []
interests_list = []
userid_list = []

with open(r"users.json") as file:
    data_dict = {}
    interests_dict = {}

    data_dict = json.load(file)
    # print(data_dict)
    for i in data_dict:
        email_list.append(i["userEmail"])
        username_list.append(i["userName"])
        snapchat_list.append(i["snapInfo"])
        interests_list.append(i["userInterests"])
        userid_list.append(i["userID"])

for i in interests_list:
    print(i)

    
    # interests_dict = json.loads(interests_list)
    # print(interests_dict)

'''==========================================================================================================================='''

'''
# Messing around with PCA (partial component analysis)
# '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
# Display the feature names and Encoding of target vars
print(f"These are the feature names\n{iris.feature_names}\n")
print(f"These are the target names\n{iris.target_names}\n")

# Format the data from iris dataset to a data frame from pandas
data = pd.DataFrame(iris.data)
data.columns = iris.feature_names
data["CLASS"] = iris.target
print(f"These are the header titles\n{data.head()}\n")

# Display the range index, all data columns, datatypes, and memory used with info() method
print(data.info())
# Display a statistical overview of the dataset
print(data.describe())

# Split the data, specifically the features and targets as 2 separate variables
x = data.iloc[:,:4]     # Features
y = data.iloc[:,4]      # Targets
print(f"This is the shape of x and y. Format = (rows, features)\n{x.shape, y.shape}")
print("Result is a tuple, or tuple of tuples\n")

'''==========================================================================================================================='''

'''
Actually using PCA from sklearn
'''

from sklearn.decomposition import PCA

# Instantiate a new object of PCA class
pca = PCA(n_components=4)       # The shapes arguments need to match when the error is thrown
# Changes the n_components=3 to see the error Im talking about
# Perform PCA, fit the PCA model to the input data and transform it to the principal components space (column)
X = pca.fit_transform(x)
# 
print(f"Covariance matrix on how much the features vary together\n{pca.get_covariance()}\n")
explained_variance = pca.explained_variance_ratio_
print(f"Total variance ratios for each principal component\n{explained_variance}\n")

print("="*50)

# Visualize the covariance to help select the amount of principal components
with plt.style.context("dark_background"):
    plt.figure(figsize=(6,4))
    plt.bar(range(4), explained_variance, alpha=0.5, align="center", label="individual explained variance")
    plt.ylabel("Explained variance ratio")
    plt.xlabel("Principal components")
    plt.legend(loc="best")
    plt.tight_layout()
    # plt.show()      # Use plt.show() to show the plot you just created

print()

# Seeing the plot, we can confidently conclude that there are 4 components with  variance
# We therefore go back to where we created `pca` variable, line 75, set the n_components= argument to however many components have significant variance

'''==========================================================================================================================='''

'''
Splitting the data into training and test sets
'''
# Why do this?
# To prevent predictions on only trained data leading to overfitting, thus giving bad results for unknown data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20, stratify=y)

'''==========================================================================================================================='''

'''
Training the Model and predicting
'''

from sklearn.neighbors import KNeighborsClassifier

# Save the KNN classifier to a variable
model = KNeighborsClassifier(7)
# Fit the training data to the model
model.fit(X_train, y_train)
# Predict the class labels of the test dataset
y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm = confusion_matrix(y_test, y_pred)
# Confusion matrix will who the count all false positives and negatives, and true positives and negatives
print(f"The confusion matrix\n{cm}\n")
# Accuracy score is formatted as a percentage (0.5 = 50%) as how effective the prediction is for predicting new data
print(f"The accurcay score\n{accuracy_score(y_test, y_pred)}")