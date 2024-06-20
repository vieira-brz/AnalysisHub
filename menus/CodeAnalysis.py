import streamlit as st
import openai
from fpdf import FPDF
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a chave da API do OpenAI
api_key = os.getenv('OPENAI_API_KEY')
organization = os.getenv('OPENAI_ORGANIZATION_ID')

# Definir a chave da API e a organização
openai.api_key = api_key
openai.organization = organization

def get_language_by_extension(file_extension):
    extension_to_language = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.php': 'PHP',
        '.html': 'HTML',
        '.css': 'CSS',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.cs': 'C#',
        '.rb': 'Ruby',
        '.go': 'Go',
        '.rs': 'Rust',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.r': 'R',
        '.pl': 'Perl',
        '.sh': 'Shell Script',
        '.bat': 'Batch',
        '.ps1': 'PowerShell',
        '.sql': 'SQL',
        '.xml': 'XML',
        '.json': 'JSON',
        '.yml': 'YAML',
        '.yaml': 'YAML',
        '.md': 'Markdown',
        '.tex': 'LaTeX',
        '.vb': 'Visual Basic',
        '.scala': 'Scala',
        '.erl': 'Erlang',
        '.ex': 'Elixir',
        '.dart': 'Dart',
        '.lua': 'Lua',
        '.m': 'MATLAB',
        '.jl': 'Julia',
        '.hs': 'Haskell',
        '.coffee': 'CoffeeScript',
        '.scss': 'Sass',
        '.less': 'Less',
        '.tsx': 'TypeScript JSX',
        '.jsx': 'JavaScript JSX'
    }
    return extension_to_language.get(file_extension, 'Desconhecida')

def analyze_code_with_openai(code, language):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Você é um assistente que explica código {language}."},
            {"role": "user", "content": f"Explique o seguinte código {language} em linguagem humana:\n\n{code}"}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    explanation = response['choices'][0]['message']['content'].strip()
    return explanation

def create_pdf(text, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True, align='L')
    pdf.output(output_path)

def describe_file():
    st.title("Code Analysis")

    uploaded_file = st.file_uploader("Escolha um arquivo de código", type=['py', 'js', 'ts', 'php', 'html', 'css'], key="file_uploader")
    if uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[1]
        language = get_language_by_extension(file_extension)
        
        code = uploaded_file.read().decode('utf-8')
        st.write(f"Linguagem detectada: {language}")

        if language == 'Desconhecida':
            st.warning("A linguagem do arquivo não foi reconhecida automaticamente. Por favor, verifique a extensão do arquivo.")
        else:
            explanation = analyze_code_with_openai(code, language)
            st.text_area("Explicação do Código", explanation, height=300, key="explanation_area")

            output_path = "explanation.pdf"
            create_pdf(explanation, output_path)
            with open(output_path, "rb") as file:
                st.download_button(
                    label="Baixar PDF",
                    data=file,
                    file_name=output_path,
                    mime='application/octet-stream',
                    key="download_pdf_button"
                )
            os.remove(output_path)