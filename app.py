import streamlit as st

st.title("Complexity Visualizer")

algorithms = {
    "Bubble Sort": "O(n²)",
    "Merge Sort": "O(n log n)",
    "Binary Search": "O(log n)"
}

algo = st.selectbox("Select Algorithm", list(algorithms.keys()))

if st.button("Visualize"):
    st.success(f"{algo}")
    st.write("Time Complexity:", algorithms[algo])