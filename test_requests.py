import requests
import json

# definition of url to send request to
url = 'http://localhost:8777/predict'

# News Headline, which are goint to be predicted with equivalent category: Entertainment, Business, Technology, Health
data = {
    "titles": [
               "The Future of Autonomous Vehicles: What’s Next for the Industry?",
               "Health Experts Warn of Rising Mental Health Issues Post-Pandemic",
               "Global Stock Markets Plunge Amid Economic Uncertainty",
               "Hollywood's Box Office Struggles Amidst Streaming Service Dominance"
               ]
}

# Send the POST request with JSON data
response = requests.post(url, json=data)

# Print the response
print(response.json())
