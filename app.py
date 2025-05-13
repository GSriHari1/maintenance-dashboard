import streamlit as st
import pandas as pd
from datetime import datetime

@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    return df

st.set_page_config(page_title="Preventive Maintenance Dashboard", layout="wide")
st.title("🛠 Preventive Maintenance Dashboard")

df = load_data()

st.sidebar.header("Filter by")
machine = st.sidebar.multiselect("Machine", options=df["Machine"].unique(), default=df["Machine"].unique())
status = st.sidebar.multiselect("Status", options=df["Status"].unique(), default=df["Status"].unique())

filtered_df = df[(df["Machine"].isin(machine)) & (df["Status"].isin(status))]

st.subheader("Maintenance Task Overview")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("Task Summary")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Tasks", len(df))
with col2:
    st.metric("Pending", len(df[df["Status"] == "Pending"]))