from google.cloud import bigquery
import firebase_admin
from firebase_admin import credentials
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CREDENTIALS_PATH = os.path.join(BASE_DIR, "firebase_key.json")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)

bigquery_client = bigquery.Client()

BQ_DATASET = "leave_management"
BQ_USERS_TABLE = f"{BQ_DATASET}.users"
BQ_LEAVES_TABLE = f"{BQ_DATASET}.leaves"
