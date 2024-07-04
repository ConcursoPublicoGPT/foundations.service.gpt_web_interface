import streamlit as st
from src.requesters.kernel_memory_requester import KernelMemoryRequester
import json


def set_prompt(prompt):
    st.session_state["prompt"] = prompt


def set_reset_prompt():
    st.session_state["reset_prompt"] = True


class ChatWidget:
    @staticmethod
    def display():
        st.write("")

        st.chat_message("ai").write(
            f"Olá, tudo bem? 👋 \n\n Quais as dúvidas que eu posso te ajudar?",
        )

        if "prompt" not in st.session_state or st.session_state.get("prompt") == "":
            prompt = st.chat_input("Faça a sua pergunta aqui ...")
        elif (
            st.session_state.get("reset_prompt")
            and st.session_state.get("prompt") != ""
            and "promp" in st.session_state
        ):
            st.session_state["reset_prompt"] = False
            prompt = st.chat_input("Faça a sua pergunta aqui ...")
            prompt = st.session_state.get("prompt")
            st.session_state["prompt"] = ""
        else:
            prompt = st.session_state.get("prompt")

        if prompt is not None:
            ChatWidget.answer_question(prompt)

    @staticmethod
    def answer_question(prompt):
        api_prompt = f"""
        Responda sempre em português brasileiro, com qualidade e acurácia.

        {prompt}
        """

        raw_answer = KernelMemoryRequester.answer(api_prompt)

        st.chat_message("human").write(prompt)

        answer = raw_answer.get("text")

        if not (raw_answer.get("noResult")):
            st.chat_message("ai").write(answer)
            st.download_button(
                "Faça o download das fontes",
                data=json.dumps(raw_answer),
                file_name="sources.json",
            )
        else:
            st.chat_message("ai").write(
                "Infelizmente, eu não consegui encontrar uma resposta a partir do meu banco de conhecimentos. Será que poderia escrever a sua pergunta de outra forma, por favor? :)"
            )
