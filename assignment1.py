import numpy as np
import pandas as pd
import streamlit as st

st.title("This is my first Assignment")
st.write("All the students do it for the cloud computing")

data = pd.DataFrame(
    {'Names': ['Hamoud','Ali','Abdullah','Hussain','Ahmed','Salman','Mohammed','Ibrahim'],
     'Grades': [21,18,19,20,23,19,11,23]})

st.write("Following is student details:")
st.write(data)
chart_data = pd.DataFrame(
    np.random.randn(20,4),
    columns=['A','B','C','D']
)

st.bar_chart(chart_data)