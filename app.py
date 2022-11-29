"""Small example streamlit application."""
import streamlit as st

def app():
    """Define main application entry point."""
    st.title("Minimal Streamlit Template")
    # And write the rest of the app inside this function!
    st.markdown("Here is where you can insert more text.")
    st.markdown("""Streamlit works more on the basis of 
\"insert things and let Streamlit figure out how to render 
them\".  If you want more flexibility for how to render
the markdown and other elements on your webpage, 
you may want to consider
[Flask](https://flask.palletsprojects.com/).""")

    st.sidebar.markdown("""You can put things in the sidebar:
* Like lists
* Or other things""")

if __name__ == '__main__':
    app()
