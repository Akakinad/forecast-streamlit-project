
import streamlit as st
import pandas as pd

# Read the uploaded CSV file (this is for local use, update path if necessary)
df = pd.read_csv('forecast_data.csv')

# Title of the Streamlit app
st.title('Forecast Data Display')

# Show the DataFrame in the Streamlit app
st.write('### Data Preview')
st.write(df.head())

# Example: Basic line chart for unit_sales over time
st.write('### Unit Sales Over Time')
st.line_chart(df.set_index('item_nbr')['unit_sales'])
