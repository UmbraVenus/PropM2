import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome to Zillow Killer :D")
try:
    df = pd.read_csv("listings.csv")
    st.dataframe(df)
except pd.errors.EmptyDataError:
    st.write("No Data Yet")
