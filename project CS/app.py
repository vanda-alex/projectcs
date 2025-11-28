import streamlit as st

st.markdown(
    """
    <style>
      .big-title { font-size: clamp(42px, 8vw, 96px); font-weight: 800; text-align: center; margin: 0; }
      .big-sub   { font-size: clamp(18px, 3vw, 28px); color: #555; text-align: center; margin: 6px 0 18px 0; }
    </style>
    <div style="width: 100%;">
      <div class="big-title">*COOKABLE*</div>
      <div class="big-sub">Because Googling 'chicken recipe' for the 47th time is exhausting.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Optional: keep small column section for other content
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.write("Welcome to")