# legend-bigquery
POC to integrate FINOS Legend with BigQuery.

## Dataflow 
```
      (I)        (II)
Legend > BigQuery > Legend
```
(I) Legend model to BigQuery table

a. How to extract the model from Legend?

b. How to create GCP services from within a K8s pod runing in GKE? 

c. How to copy the JSON to BigQuery? 

(II) BigQuery to Legend
a. How to copy the JSON form BigQuery to Legend?

## Braindump

(I)
- Create a dataset in BigQuery.
- Create a table in BigQuery using a JSON schema file.
- Transfer the JSON file to Google Cloud Storage (GCS) using the kubectl cp and gsutil cp commands.
- Import the JSON file into BigQuery using the bq load command.

1. Create a dataset in BigQuery: 
   ```
   bq mk <dataset-name>
   ```

2. Create a table in BigQuery:
   ```
   bq mk --table <dataset-name>.<table-name> <schema-file>
   ```
   
   `<schema-file>` should be the path to a JSON file that describes the schema of the table.

3. Transfer the JSON file to GCS:
   ```
   gsutil cp <local-directory>/<json-file> gs://<bucket-name>/<object-name>
   ```

4. Import the JSON file into BigQuery:
   ```
   bq load --source_format=NEWLINE_DELIMITED_JSON <dataset-name>.<table-name> gs://<bucket-name>/<object-name> <schema-file>
   ```
