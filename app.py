import streamlit as st
import math
import pandas as pd

st.title("Complexity Visualizer")

n = st.slider("Enter N", 1, 200, 10)

x = list(range(1, n + 1))

data = {
    "n": x,
    "O(1)": [1 for _ in x],
    "O(log n)": [round(math.log2(i), 2) for i in x],
    "O(n)": x,
    "O(n log n)": [round(i * math.log2(i), 2) for i in x],
    "O(n²)": [i * i for i in x]
}

df = pd.DataFrame(data)

st.dataframe(df)