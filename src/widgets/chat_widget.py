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

            text = answer.get("text")
            sources = answer.get("sources")

            st.chat_message("human").write(prompt)
            st.chat_message("ai").write(text)

            for source in sources:
                for partition in source.get("partitions"):
                    st.chat_message("ai").markdown(
                        f"**• Relevância :** {partition.get("relevance")} &nbsp; \ **• Conteúdo :** {partition.get('text')}"
                    )
            st.chat_message("ai", avatar=":material/flutter_dash:").write(f"")

            # [] => documentId => partitions [] => text & relevance
