'''
Organizing user data from users.json
'''
# Import required libraries
import json

def populate_lists():
    # Global variables
    email_list = []
    username_list = []
    snapchat_list = []
    interests_list = []
    userid_list = []

    with open(r"users.json") as file:
        data_dict = {}
        interests_dict = []

        data_dict = json.load(file)
        # print(data_dict)
        for i in data_dict:
            email_list.append(i["userEmail"])
            username_list.append(i["userName"])
            snapchat_list.append(i["snapInfo"])
            interests_list.append(i["userInterests"])
            userid_list.append(i["userID"])

    # print(interests_list)

    for i in interests_list:
        keys = i.keys()
        values = i.values()
        # print(keys,values)
        # for key in keys:
        #     print(key)

    for key in keys:
        print(key)
    for val in values:
        print(val)

        # print(i.values())

'''==========================================================================================================================='''

'''
Visualizing bar data with pandas and matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

def bar_data():
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

'''
Visualizing user interest data as a scatter plot
'''
# Also imported pandas as pd and matplotlib as plt libraries
import numpy as np

def scatter_data():
    # # Read and save userInsterest.json to a pandas Data Frame
    # data = pd.read_json(r"C:\Users\lengu\Desktop\School\CSE 310 Applied programming\2023\HH_survey\Homie-Hopper-Backend-Mess-Around\userInsterest.json")
    # data_df = pd.DataFrame(data)
    
    # # Set userID values as indices
    # data_df.set_index("userID", inplace=True)
    # data_df = data_df["userInterests"].apply(pd.Series).T

    # # # Create scatter plot with first 3 users
    # # plt.scatter(data_df.index, data_df["0zJNMsXJusc0eSjAsLpJiK2qKFA3"], color="blue", label="Peyton Haws")
    # # plt.scatter(data_df.index, data_df["23YTrKsZbfahA72gd0zlXXgTzRb2"], color="red", label="Jared Keh")
    # # plt.scatter(data_df.index, data_df["2ctKnR3VjpfBNesW8MkuRqpYjJh1"], color="green", label="Sergio Alba")

    # # Convert userID column to a list
    # user_ids = data_df.columns.to_list()
    # # Set colors
    # # colors = np.random.uniform(15, 80)
    # # colors = ["red", "blue", "green"]
    # colors = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray", "olive", "cyan"] * 4
    # # Create scatter plots
    # for i,user_id in enumerate(user_ids):
    #     plt.scatter(data_df.index, data_df[user_id], color=colors[i], label=user_id)

    # # Set axis labels and legend
    # plt.xlabel("Question Number")
    # plt.ylabel("Interest Level")
    # plt.legend()
    # # Display the scatter plot
    # plt.show()

    # Read and save userInsterest.json to a pandas DataFrame
    data = pd.read_json(r"C:\Users\lengu\Desktop\School\CSE 310 Applied programming\2023\HH_survey\Homie-Hopper-Backend-Mess-Around\userInsterest.json")
    data_df = pd.DataFrame(data)

    # Set userID values as indices
    data_df.set_index("userID", inplace=True)
    data_df = data_df["userInterests"].apply(pd.Series).T

    # Get user IDs and covert to a list
    user_ids = data_df.columns.tolist()

    fig, ax = plt.subplot()
    scatter_plots = []
    # Loop through each user profile
    for user_id in user_ids:
        # Generate x and y coordinates based on user profiles
        x = data_df.index.astype(int)
        y = data_df[user_id]
        # Set sizes and colors based on user profiles
        sizes = data_df[user_id]
        colors = data_df[user_id]
        scatter = ax.scatter(x, y, s=sizes, c=colors, cmap="viridis", vmin=0, vmax=100)
        scatter_plots.append(scatter[0])

    # Define and display the plot
    ax.set(xlim=(0,data_df.index.max()), ylim=(-1,5))       # Adjusts the y axis as needed
    ax.set_xlabel("Question Number")
    ax.set_ylabel("Interest Level")
    ax.set_title("User Profiles Interests")
    fig.colorbar(scatter_plots[0], label="color")
    ax.legend(loc="uppper right", bbox_to_anchor=(1.3,1.0))
    plt.show()


'''==========================================================================================================================='''

'''
matplotlib scatter plot practice
'''

# Imported matplotlib.pyplot as plt and numpy as np 
def scatter_practice():
    # plt.style.use("_mpl-gallery")

    # Generate random data
    x = 4+np.random.normal(0,2,24)
    y = 4+np.random.normal(0,2,len(x))

    # Save sorta random sizes and colors
    sizes = np.random.uniform(15,80,len(x))
    colors = np.random.uniform(15,80,len(x))

    # Define and display the plot (WARNING: will be smol)
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, s=sizes, c=colors, cmap="viridis", vmin=0, vmax=100)
    ax.set(xlim=(0,8), xticks=np.arange(1,8), ylim=(0,8), yticks=np.arange(1,8))
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.colorbar(scatter, label="Color")
    plt.show()


# Imported json, numpy as mp, and matplotlib.pyplot as plt

def scatter_data_simple():
    # open file to save data to lists
    with open(r"userInsterest.json") as file:
        data_list = []
        UI_list = []
        id_list = []
        data_list = json.load(file)

        # Convert all userInterests values to list data types
        for i in data_list:
            UI_list.append(list(i["userInterests"].values()))     # UI_list to be y axis
            # id_list.append(i["userID"])
        
        # Temporary list to represent total amount of users
        total_users = []
        for i in range(len(data_list)):
            total_users.append(i)        # total_users list to be x axis

        # Set custom axes ticks and limits
        plt.xticks(np.arange(0, len(total_users), 1))
        plt.yticks(np.arange(0, len(UI_list), 1))
        # Define and show plot
        for user, interests in zip(total_users, UI_list):
            plt.scatter([user] * len(interests), interests)
        # plt.scatter(total_users, UI_list)
        
        # # Define labels
        plt.xlabel("User")
        plt.ylabel("Interest Level")
        plt.title("User Interests")
        plt.show()

'''==========================================================================================================================='''


'''
Recommendation engine using Euclidean distance method
'''

# Imported pandas as pd 

def reccomend():
    data = pd.read_json(r"C:\Users\lengu\Desktop\School\CSE 310 Applied programming\2023\HH_survey\Homie-Hopper-Backend-Mess-Around\userInsterest.json")
    # print(data.info())

    print(data.groupby("userID")["userInterests"].count().head()) # Whatever is in parenthesis can NOT be a dictionary

    # with open(r"userInsterest") as file:
    #     data = pd.read_json("C:\Users\lengu\Desktop\School\CSE 310 Applied programming\2023\HH_survey\Homie-Hopper-Backend-Mess-Around\userInsterest.json")

'''==========================================================================================================================='''

'''
Sorting and weighing algorithm for users
'''
def bubble_sort(array):
    switched = False
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                switched = True

            if not switched:
                break
    print(array)

### TODO Use embedded dictionaries with separate key "labels" to assign a rank/weight to each question and edit original data with rank value
{
    "userInterests": {
        "q7": {"Level": 1, "Rank": 10},
        "q1": {"Level": 0, "Rank": 9},
        "q6": {"Level": 1, "Rank": 8}
    }
}

'''==========================================================================================================================='''

'''
Finding similarities with Euclidean distance 
'''

# # ## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Euclidean distance is simply know as the 2d length between 2 points in space.
# Same as Pythagorean theorem except its expanded (or deconstructed depending on your beliefs)
#   Pythagorean: a^2 + b^2 = c^2
#   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   Euclidean: sqrt((b1 - a1)^2 + (b2 - a2)^2 +...) = c
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Import math, json libraries and dataset list obj from users copy.json
from users_copy import dataset
import math

def euclid_dist(x, y):
    # Fancy list comprehension using the zip() object
    distance = math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
    print(distance)

def find_similarities():
    pass

'''==========================================================================================================================='''

'''
Calculating Pearsons correlation coefficient
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Officially known as Person correlation coeffiecient (PCC), is a measure of linear 
# correlation between two vars. Or two persons data points. Defined as the covariance 
# of 2 variables divided my the product of their respective standard deviation. Is very 
# well suited to quantifying linear correlations, and remain largely unaffected by 
# different scales of measurement
# 
# where r = the coefficient, cov = covariance, sd = standard deviation
# r(x,y) = cov(x,y)/(sd(x)*sd(y))
# 
# 1) Calculate the averages of x and y (assuming there are multiple values, or data 
# collection, of x and y)
# 2) Calculate the difference between each data point value and its respective average
# 3) Square the differences
# 4) Calculate the sum of of squared differences
# 5) Calculate the sum of the product (do this first) of differences
# 6) Squareroot the sums (for x and y)
# 7) Find r
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import sqrt from math
# from users_copy import dataset
from sampledata import dataset

