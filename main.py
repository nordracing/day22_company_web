import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
content1 = """
Our company is the best in the Software Development.
We are working on 30+ different projects now and have 20+ active clients.
"""
st.write(content1)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row["first name"].capitalize()} {row["last name"].capitalize()}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row["first name"].capitalize()} {row["last name"].capitalize()}")
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row["first name"].capitalize()} {row["last name"].capitalize()}")
        st.write(row["role"])
        st.image("images/"+row["image"])