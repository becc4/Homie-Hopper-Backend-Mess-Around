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
print(iris.feature_names)
print(iris.target_names)

# Format the data from iris dataset to a data frame from pandas
data = pd.DataFrame(iris.data)
data.columns = iris.feature_names
data["CLASS"] = iris.target
print(data.head())
