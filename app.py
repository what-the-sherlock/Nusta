import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image comparison", layout="centered")

st.title("OHRC images")

st.markdown("1.")

image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Original",
    label2="Enhanced"
)

