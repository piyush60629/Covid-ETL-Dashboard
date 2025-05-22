import pandas as pd
import streamlit as st

# Load the ETL result
df = pd.read_csv("india_covid_summary.csv")

st.title("COVID-19 State-wise Summary for India")

# Show table
st.dataframe(df)

# Show bar chart of confirmed cases
st.subheader("Confirmed Cases by State")
st.bar_chart(data=df, x="Province_State", y="Confirmed")

# Show death rate
st.subheader("Death Rate by State (%)")
st.line_chart(data=df, x="Province_State", y="Death_Rate_%")
