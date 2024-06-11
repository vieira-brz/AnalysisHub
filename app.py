import streamlit as st
from pages.LightHouseAnaliser import verify_site

# Menu principal
def main():    
    menu = ["Lighthouse Analiser", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Lighthouse Analiser":
        verify_site()
    elif choice == "About":
        st.subheader("About")
        st.write("This app allows you to verify website scores such as performance, accessibility, and more using Streamlit and Lighthouse.")
        st.write("You can also integrate machine learning models and upload large data files for analysis.")

if __name__ == '__main__':
    main()
