import streamlit as st


st.write("Hello World")
#creating columns to easily orient objects on the page
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
 st.write("Welcome to:")
 st.title("*COOKABLE*")
# centering the slogan in the middle of the page using HTML
 
 st.markdown(
        "<h3 style='text-align:center'>Because Googling 'chicken recipe' for the 47th time is exhausting.</h3>",
        unsafe_allow_html=True,
    )

