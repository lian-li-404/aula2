import pandas as pd
import streamlit as st

df = pd.read_csv(r"C:\Users\elian.oliveira\Desktop\aulas\aula_1\teste.csv",sep=';')
st.table(df)