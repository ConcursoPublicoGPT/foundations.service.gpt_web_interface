import streamlit as st


class TopicSelectorWidget:
    @staticmethod
    def display():
        st.write("")
        st.subheader("1. Tópicos")
        topic = st.selectbox(
            "Escolha o tópico que você deseja estudar:",
            [
                "Administração Pública",
                "Edital : Educação, Saúde, Desenvolvimento Social e Direitos Humanos",
            ],
        )

        return topic
