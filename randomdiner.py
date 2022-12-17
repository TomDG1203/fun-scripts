import random
import requests

# Set the API endpoint
endpoint = "https://api.uber.com/v1/products"

# Set the parameters for the request
params = {
    "latitude": 51.05,
    "longitude": 3.7167
}

# Set the header with the API key
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

# Send the request and get the response
response = requests.get(endpoint, params=params, headers=headers)

# Get the options from the response
options = response.json()

# Get the list of options from the response
option_list = options["products"]

# Choose a random option from the list
chosen_option = random.choice(option_list)

# Print the chosen option
print(chosen_option)
