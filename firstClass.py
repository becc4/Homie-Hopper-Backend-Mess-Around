
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Possible class structure for handling back end of Homie Hopper
# There will be 3 classes: User, Math, and Data
#   User: will store an individual user's data
#   Math: will store euclidean distance as d, pearson correlation coefficient as r, and
#   use user data from the user class
#   Data: will extract and format necessary user data from the json
# 
# ALL CLASS STRUCTURES ARE SUBJECT TO CHANGE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from users_copy import dataset
import numpy as np
import json
import math

class User:
    def __init__(self, ID, ANSWERS):
        self.ID = ID
        self.ANSWERS = ANSWERS

    def assign_data(data):
        # figure out how to assign different user ids and answers to individual users
        pass

class Math:
    def __init__(self, user1_data, user2_data, d, r):
        self.user1_data = user1_data
        self.user2_data = user2_data
        self.d = d
        self.r = r

    def euclid_distance(self):
        self.d = math.sqrt(sum(pow(a - b, 2) for a, b in zip(self.user1_data, self.user2_data)))
        print(self.d)
        return self.d

    def pearson_coefficient(self):
        X = np.array(self.user1_data)
        Y = np.array(self.user2_data)

        mean_x = np.mean(X)
        mean_y = np.mean(Y)

        dev_x = X - mean_x
        dev_y = Y - mean_y

        sum_prod_devs = np.sum(dev_x * dev_y)

        std_dev_x = np.std(X)
        std_dev_y = np.std(Y)

        self.r = sum_prod_devs / (len(X) * std_dev_x * std_dev_y)

        print(self.r)
        return self.r

class Data:
    def __init__(self, data_dict, interests_list, userid_list):
        self.data_dict = {}
        self.interests_list = []
        self.userid_list = []

    def process_data(self):
        with open(r"users.json") as file:    
            self.data_dict = json.load(file)

            for i in self.data_dict:
                self.interests_list.append(i["userInterests"])
                self.userid_list.append(i["userID"])

        return self.interests_list, self.userid_list

def main():
    # figure out which parameters to pass in to which objects
    # this order will probably be best
    data = Data()   # Extract all necessary user data, to pass to User()
    user = User()   # reorganize data and choose users, to pass to Math()
    math = Math()   # Calculate the distance (d) and pearson coefficient (r) for the users chosen
    

if __name__ == "__main__":
    main()