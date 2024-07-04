import streamlit as st


class HeaderWidget:
    @staticmethod
    def display():
        st.title(":orange[RAG Researcher]")
        st.write(
            "Nós possuímos 1 artigo no banco de dados. Faça as suas perguntas! 🧑‍🔬🔬"
        )
