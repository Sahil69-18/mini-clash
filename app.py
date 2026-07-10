import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mini Clash", layout="centered")

# This reads your index.html file and displays it inside Streamlit
with open("index.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=650, scrolling=False)
