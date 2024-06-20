import os
import requests
import json
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up GCP client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
client = storage.Client()
bucket = client.get_bucket('weather_bucket01')

# OpenWeatherMap API details
api_key = os.getenv('OPENWEATHERMAP_API_KEY')
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# City for which you want to fetch weather data
city_name = 'Lagos'
complete_url = base_url + 'appid=' + api_key + '&q=' + city_name

# Fetching the data
response = requests.get(complete_url)
data = response.json()

# Saving to Google Cloud Storage
blob = bucket.blob('weather_data.json')
blob.upload_from_string(json.dumps(data), 'application/json')

print("Data fetched and saved to GCS successfully!")
