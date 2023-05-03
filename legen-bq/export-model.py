import requests

# Define the endpoint URL
url = "http://localhost:8080/api/v1/entities/export"

# Define the query parameters for the export
query_params = {
    "package": "com.example.models",
    "entities": "Person",
    "format": "json"
}

# Send a GET request to the export endpoint with the query parameters
response = requests.get(url, params=query_params)

# Check the response status code to ensure the export was successful
if response.status_code == 200:
    # Write the exported model to a file
    with open("exported_model.zip", "wb") as f:
        f.write(response.content)
    print("Model exported successfully")
else:
    print("Error exporting model: ", response.text)