def process_users(user1, user2):
    same_interest = {}
    for i in dataset[user1]:
        if i in dataset[user2]:
            same_interest[i] = 1

    # print(same_interest)

    # for i in dataset[user1]:
    #     print(i)
        # if i in i["userInterests"]:
        #     same_interest[i] = 1

    num_of_interests = len(same_interest)
    print(same_interest)
    print(num_of_interests)
    print(dataset[user1])
    print(dataset[user2])



def pear_coef(user1, user2):

    # print(IDs, interests, count)
    # q1_vals = []
    # for j in interests:
        
    #     q1_vals.append(j["q1"])

    
    # print(q1_vals)
    # print(sum(q1_vals)/len(q1_vals))

    pass


'''==========================================================================================================================='''


def main():
    # my_array = [12,5,99,-9,3.14]

    x_coord = [1,2,3,4,5]
    y_coord = [2,4,6,8,10]

    x = [1,2]
    y = [5,10]

    user1 = "Lisa Rose"
    user2 = "Michael Phillips"

    # populate_lists()
    # bar_data()
    # scatter_data()
    # scatter_practice()
    # scatter_data_simple()
    # bubble_sort(my_array)
    # euclid_dist(x, y)
    # find_similarities()
    process_users(user1, user2)
    # pear_coef()
        

if __name__ == "__main__":
    main()
