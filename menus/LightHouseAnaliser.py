import streamlit as st
import requests

def run_pagespeed_insights(url, api_key):
    params = {
        'url': url,
        'key': api_key
    }
    response = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed', params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Failed to analyze page. Error: {response.status_code}")
        return None

def verify_site():
    st.title("Insights Analysis Tool")
    url = st.text_input("Enter the URL to analyze:")
    api_key = "AIzaSyD1JcoPPOF8z2KhYI4e6blZlMmZptplbL4"  # Substitua isso pela sua chave de API

    if st.button("Analyze page load"):
        if url:
            with st.spinner('Analyzing page load...'):
                report = run_pagespeed_insights(url, api_key)
            
            if report:
                st.success("Page load analysis completed successfully.")
                
                # Extract and display PageSpeed Insights data
                if 'lighthouseResult' in report:
                    scores = {}
                    categories = report['loadingExperience']['metrics']
                    for category, data in categories.items():
                        scores[category.capitalize()] = data['category']
                    
                    # Plot the scores as a bar chart
                    st.bar_chart(scores)
                else:
                    st.error("No PageSpeed Insights data available for this URL.")
        else:
            st.warning("Please enter a URL.")