import streamlit as st
import random

st.set_page_config(page_title="Flip Tee Finder", page_icon="👕")
st.title("👕 Flip Tee Finder")

uploaded = st.file_uploader("Upload a T-shirt photo", type=["jpg","jpeg","png"])

if uploaded:
    st.image(uploaded, caption="Your T-shirt", use_column_width=True)
    score = random.randint(40, 95)
    st.metric("Quick-Flip Score", f"{score}/100")

    low = int(20 + score*0.8)
    high = int(50 + score*1.8)
    st.write(f"💰 Estimated resale range: **${low} – ${high}**")

    st.subheader("Listing Helper")
    st.write("""
    - Take clear photos of front, back, and tag  
    - Note size & condition  
    - Add keywords: band, vintage, Harley, Nintendo  
    """)
