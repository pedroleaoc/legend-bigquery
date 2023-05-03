from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Define the BigQuery table name and dataset
table_name = "my_dataset.my_table"
dataset_id, table_id = table_name.split(".")

# Get the schema for the BigQuery table
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)
schema = table.schema

# Print the schema fields
for field in schema:
    print(field.name, field.field_type)
