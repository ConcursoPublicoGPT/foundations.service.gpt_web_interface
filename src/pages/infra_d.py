import streamlit as st
from src.widgets.chat_widget import ChatWidget


class PageInfraD:
    @staticmethod
    def display():
        st.title(":green[Infraestrutura D] 🏭😎")
        st.write(
            "Este BOT visa testar a infraestrutura D, a qual é composta por um **modelo de reasoning de MÉDIA QUALIDADE**, **MAIOR QTD. de documentos** e **POSSUI PRÉ-FILTRAGEM**. Faça os seus experimentos! 🧑‍🔬🔬"
        )
        st.write("**• Tópico:**")
        topic = st.selectbox(
            label="Selecione o tópico.", options=["act", "fap", "test", "medicamentos"]
        )
        st.write("**• Chat:**")
        ChatWidget.display(topic=topic, model="d")
