pip install matplotlib
pip install pandas


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Branch': ['Branch 1', 'Branch 2', 'Branch 3', 'Branch 4', 'Branch 5', 'Branch 6', 'Branch 7', 'Branch 8', 'Branch 9', 'Branch 10'] * 12,
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South'] * 12,
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] * 10,
    'Sales': [12000, 15000, 13000, 11000, 14000, 12500, 16000, 13500, 14500, 15000,
              13000, 16000, 14000, 12000, 15000, 13500, 17000, 14500, 15500, 16000] * 6,
    'Income': [8000, 9000, 8500, 7500, 8800, 8200, 9500, 8900, 8700, 9100,
               9000, 10000, 9500, 8500, 9800, 9200, 10500, 9900, 9700, 10100] * 6,
    'Expenses': [4000, 6000, 4500, 3500, 5200, 4300, 5500, 4600, 5800, 5900,
                 4000, 6000, 4500, 3500, 5200, 4300, 5500, 4600, 5800, 5900] * 6
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Profit'] = df['Income'] - df['Expenses']

# Title of the app
st.title("Coffee Shop Branches Performance")

# Sidebar for filtering
st.sidebar.title("Filters")

# Region filter
selected_region = st.sidebar.multiselect("Select Region(s)", df['Region'].unique(), default=df['Region'].unique())

# Branch filter
selected_branch = st.sidebar.multiselect("Select Branch(es)", df['Branch'].unique(), default=df['Branch'].unique())

# Month filter
selected_month = st.sidebar.multiselect("Select Month(s)", df['Month'].unique(), default=df['Month'].unique())

# Filter data based on selections
filtered_data = df[
    (df['Region'].isin(selected_region)) & 
    (df['Branch'].isin(selected_branch)) & 
    (df['Month'].isin(selected_month))
]

# Display the sales data table
st.header("Sales Data")
st.table(filtered_data[['Branch', 'Region', 'Month', 'Sales']])

# Plot sales data
st.header("Sales Chart")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filtered_data['Branch'], filtered_data['Sales'], color='blue')
ax.set_title('Sales')
ax.set_ylabel('Amount')
plt.xticks(rotation=45)
st.pyplot(fig)

# Display the income, expense, and profit table
st.header("Income, Expense, and Profit Data")
st.table(filtered_data[['Branch', 'Region', 'Month', 'Income', 'Expenses', 'Profit']])

# Plot income and expense data
st.header("Income and Expense Chart")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(filtered_data['Branch'], filtered_data['Income'], color='green', label='Income')
ax.bar(filtered_data['Branch'], filtered_data['Expenses'], color='red', label='Expenses')
ax.set_title('Income and Expenses')
ax.set_ylabel('Amount')
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)

# Summary statistics
st.header("Summary Statistics")
st.write(filtered_data.describe())
