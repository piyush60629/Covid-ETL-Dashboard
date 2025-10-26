COVID ETL Dashboard
Overview

The COVID ETL Dashboard is an end-to-end data pipeline project that collects, cleans, and transforms COVID-19 data from public APIs and visualizes it through an interactive Streamlit dashboard. This project demonstrates skills in ETL processes, data analysis, PostgreSQL database management, and dashboard development.

Features

Data Extraction: Collects COVID-19 data from reliable public APIs.

Data Transformation: Cleans and transforms raw data using Python and Pandas for accurate analysis.

Data Loading: Loads processed data into a PostgreSQL database for easy querying and storage.

Dashboard Visualization: Interactive Streamlit dashboard to visualize daily cases, recoveries, and trends.

Reliability: Includes logging and error handling to ensure accurate and consistent data processing.

Technologies Used

Programming Language: Python

Data Processing: Pandas

Database: PostgreSQL

Dashboard: Streamlit

Others: Logging, API integration

Installation

Clone the repository:

git clone https://github.com/<yourusername>/covid-etl-dashboard.git
cd covid-etl-dashboard


Install dependencies:

pip install -r requirements.txt


Set up PostgreSQL:

Create a database named covid_data.

Update database credentials in the configuration file or .env file.

Run the ETL script:

python etl_pipeline.py


Run the Streamlit dashboard:

streamlit run dashboard.py

Project Structure
covid-etl-dashboard/
│
├── etl_pipeline.py        # ETL pipeline script
├── dashboard.py           # Streamlit dashboard script
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── data/                  # Optional folder for sample data

Usage

Visit the Streamlit dashboard URL in your browser after running dashboard.py.

Explore daily cases, recoveries, and trends in COVID-19 data.

The dashboard updates automatically based on the latest ETL pipeline run.
