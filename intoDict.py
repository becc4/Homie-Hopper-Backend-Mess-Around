import json
import math

def makeDict():
    with open('users.json', 'r') as file:
        users = json.load(file)
    
    allClients = list()

    for i in users:
        name = i['userName']
        interests = (i['userInterests'])
        interests["name"] = name
        #print(interests)

        allClients.append(interests)

    return allClients

def makeList():
    with open('users.json', 'r') as file:
        users = json.load(file)
    
    all_answers = list()
    key = list()

    for i in users[0]['userInterests']:
        key.append(i)
    
    key.sort()

    for i in users: # for each user
        name = i['userName']
        interests = (i['userInterests'])

        answers = [name]

        for i in key:
            answers.append(interests[i])
        #print(keys, answers)

        all_answers.append(answers)
    
    return all_answers, key

def euclid_dist(x, y):
    distance = math.sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
    print(distance)

def main():
    INTERESTS, KEY = makeList()
    NAMES = 0
    print(INTERESTS)
    allClients = 0
    
    for x in allClients: # all the clients
        for y in allClients:
            if y == x:
                pass
            else:
                #print(x, y)
                euclid_dist(x, y)

main()