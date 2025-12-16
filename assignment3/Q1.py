import pandas as pd 
import streamlit as st 
import pandasql as ps

st.title("CSV Explorer !!")

data_file = st.file_uploader("Upload a CSV file",type = ["csv"])
if data_file:
    df = pd.read_csv(data_file)
    st.dataframe(df)
    query = "select job, SUM(sal) total from data GROUP BY job"
    result = ps.sqldf(query,{"data":df})
    st.write(result)