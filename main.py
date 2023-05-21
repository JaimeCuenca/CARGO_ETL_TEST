from etl.Orchestrator import ETLWorkflow

# ETL configuration
bucket_name = "name of the bucket in GCS"
source_blob_name = "name of the file in the bucket"
local_file_path = "path where we want to download the file + the name of the file"
dataset_id = "id of he dataset"
table_name = "name of the table to upload to bigquery"

# ETL execution
etl_workflow = ETLWorkflow(bucket_name, source_blob_name, local_file_path, dataset_id, table_name)
etl_workflow.run()
