import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Branch': ['Branch 1', 'Branch 2', 'Branch 3', 'Branch 4', 'Branch 5', 'Branch 6', 'Branch 7', 'Branch 8', 'Branch 9', 'Branch 10'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'North', 'South'],
    'Sales': [12000, 15000, 13000, 11000, 14000, 12500, 16000, 13500, 14500, 15000],
    'Income': [8000, 9000, 8500, 7500, 8800, 8200, 9500, 8900, 8700, 9100],
    'Expenses': [4000, 6000, 4500, 3500, 5200, 4300, 5500, 4600, 5800, 5900]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Title of the app
st.title("Coffee Shop Branches Performance")

# Sidebar for filtering by region
st.sidebar.title("Filter by Region")
selected_region = st.sidebar.selectbox("Select a Region", df['Region'].unique())

# Filter data based on the selected region
filtered_data = df[df['Region'] == selected_region]

# Display the data
st.header(f"Performance of Branches in {selected_region} Region")
st.table(filtered_data)

# Plot sales, income, and expenses
fig, ax = plt.subplots(3, 1, figsize=(10, 15))

# Sales
ax[0].bar(filtered_data['Branch'], filtered_data['Sales'], color='blue')
ax[0].set_title('Sales')
ax[0].set_ylabel('Amount')

# Income
ax[1].bar(filtered_data['Branch'], filtered_data['Income'], color='green')
ax[1].set_title('Income')
ax[1].set_ylabel('Amount')

# Expenses
ax[2].bar(filtered_data['Branch'], filtered_data['Expenses'], color='red')
ax[2].set_title('Expenses')
ax[2].set_ylabel('Amount')

plt.tight_layout()
st.pyplot(fig)

# Summary statistics
st.header("Summary Statistics")
st.write(filtered_data.describe())
