import requests
import json

# Define the endpoint URL
url = "http://localhost:8080/api/v1/entities/schema"

# Define the query parameters for the schema export
query_params = {
    "package": "com.example.models",
    "entity": "Person",
    "format": "json"
}

# Send a GET request to the schema endpoint with the query parameters
response = requests.get(url, params=query_params)

# Check the response status code to ensure the export was successful
if response.status_code == 200:
    # Parse the JSON response
    schema = json.loads(response.text)
    # Print the schema definition
    print(schema)
else:
    print("Error exporting schema: ", response.text)
