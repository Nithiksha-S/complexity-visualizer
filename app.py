import streamlit as st

st.set_page_config(page_title="Complexity Visualizer")

st.title("Complexity Visualizer")
st.write("Welcome to Complexity Visualizer")

algo = st.selectbox(
    "Select Algorithm",
    ["Bubble Sort", "Merge Sort", "Binary Search"]
)

if st.button("Visualize"):
    st.success(f"{algo} visualization loaded")