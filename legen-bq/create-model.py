import requests
import json

# Define the endpoint URL
url = "http://localhost:8080/api/v1/models"

# Define the JSON payload for the model
model_data = {
    "package": "com.example.models",
    "name": "Person",
    "description": "A model representing a person",
    "properties": [
        {
            "name": "id",
            "type": "Integer",
            "description": "The ID of the person"
        },
        {
            "name": "name",
            "type": "String",
            "description": "The name of the person"
        }
    ]
}

# Convert the model data to JSON
json_data = json.dumps(model_data)

# Send a POST request to the models endpoint with the JSON data
response = requests.post(url, data=json_data)

# Check the response status code to ensure the model was created successfully
if response.status_code == 201:
    print("Model created successfully")
else:
    print("Error creating model: ", response.text)
