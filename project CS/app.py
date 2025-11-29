import streamlit as st

# using HTML and CSS to make the title big and centered 
st.markdown(
    """
    <style>
      .big-title { font-size: clamp(42px, 8vw, 96px); font-weight: 800; text-align: center; margin: 0; }
      .big-sub   { font-size: clamp(18px, 3vw, 28px); color: #555; text-align: center; margin: 6px 0 18px 0; }
    </style>
    <div style="width: 100%;">
      <div class="big-title">COOKABLE</div>
    </div>
    """,
    unsafe_allow_html=True,
)

#creating columns to center the welcome statement
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  st.markdown("### Because googling 'chicken recipe' for the 47th time is exhausting.")
  st.markdown("---")
  