import streamlit as st
import pandas as pd
import plotly.express as px
import statistics as ss

vehicles  = pd.read_csv("vehicles_us.csv")

vehicles['cylinders'] = vehicles['cylinders'].fillna(ss.median(vehicles['cylinders']))

vehicles1 = vehicles.groupby(['model','model_year'])['cylinders'].median().reset_index()
vehicles2 = vehicles.merge(vehicles1,how='left')



auto_only = vehicles2[vehicles2["transmission"] == "automatic"]

st.header("Data Viewer")

automatic = st.checkbox("View vehicles with only automatic transmission")

if automatic:
    st.write(auto_only)
else:
    st.write(vehicles2) 


st.header("Prices per Car Model Year")

# Correct variable names
fig = px.scatter(vehicles2, x="model_year", y="price", color = 'type')

event1 = st.plotly_chart(fig,use_container_width=True,theme="streamlit")

st.header('Price per Car Model Condition')

fig1 = px.bar(vehicles2, x='condition', y='price', color = 'type')

event2 = st.plotly_chart(fig1,use_container_width=True,theme="streamlit")

st.header("Histogram of type vs days_listed")

show_hist = st.checkbox("Show histogram")

if show_hist:
    fig2 = px.histogram(vehicles2, x='days_listed', nbins=100, labels={'x': 'Days Listed', 'y': 'Count'}, color ='type')
    event3 = st.plotly_chart(fig2,use_container_width=True,theme="streamlit")
    