import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Belajar Analisis Data')

st.write(
    pd.DataFrame({
        'c1': [1, 2, 3],
        'c2': [4, 5, 6],
    })
)

st.markdown(
    """
    # My First App
    Hello, para calon praktisi data masa depan!
    """
)


st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
st.caption('Copyright (c) 2025')


code = """
def hello():
    print('Hello World!')
"""
st.code(code, language='python')

st.text("Halo, calon praktisi data masa depan!")


st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")


df = pd.DataFrame({
    'c1': [1, 2, 3,4],
    'c2': [10, 20,30,40],
})

st.dataframe(data=df, width=500, height=150)

st.table(df)

st.metric(
    label='Temperature',
    value='28 °C',
    delta="1.2 °C"
)

st.json({
    'c1': [1, 2, 3],
    'c2': [4, 5, 6],
})

n = np.random.normal(15,5, 250)

fig, ax = plt.subplots()
ax.hist(n, bins=15)
st.pyplot(fig)
