import streamlit as st
import pandas as pd
import plotly.express as px
from constants import FILE

df = pd.read_csv(FILE)

st.title('Projeto prático do tutorial da Python Brasil')
st.markdown("## Nutrition Facts for McDonald's Menu")

categories = df['Category'].unique().tolist()

st.markdown("### Describe")
if st.checkbox('Apresentar describe símples'):
    st.write(df.describe())
if st.checkbox('Apresentar describe agrupado por categoria'):
    category = st.selectbox(
        'Selecione uma categoria para mostrar um describe da categoria.',
        categories
    )
    st.write(df.loc[df['Category']==category].describe())

if st.checkbox('Mostrar dataframe'):
    st.dataframe(df)
if st.checkbox('Mostrar dataframe como tabela'):
    st.table(df)

columns = categories = df.columns.tolist()
column = st.selectbox(
        'Selecione uma coluna para plotar o histograma.',
        columns
    )

fig = px.histogram(df, x=column)
st.plotly_chart(fig)