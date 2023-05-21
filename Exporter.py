from google.cloud import bigquery

class Exporter:
    def __init__(self, dataset_id, table_name):
        self.dataset_id = dataset_id
        self.table_name = table_name

    def export_to_bigquery(self, file_path):
        """
            Exports a CSV to Bigquery
        """
        try:
            client = bigquery.Client()
            dataset_ref = client.dataset(self.dataset_id)
            table_ref = dataset_ref.table(self.table_name)

            job_config = bigquery.LoadJobConfig()
            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.skip_leading_rows = 1  # If CSV has headers, change to 1

            with open(file_path, "rb") as source_file:
                job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

            job.result()

            print(f"Data exported {self.table_name} to BigQuery.")
        except Exception as e:
            print(f"Error exporting data to BigQuery: {str(e)}")
