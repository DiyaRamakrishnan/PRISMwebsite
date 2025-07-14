import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aid2Day Inspired Site", layout="wide")

# You can replace this with your actual logo or banner
st.markdown("<h1 style='text-align: center; color: #1F77B4;'>Welcome to Our Mission</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Together we build a better future.</h3>", unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1, 1])
with col1:
    st.image("https://images.unsplash.com/photo-1509099836639-18ba1795216d", use_column_width=True)
with col2:
    st.markdown("""
        ### Our Goal  
        We empower underserved communities through actionable programs and global collaboration.  
        Whether you're here to **volunteer**, **donate**, or **learn**, you’re in the right place.  
        
        👉 Use the sidebar to navigate and learn more.
    """)
