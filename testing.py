'''
Organizing user data from users.json
'''

# # Import required libraries
# import json

# # Global variables
# email_list = []
# username_list = []
# snapchat_list = []
# interests_list = []
# userid_list = []

# with open(r"users.json") as file:
#     data_dict = {}
#     interests_dict = {}

#     data_dict = json.load(file)
#     # print(data_dict)
#     for i in data_dict:
#         email_list.append(i["userEmail"])
#         username_list.append(i["userName"])
#         snapchat_list.append(i["snapInfo"])
#         interests_list.append(i["userInterests"])
#         userid_list.append(i["userID"])

#     # print(interests_list)
    
#     interests_dict = json.loads(interests_list)
#     # print(interests_dict)

'''==========================================================================================================================='''

'''
Messing around with PCA (partial component analysis)
'''

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
pca = PCA()
# Perform PCA, fit the PCA model to the input data and transform it to the principal components space (column)
X = pca.fit_transform(x)
# 
print(f"Covariance matrix on how much the features vary together\n{pca.get_covariance()}\n")
explained_variance = pca.explained_variance_ratio_
print(f"Total variance ratios for each principal component\n{explained_variance}\n")

print("="*20)

# Visualize the covariance to help select the amount of principal components
with plt.style.context("dark_background"):
    plt.figure(figsize=(6,4))
    plt.bar(range(4), explained_variance, alpha=0.5, align="center", label="individual explained variance")
    plt.ylabel("Explained variance ratio")
    plt.xlabel("Principal components")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()      # Use plt.show() to show the plot you just created

    