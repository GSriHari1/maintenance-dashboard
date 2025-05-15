import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Preventive Maintenance Dashboard", layout="wide")

# Load data
df = pd.read_csv("data.csv")

# Sidebar filters
st.sidebar.header("Filter by")
machines = st.sidebar.multiselect("Machine", df["Machine"].unique(), default=df["Machine"].unique())
statuses = st.sidebar.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())

# Filter data
filtered_df = df[(df["Machine"].isin(machines)) & (df["Status"].isin(statuses))]

# Main title
st.markdown("## 🛠️ Preventive Maintenance Dashboard")

# Maintenance Task Overview
st.markdown("### Maintenance Task Overview")
# st.dataframe(filtered_df.reset_index(drop=True).rename_axis('Row').reset_index().assign(Row=lambda d: d['Row'] + 1))
st.dataframe(
    filtered_df.reset_index(drop=True)
    .rename_axis("Row")
    .reset_index()
    .assign(Row=lambda d: d["Row"] + 1)
    .set_index("Row")
)

# Pie Chart
st.markdown("### Task Status Distribution")
status_counts = filtered_df["Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

if not status_counts.empty:
    fig = px.pie(status_counts, names="Status", values="Count", title="Maintenance Status Breakdown", color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No data available for the selected filters.")

# Task Summary
st.markdown("### Task Summary")
total_tasks = len(filtered_df)
pending_tasks = len(filtered_df[filtered_df["Status"] == "Pending"])
col1, col2 = st.columns(2)
col1.metric("Total Tasks", total_tasks)
col2.metric("Pending", pending_tasks)
