import pandas as pd

class Transformer:
    def transform_data(self, source_file_path, destination_file_path):
        """
            Transforms data into CSV
        """
        try:
            data = pd.read_csv(source_file_path)
            # Transformations required
            transformed_data = data  # Example: No transformations in this case

            transformed_data.to_csv(destination_file_path, index=False)
            print(f"Transformed data storaged in: {destination_file_path}.")
        except Exception as e:
            print(f"Error transforming data: {str(e)}")
