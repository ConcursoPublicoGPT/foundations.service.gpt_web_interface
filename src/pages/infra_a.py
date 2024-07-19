import streamlit as st
from src.widgets.chat_widget import ChatWidget


class PageInfraA:
    @staticmethod
    def display():
        st.title(":orange[Arquitetura | BigBang] 🪐")
        st.write(
            "Esta arquitetura é a primeira arquitetura desenvolvida. Composta por **GPT-4o, rerank, busca vetorial baseada em cosines e leitura de todo o contexto**.\n\nFaça os seus experimentos."
        )
        st.write("**• Tópico:**")
        topic = st.selectbox(label="Selecione o tópico.", options=["act"])
        st.write("**• Chat:**")
        ChatWidget.display(topic=topic, model="a")
