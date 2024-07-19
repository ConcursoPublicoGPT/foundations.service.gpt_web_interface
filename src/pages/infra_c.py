import streamlit as st
from src.widgets.chat_widget import ChatWidget


class PageInfraC:
    @staticmethod
    def display():
        st.title(":violet[Arquitetura | Parallels] 🔀")
        st.write(
            "Esta arquitetura é a primeira arquitetura desenvolvida. Composta por **GPT-4o, rerank, busca vetorial baseada em cosines e com uma estrutura de pré-filtragem baseada em parallel quotes**.\n\nFaça os seus experimentos."
        )
        st.write("**• Tópico:**")
        topic = st.selectbox(label="Selecione o tópico.", options=["act"])
        st.write("**• Chat:**")
        ChatWidget.display(topic=topic, model="c")
