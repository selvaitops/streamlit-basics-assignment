import streamlit as st
import pandas as pd


st.title("Sales Dashboard")
st.subheader("Simple app to view and filter sales data using category")

data = {
    'Product': ['Laptop', 'Shirt', 'Mobile', 'Jeans', 'Tablet', 'T-shirt'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Sales': [50000, 2000, 30000, 2500, 15000, 1800]
}

df = pd.DataFrame(data)

st.sidebar.header("Filter Options")

categories = df['Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)

filtered_df = df[df['Category'] == selected_category]

st.write(f"Showing data: {selected_category}")
st.dataframe(filtered_df)

st.write("Sales Trend")
st.line_chart(filtered_df['Sales'])
