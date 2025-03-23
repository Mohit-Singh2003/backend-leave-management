from google.cloud import bigquery
import firebase_admin
from firebase_admin import credentials

# Load Firebase credentials
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

# BigQuery client setup
client = bigquery.Client()

# Dataset and Table Names
BQ_DATASET = "leave_management"
BQ_USERS_TABLE = f"{BQ_DATASET}.users"
BQ_LEAVES_TABLE = f"{BQ_DATASET}.leaves"
