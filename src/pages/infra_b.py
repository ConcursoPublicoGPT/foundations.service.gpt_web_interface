import streamlit as st
from src.widgets.chat_widget import ChatWidget


class PageInfraB:
    @staticmethod
    def display():
        st.title(":blue[Infraestrutura B] 🏭🚀")
        st.write(
            "Este BOT visa testar a infraestrutura B, a qual é composta por um **modelo de reasoning de QUALIDADE MÉDIA**, **MAIOR QTD. de documentos** e **NÃO POSSUI PRÉ-FILTRAGEM**. Faça os seus experimentos! 🧑‍🔬🔬"
        )
        st.write("**• Tópico:**")
        topic = st.selectbox(
            label="Selecione o tópico.", options=["act", "fap", "test", "medicamentos"]
        )
        st.write("**• Chat:**")
        ChatWidget.display(topic=topic, model="b")
