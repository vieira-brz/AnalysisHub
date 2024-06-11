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
            padding: 10px;
            display: flex;
            margin-top: 40px;
            text-align: center;
            align-items: center;
        }

        .content > img {
            width: 20%;
            height: 20%;
            margin-right: 20px;
            border-radius: 50%;
        }
        </style>

        <div class="content">
            <img src="https://avatars.githubusercontent.com/vieira-brz" />
            <label>Connect with me:</label>
            <a href="https://github.com/vieira-brz" target="_blank"><img width="80" src="https://pngimg.com/uploads/github/github_PNG23.png" style="background:white;border-radius:5px;"/></a> |
            <a href="https://linkedin.com/in/vinicius-vieira-braz" target="_blank"><img width="80" src="https://static.licdn.com/aero-v1/sc/h/d9us1rzvy2i1u6h4cnr4pexfb"/></a> |
            <a href="https://www.kaggle.com/viniciusbraz03" target="_blank"><img width="80" src="https://www.kaggle.com/static/images/site-logo.svg"/></a>
        </div>
        """,
        unsafe_allow_html=True
    )