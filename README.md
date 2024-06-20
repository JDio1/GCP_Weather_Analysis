# Weather Data Pipeline

## Project Overview
This project is a Weather Data Pipeline that fetches weather data from OpenWeatherMap, processes the data, and loads it into Google BigQuery for analysis and visualization.

## Setup Instructions

### Prerequisites
- Python 3.6+
- Google Cloud SDK
- OpenWeatherMap API Key
- Google Cloud Project with BigQuery and Cloud Storage enabled

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/JDio1/GCP_Weather_Analysis.git
   cd weather-data-pipeline

2. **Set Up Virtual Environment (Optional but recommended)**:
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install Dependencies**:
    pip install -r requirements.txt


4. **Set Environment Variables**:
    Create a .env file in the project root directory and add the following:
    GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-file.json
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key

5. **Fetch Weather Data**:
    python src/fetch_weather_data.py


6. **Process Weather Data**:
    python src/process_weather_data.py


7. **Load Data into BigQuery**:
    python src/load_data_to_bigquery.py

## Project Structure
    src/fetch_weather_data.py: Script to fetch weather data from OpenWeatherMap.
    src/process_weather_data.py: Script to process and flatten the fetched data.
    src/load_data_to_bigquery.py: Script to load processed data into BigQuery.
    requirements.txt: Python dependencies.
    .gitignore: Files to be ignored by Git.
    README.md: Project documentation.


