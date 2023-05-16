'''
Organizing user data from users.json
'''

# Import required libraries
import json

# Global variables
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

# for i in interests_list:
#     print(i)
    # interests_dict = json.loads(interests_list)
    # print(interests_dict)

'''==========================================================================================================================='''

'''
Visualizing data with pandas and matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

# Open and parse the json file
with open(r"userInsterest.json") as file:
    data_df = pd.read_json(file)

    # Set the userID values as indicies
    data_df.set_index("userID", inplace=True)
    data_df = data_df["userInterests"].apply(pd.Series).T
    # # Convert the data_df values to ints and sort them by numerical order
    # data_df.columns = data_df.columns.str[1:].astype(int)
    # data_df = data_df.sort_index(axis=1)

    # Set plot type, and axes lables
    ax = data_df.plot(kind="bar", rot=0)
    ax.set_xlabel("Question Number")
    ax.set_ylabel("Interest Level")
    ax.legend(title="user ID", bbox_to_anchor=(1,1))

    plt.show()

'''==========================================================================================================================='''

