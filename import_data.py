import streamlit as st
import pandas as pd

df = pd.read_csv("dir/aFile.csv")

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    "Press to Download",
    csv,
    "aFile.csv",
    "text/csv",
    key='download-csv'
)