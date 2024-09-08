import streamlit as st
from streamlit_image_comparison import image_comparison

st.set_page_config(page_title="Image comparison", layout="centered")

st.title("OHRC images")

st.markdown("1.")

image_comparison(
    img1="https://github.com/what-the-sherlock/Nusta/blob/25eec79cacb85936b567e56bbaad2b168ebc6c19/WhatsApp%20Image%202024-09-08%20at%2013.50.28_b4fa08cc.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Original",
    label2="Enhanced"
)

