import os
from google.cloud import bigquery
from google.cloud import storage
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up GCP clients
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
storage_client = storage.Client()
bigquery_client = bigquery.Client()

# Load processed data from GCS
bucket = storage_client.get_bucket('weather_bucket01')
blob = bucket.blob('processed_weather_data.json')
data = json.loads(blob.download_as_string())

# Define BigQuery dataset and table
dataset_id = 'weather_dataset'
table_id = 'weather_analysis'
table_ref = bigquery_client.dataset(dataset_id).table(table_id)

# Define schema
schema = [
    bigquery.SchemaField("city_name", "STRING"),
    bigquery.SchemaField("temperature", "FLOAT"),
    bigquery.SchemaField("pressure", "INTEGER"),
    bigquery.SchemaField("humidity", "INTEGER"),
    bigquery.SchemaField("wind_speed", "FLOAT"),
    bigquery.SchemaField("timestamp", "TIMESTAMP"),
]

# Load data to BigQuery
job_config = bigquery.LoadJobConfig(schema=schema)
job = bigquery_client.load_table_from_json(data, table_ref, job_config=job_config)
job.result()

print("Data loaded to BigQuery successfully!")
