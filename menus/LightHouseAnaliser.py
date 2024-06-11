import streamlit as st
import json
import matplotlib.pyplot as plt
import subprocess
from weasyprint import HTML
from bs4 import BeautifulSoup
import requests

# Configuração do Streamlit para fundo transparente
st.set_option('deprecation.showPyplotGlobalUse', False)
st.markdown("""
    <style>
        .stPlotlist>div>div>div {
            background-color: transparent !important;
        }
    </style>
    """, unsafe_allow_html=True)

def run_lighthouse(url):
    # Ensure Lighthouse CLI is in the PATH
    lighthouse_path = 'lighthouse' 
    result = subprocess.run(
        [lighthouse_path, url, '--output', 'json', '--output-path', 'report.json'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    if result.returncode == 0:
        with open('report.json', 'r') as file:
            report = json.load(file)
            
            # Extract scores for each category
            scores = {}
            categories = ['performance', 'accessibility', 'best-practices', 'seo', 'pwa']
            for category in categories:
                if category in report['categories']:
                    score = report['categories'][category]['score'] * 100
                    scores[category.capitalize()] = score
            
            return report, scores
    else:
        st.error(result.stderr.decode())
        return None, None

def get_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        st.error(f"Error retrieving page title: {e}")
        return None

def display_score_card(category, score):
    st.markdown(
        f"""
        <div style="border-radius: 5px; padding: 20px; background-color: #262730; margin-bottom: 20px;">
            <h3>{category} Score</h3>
            <p>This website scored {score:.1f}% in {category.lower()}.</p>
            <p>Highest score: {max(score, 100-score):.1f}% | Lowest score: {min(score, 100-score):.1f}%</p>
            <p>Difference: {abs(2*max(score, 100-score) - 100):.1f}%</p>
        </div>
        """, unsafe_allow_html=True
    )

def plot_score_pie(category, score):
    labels = [f'{score:.1f}% {category.capitalize()}', f'{100 - score:.1f}% Other']
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie([score, 100 - score], labels=labels, colors=['#1f77b4', '#f0f0f0'], startangle=90, wedgeprops=dict(edgecolor='black', linewidth=1), textprops={'fontsize': 14})
    ax.axis('equal')
    return fig

def extract_diagnostics(report):
    diagnostics = {}
    for category in report['categories']:
        diagnostics[category] = []
        for audit in report['categories'][category]['auditRefs']:
            audit_id = audit['id']
            if report['audits'][audit_id]['score'] is not None and report['audits'][audit_id]['score'] < 1:
                diagnostics[category].append({
                    'title': report['audits'][audit_id]['title'],
                    'description': report['audits'][audit_id]['description']
                })
    return diagnostics

def generate_html_content(url, page_title, scores, diagnostics, charts):
    # Coleta o conteúdo HTML do Streamlit
    html_content = f"""
    <h1>Insights Analysis Tool</h1>
    <br>
    <p><strong>Title:</strong> {page_title}</p>
    <p><strong>URL:</strong> <a href="{url}" style="color:blue;text-decoration:none;">{url}</a></p>
    """

    # Adiciona os scores de cada categoria
    for category, score in scores.items():
        cor = 'green' if score > 80 else 'darkorange' if score >= 50 else'red'

        html_content += f"<br><h3>{category} Score</h3>"
        html_content += f"<p>This website scored <strong style=\"color:{cor}\">{score:.1f}%</strong> in {category.lower()}.</p>"
        html_content += f"<p>Highest score: <strong style=\"color:{cor}\">{max(score, 100-score):.1f}%</strong> | Lowest score: <strong style=\"color:darkorange\">{min(score, 100-score):.1f}%</strong></p>"
        html_content += f"<p>Difference: <strong>{abs(2*max(score, 100-score) - 100):.1f}%</strong></p>"

        if category in diagnostics and diagnostics[category]:
            html_content += f"<br><h4>Diagnostics for {category}</h4><ul>"
            for diag in diagnostics[category]:
                html_content += f"<li><strong>{diag['title']}:</strong> {diag['description']}</li>"
            html_content += "</ul>"

    # Retorna o conteúdo HTML
    return html_content

def verify_site():
    st.title("Insights Analysis Tool")
    st.write("This application only works with Node JS installed, so you must run it in your own local environment.")
    url = st.text_input("Enter the URL to analyze:")

    if st.button("Analyze page load"):
        if url:
            with st.spinner('Running Lighthouse analysis...'):
                report, scores = run_lighthouse(url)
                page_title = get_page_title(url)
            
            if report and scores and page_title:
                st.success("Lighthouse analysis completed successfully.")
                
                # Extract diagnostics
                diagnostics = extract_diagnostics(report)

                # Display score for each category in a card
                for category, score in scores.items():
                    display_score_card(category, score)
                    fig = plot_score_pie(category, score)
                    st.pyplot(fig)

                # Generate charts
                charts = []
                # Add your chart generation logic here and append them to the charts list

                # Generate PDF report
                html_content = generate_html_content(url, page_title, scores, diagnostics, charts)
                pdf = HTML(string=html_content).write_pdf()
                st.download_button(label="Download PDF Report", data=pdf, file_name="report.pdf", mime="application/pdf")
            else:
                st.error("Lighthouse analysis failed.")
        else:
            st.warning("Please enter a URL.")