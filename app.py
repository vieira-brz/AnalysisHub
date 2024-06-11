import streamlit as st
from menus.LightHouseAnaliser import verify_site
from menus.About import about

# Menu principal
def main():    
    menu = ["About", "Web Performance Analiser"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Web Performance Analiser":
        verify_site()

    elif choice == "About":
        about()

if __name__ == '__main__':
    main()