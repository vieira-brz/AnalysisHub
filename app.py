import streamlit as st
from menus.LightHouseAnaliser import verify_site
from menus.About import about, developer_info
from menus.CodeAnalysis import describe_file  

# Menu principal
def main():    
    menu = ["Web Performance Analiser", "Code Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    developer_info()
    
    if choice == "Web Performance Analiser":
        verify_site()
    elif choice == "Code Analysis":
        describe_file() 
    elif choice == "About":
        about()

if __name__ == '__main__':
    main()
