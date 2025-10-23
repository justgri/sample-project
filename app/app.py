import streamlit as st
import pandas as pd
from pathlib import Path


st.title("Sample Project")

st.header("Hello world!")

st.markdown("Some additional text")


ROOT = Path(__file__).parent  # .../app
df_disney = pd.read_csv(ROOT / "data" / "disney_movies_clean.csv")


# df_disney = pd.read_csv("data/disney_movies_clean.csv")
# df_disney = pd.read_csv("app/data/disney_movies_clean.csv")


st.dataframe(df_disney)

st.header("Project Intro")

st.header("Data overview")

col_data, _, col_chart = st.columns((0.8, 0.05, 1))

with col_data:
    st.subheader("Raw Data")
    st.dataframe(df_disney)

with col_chart:
    st.subheader("Data Overview")
    st.markdown("Placeholder for chart")
