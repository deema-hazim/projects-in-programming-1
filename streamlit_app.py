import streamlit as st
from streamlit_option_menu import option_menu


st.title("First App")

selected = option_menu(
    menu_title=None,
    options=[
        "Introduction", "Information"
    ],
    default_index=0,
    orientation="horizontal",
)

if selected == "Introduction":
    st.write("My name is Deema. This is my first application for this class :)")
