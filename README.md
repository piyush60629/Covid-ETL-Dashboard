# COVID ETL Dashboard

## Overview
The **COVID ETL Dashboard** is an end-to-end project that collects, cleans, and transforms COVID-19 data from public APIs and visualizes it through an interactive **Streamlit dashboard**.  

It demonstrates skills in **ETL processes, data analysis, PostgreSQL database management, and dashboard development**.

---

## Features
- Extracts COVID-19 data from public APIs.
- Cleans and transforms raw data using **Python** and **Pandas**.
- Loads processed data into **PostgreSQL** for querying and analysis.
- Interactive **Streamlit dashboard** to visualize daily cases, recoveries, and trends.
- Logging and error handling for reliable data processing.

---

## Technologies Used
- **Programming Language:** Python  
- **Data Processing:** Pandas  
- **Database:** PostgreSQL  
- **Dashboard:** Streamlit  
- **Other Tools:** Logging, API integration

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<yourusername>/covid-etl-dashboard.git
cd covid-etl-dashboard


## Installation

1. **Install dependencies**
```bash
pip install -r requirements.txt

2. **Set up PostgreSQL**

Create a database named covid_data.

Update database credentials in the .env file or configuration.

3. **Run the ETL pipeline**

python etl_pipeline.py


4. **Run the Streamlit dashboard**

streamlit run dashboard.py

## Project Structure

covid-etl-dashboard/
│
├── etl_pipeline.py        # ETL pipeline script
├── dashboard.py           # Streamlit dashboard script
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── data/                  # Optional folder for sample data

