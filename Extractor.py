from google.cloud import storage

class Extractor:

    """
    This class manage the data extraction from a GCS Bucket

    The definition of each att is:

        - bucket_name = Name of the google cloud storage bucket
        - source_blob_name = Name of the file in the bucket
        - destination_file_name = Local route with filename
    """
    
    def __init__(self, bucket_name, blob_name, destination_file_name):
        self.bucket_name = bucket_name
        self.source_blob_name = blob_name
        self.destination_file_name = destination_file_name

    def download_from_bucket(self):
        """
            Downloads a file from a bucket into local route
        """
        try:
            storage_client = storage.Client()
            bucket = storage_client.bucket(self.bucket_name)
            blob = bucket.blob(self.source_blob_name)
            blob.download_to_filename(self.destination_file_name)
        except Exception as e:
            print(f"Download failed due to Exception: {str(e)}")