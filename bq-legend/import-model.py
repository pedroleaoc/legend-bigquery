import json
import requests
from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Define the BigQuery table name and dataset
table_name = "my_dataset.my_table"
dataset_id, table_id = table_name.split(".")

# Get the data from the BigQuery table
table_ref = client.dataset(dataset_id).table(table_id)
rows = client.list_rows(table_ref)
data = [dict(row) for row in rows]

# Save the data to a file in JSON format
with open("table_data.json", "w") as f:
    json.dump(data, f)

# Define the Legend API endpoint and headers
url = "http://localhost:8080/api/v1/entities"
headers = {"Content-Type": "application/json"}

# Load the data from the JSON file and create a Legend model
with open("table_data.json", "r") as f:
    data = json.load(f)
model = {
    "name": table_name,
    "class": {
        "name": table_name,
        "id": table_name,
        "properties": [
            {"name": k, "type": str(type(v).__name__).lower()} for k, v in data[0].items()
        ]
    }
}

# Send a PUT request to the entities endpoint with the model payload
response = requests.put(url, headers=headers, json=model)

# Check the response status code to ensure the import was successful
if response.status_code == 200:
    print("Legend model imported successfully")
else:
    print("Error importing Legend model: ", response.text)
