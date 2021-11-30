import streamlit as st

st.title("my application")
st.markdown("my application 2")

st.sidebar.text("hello sidebar")

button = st.button("click me")
if button:
    st.balloons()