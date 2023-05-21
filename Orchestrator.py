from etl.Extractor import Extractor
from etl.Transformer import Transformer
from etl.Exporter import Exporter

class ETLWorkflow:

    """
        This class orchestrates the flow of the ETL
            - Extraction from the class extractor
            - Transformations from the class transformer
            - Exportation to Bigquery with the class exporter
    """

    def __init__(self, bucket_name, source_blob_name, local_file_path, dataset_id, table_name):
        self.bucket_name = bucket_name
        self.source_blob_name = source_blob_name
        self.local_file_path = local_file_path
        self.dataset_id = dataset_id
        self.table_name = table_name

    def run(self):
        # 1: Extract data from Google Cloud Storage's bucket
        extractor = Extractor(self.bucket_name, self.source_blob_name, self.local_file_path)
        extractor.download_from_bucket()

        # 2: Transform extracted data
        transformer = transformer()
        transformed_file_path = self.local_file_path + ".csv"  # Adds the .csv extension to the file
        transformer.transform_data(self.local_file_path, transformed_file_path)

        # 3: Export transformed data to Bigquery
        exporter = exporter(self.dataset_id, self.table_name)
        exporter.export_to_bigquery(transformed_file_path)

        print("ETL workflow finished with 0 errors.")