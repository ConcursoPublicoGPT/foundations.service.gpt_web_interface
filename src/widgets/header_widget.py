import streamlit as st


class HeaderWidget:
    @staticmethod
    def display():
        st.title(":orange[DSM-5 & CID-10] 📖")
        st.write(
            "Este BOT é capaz de utilizar referências do DSM-5 e do CID-10 para elobarar respostas inteligentes para as suas dúvidas. Faça as suas perguntas! 🧑‍🔬🔬"
        )
