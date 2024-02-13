from driver import img_create
import streamlit as st
st.title("SpriteAI ")
desc = st.text_input("Enter a description here")


st.caption("Enter a physical description of a person, be as descriptive as possible!")
submit = st.button("Submit🚀")
if submit:
    st.header("Result 👉🏻")
    st.image(img_create(description=desc))
    
st.link_button("Built by Nirbhay S.", "https://www.nirbhaysinghnarang.com")