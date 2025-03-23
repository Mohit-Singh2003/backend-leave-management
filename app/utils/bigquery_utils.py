from google.cloud import bigquery
import os

def get_bigquery_client() -> bigquery.Client:
    """
    Initializes and returns a BigQuery client using credentials from the environment.
    """
    # Optional: Set your GOOGLE_APPLICATION_CREDENTIALS here if needed
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"

    client = bigquery.Client()
    return client
