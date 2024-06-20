import json
import pandas as pd
import os
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up GCP client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
client = storage.Client()
bucket = client.get_bucket('weather_bucket01')

# Load data from GCS
blob = bucket.blob('weather_data.json')
data = json.loads(blob.download_as_string())

# Flatten the JSON data
flattened_data = {
    'city_name': data['name'],
    'temperature': data['main']['temp'],
    'pressure': data['main']['pressure'],
    'humidity': data['main']['humidity'],
    'wind_speed': data['wind']['speed'],
    'timestamp': data['dt']
}

# Convert to DataFrame
df = pd.DataFrame([flattened_data])

# Save processed data back to GCS
processed_blob = bucket.blob('processed_weather_data.json')
processed_blob.upload_from_string(df.to_json(orient='records'), 'application/json')

print("Data processed and saved to GCS successfully!")
