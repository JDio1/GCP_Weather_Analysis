# Weather Data Pipeline

## Project Overview
This project is a Weather Data Pipeline that fetches weather data from OpenWeatherMap, processes the data, and loads it into Google BigQuery for analysis and visualization.

This project demonstrates a data engineering pipeline built using Python and Google Cloud Platform (GCP) services. The pipeline fetches weather data from the OpenWeatherMap API, processes it, and stores it in Google Cloud Storage for further analysis and visualization. It is a great example of how to work with public APIs, handle data processing, and utilize cloud storage solutions.

## Purpose

The primary purpose of this project is to showcase a practical application of data engineering skills by building an end-to-end data pipeline. It provides a concrete example of how to automate the collection, processing, and storage of weather data using modern cloud technologies and Python programming.

## Problem It Solves

Weather data is crucial for various applications, including agriculture, disaster management, transportation, and daily life planning. However, accessing and processing this data efficiently can be challenging. This project solves the problem by automating the entire workflow:
- **Data Collection**: Fetching real-time weather data from OpenWeatherMap API.
- **Data Processing**: Parsing and structuring the raw data.
- **Data Storage**: Storing the processed data in Google Cloud Storage for easy access and analysis.

## Interesting Aspects

- **API Integration**: Demonstrates how to integrate and fetch data from a third-party API (OpenWeatherMap).
- **Cloud Storage**: Utilizes Google Cloud Storage to store and manage large datasets.
- **Python Scripting**: Uses Python scripts to automate the data pipeline, showcasing efficient data handling and processing techniques.
- **Environment Management**: Implements environment variables and `dotenv` for secure management of API keys and service account credentials.

## Technologies Used

- **Programming Language**: Python
- **Cloud Platform**: Google Cloud Platform (GCP)
- **Services**: Google Cloud Storage
- **API**: OpenWeatherMap API
- **Libraries**:
  - `google-cloud-storage`: Google Cloud Storage client library
  - `requests`: HTTP library for making API calls
  - `python-dotenv`: For loading environment variables from a `.env` file
  - `pandas`: For data manipulation and analysis
  - `db-dtypes`: For handling database-specific data types in pandas

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


