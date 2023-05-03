from google.cloud import bigquery
import json

# Load the Legend schema from a JSON file
with open("legend_schema.json", "r") as f:
    schema = json.load(f)

# Initialize the BigQuery client
client = bigquery.Client()

# Define the BigQuery table schema from the Legend schema
table_schema = []
for field in schema:
    field_name = field["name"]
    field_type = field["type"]
    field_mode = "NULLABLE"
    table_field = bigquery.SchemaField(field_name, field_type, mode=field_mode)
    table_schema.append(table_field)

# Define the BigQuery table name and dataset
table_name = "my_dataset.my_table"
dataset_id, table_id = table_name.split(".")

# Define the BigQuery table object
table_ref = client.dataset(dataset_id).table(table_id)
table = bigquery.Table(table_ref, schema=table_schema)

# Create the BigQuery table
try:
    table = client.create_table(table)
    print(f"Table {table_id} created")
except Exception as e:
    print(f"Error creating table: {e}")
