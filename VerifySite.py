import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Function to run the Lighthouse analysis
def run_lighthouse(url):
    # Ensure Lighthouse CLI is in the PATH
    lighthouse_path = 'lighthouse'  # Assuming it's in the PATH
    result = subprocess.run(
        [lighthouse_path, url, '--output', 'json', '--output-path', 'report.json'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    if result.returncode == 0:
        with open('report.json', 'r') as file:
            report = json.load(file)
        return report
    else:
        st.error(result.stderr.decode())
        return None

# Streamlit UI
st.title("Lighthouse Analysis Tool")
url = st.text_input("Enter the URL to analyze:")

if st.button("Analyze page load"):
    if url:
        with st.spinner('Running Lighthouse analysis...'):
            report = run_lighthouse(url)
        
        if report:
            st.success("Lighthouse analysis completed successfully.")
            
            # Extract and display Lighthouse report data
            scores = {}
            categories = ['performance', 'accessibility', 'best-practices', 'seo', 'pwa']
            for category in categories:
                if category in report['categories']:
                    scores[category.capitalize()] = report['categories'][category]['score'] * 100
            
            # Plot the scores as a pie chart
            df = pd.DataFrame(scores.items(), columns=['Category', 'Score'])
            fig, ax = plt.subplots()
            ax.pie(df['Score'], labels=df['Category'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig)
        else:
            st.error("Lighthouse analysis failed.")
    else:
        st.warning("Please enter a URL.")