import streamlit as st

def about():
    st.subheader("About")
    st.write("This app allows you to verify website scores such as performance, accessibility, and more using Streamlit and Lighthouse.")
    st.write("You can also integrate machine learning models and upload large data files for analysis.")
    st.write("Feel free to explore different features and customize the analysis according to your needs!")
    st.write("If you have any questions or suggestions, don't hesitate to reach out to us.")

    # Criando o rodapé com links para suas redes sociais
    st.markdown(
        """
        <style>
        .content {
            gap: 20px;
            width: 100%;
            display: flex;
            margin-top: 40px;
            text-align: center;
            align-items: center;
        }
        </style>

        <div class="content">
            <label>Connect with me:</label>
            <a href="https://github.com/vieira-brz" target="_blank"><img width="80" src="https://pngimg.com/uploads/github/github_PNG23.png" style="background:white;border-radius:5px;"/></a> |
            <a href="https://linkedin.com/in/vinicius-vieira-braz" target="_blank"><img width="80" src="https://static.licdn.com/aero-v1/sc/h/d9us1rzvy2i1u6h4cnr4pexfb"/></a> |
            <a href="https://www.kaggle.com/viniciusbraz03" target="_blank"><img width="80" src="https://www.kaggle.com/static/images/site-logo.svg"/></a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Função para exibir as informações do desenvolvedor na barra lateral
def developer_info():
    # st.sidebar.subheader("Desenvolvido por:")
    st.sidebar.markdown("""
        <style>
        .content-sidebar {
            display: flex; 
            margin-top: 10px;
            flex-direction: column;
        }

        .content-sidebar > div {
            gap: 15px;
            display: flex;
            place-items: center;
        }
        
        .content-sidebar > div > div > h6 {
            margin-top: -10px;
            margin-bottom: -10px;
        }
                        
        .content-sidebar > div > div > a {
            margin-left: -8px;
        }

        .content-sidebar > div > img {
            max-width: 100px;
            max-height: 100px;
            border-radius: 50%;
        }

        .content-sidebar > div > h3 {
            float: right;
        }
        </style>
                        
        <div class="content-sidebar">
            <div>
                <img src="https://avatars.githubusercontent.com/vieira-brz" style="border-radius:50%;width:150px;height:150px;"/>
                <div>
                    <h3>Vinícius Vieira Braz</h3>
                    <h6>Full Stack Developer</h6>
                    <a href="https://github.com/vieira-brz" target="_blank"><img width="40" src="https://pngimg.com/uploads/github/github_PNG23.png" style="background:white;border-radius:5px;margin:0 10px;"/></a> 
                    <a href="https://linkedin.com/in/vinicius-vieira-braz" target="_blank"><img width="40" src="https://static.licdn.com/aero-v1/sc/h/d9us1rzvy2i1u6h4cnr4pexfb" style="margin:0 10px;"/></a> 
                    <a href="https://www.kaggle.com/viniciusbraz03" target="_blank"><img width="40" src="https://www.kaggle.com/static/images/site-logo.svg" style="margin:0 10px;"/></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)