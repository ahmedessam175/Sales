import numpy as np 
import pandas as pd 
import plotly.express as px 
import streamlit as st 

data=pd.read_csv('Sales.csv') 
st.write('Author:@AhmedEssam')

st.title('Sales')

st.dataframe(data.head())

col1 ,col2 = st.columns(2)

with col1 :
    fig1=px.pie(data, values='Profit' , names='Product',color_discrete_sequence=px.colors.sequential.RdBu
       ,width=500, height=400)
    st.plotly_chart(fig1)


with col2:
    fig2=px.pie(data, values='Profit' , names='week_day',width=500, height=400)
    st.plotly_chart(fig2)    


with col1:
    fig3=px.scatter(data, x="Profit", y="Price Each",
                 size="Quantity Ordered", color="City",
                  log_x=True, size_max=70,width=500, height=400)
    st.plotly_chart(fig3)


with col2:
    fig4=px.bar(data,x='week_day',y='Profit',color='Quantity Ordered',width=500, height=400)
    st.plotly_chart(fig4)


with col1:
    fig5=px.box(data,x='City',y='Price Each',width=500, height=400)
    st.plotly_chart(fig5) 



with col2:
    fig6=px.box(data,x='Price Each',y='week_day',color='Quantity Ordered',width=500, height=400)
    st.plotly_chart(fig6)

























