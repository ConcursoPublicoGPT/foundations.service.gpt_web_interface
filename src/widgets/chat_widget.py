import streamlit as st
from src.requesters.kernel_memory_requester import KernelMemoryRequester


class ChatWidget:
    @staticmethod
    def display(topic):
        st.write("")
        st.subheader("2. Chat")

        st.chat_message("ai").write(
            f"Olá, tudo bem? 👋 Como posso te ajudar com o tópico **{topic}**?"
        )

        prompt = st.chat_input("Faça a sua pergunta aqui ...")

        if prompt is not None:
            answer = KernelMemoryRequester.answer(prompt)
            st.chat_message("human").write(prompt)

            text = answer.get("text")

            if not (answer.get("noResult")):
                st.chat_message("ai").write(text)
            else:
                st.chat_message("ai").write(
                    "Infelizmente, eu não consegui encontrar uma resposta a partir do meu banco de conhecimentos. Será que poderia escrever a sua pergunta de outra forma, por favor? :)"
                )
