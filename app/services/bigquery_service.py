from google.cloud import bigquery
from utils.bigquery_utils import get_bigquery_client

def execute_query(query: str) -> list[dict]:
    """
    Execute a given SQL query on BigQuery and return the results.
    """
    client = get_bigquery_client()
    job = client.query(query)
    results = job.result()
    
    return [dict(row) for row in results]

def insert_row(dataset_id: str, table_id: str, row_data: dict) -> None:
    """
    Insert a single row into a specific BigQuery table.
    """
    client = get_bigquery_client()
    table_ref = client.dataset(dataset_id).table(table_id)
    errors = client.insert_rows_json(table_ref, [row_data])

    if errors:
        raise Exception(f"Encountered errors while inserting row: {errors}")

def fetch_all_rows(dataset_id: str, table_id: str) -> list[dict]:
    """
    Fetch all rows from a specific BigQuery table.
    """
    query = f"SELECT * FROM `{dataset_id}.{table_id}`"
    return execute_query(query)
