import json

items ={}

# Load data from JSON file
with open('users.json') as file:
    data = json.load(file)

# Create a dictionary to store the result
result = {}

# Iterate over each user's interests
for userinterests in data:
    user = userinterests['suggestedGroup']
    interests = userinterests['userName']

    # Create a dictionary for the user's interests
    user_result = {}
    for interest, value in userinterests.items():
        user_result[interest] = value

    # Add user's interests to the result dictionary
    result[user] = user_result

# Save the result to a new JSON file
with open('user_interests_result.json', 'w') as file:
    json.dump(result, file, indent=4)

print("Result saved to user_interests_result.json")



