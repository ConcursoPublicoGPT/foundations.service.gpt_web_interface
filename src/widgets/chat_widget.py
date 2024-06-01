import streamlit as st
from src.requesters.kernel_memory_requester import KernelMemoryRequester
from src.widgets.topic_selector_widget import TopicSelectorWidget
import json


def set_prompt(prompt):
    st.session_state["prompt"] = prompt


def set_reset_prompt():
    st.session_state["reset_prompt"] = True


class ChatWidget:
    @staticmethod
    def display(topic):
        st.write("")

        st.chat_message("ai").write(
            f"Olá, tudo bem? 👋 \n\n Quais as dúvidas que eu posso te ajudar com **{topic}**?",
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
            ChatWidget.answer_question(prompt, topic)

    @staticmethod
    def answer_question(prompt, topic):
        api_prompt = f"""
        Você deve atuar como um professor respondendo a pergunta de um aluno de forma clara e detalhada.
        Responda sempre em português brasileiro.
        Além da resposta para a pergunta, você deve retornar uma lista com 3 novas perguntas e diferentes que irão estimular a pessoa aprender mais sobre conceitos relacionados à pergunta feita e que estejam relacionadas ao seu contexto:

        {prompt}
        """

        translated_topic_to_api = TopicSelectorWidget.mapping().get(topic)

        raw_answer = KernelMemoryRequester.answer(api_prompt, translated_topic_to_api)

        st.chat_message("human").write(prompt)

        answer = raw_answer.get("text")

        if not (raw_answer.get("noResult")):
            st.chat_message("ai").write(answer)
        else:
            st.chat_message("ai").write(
                "Infelizmente, eu não consegui encontrar uma resposta a partir do meu banco de conhecimentos. Será que poderia escrever a sua pergunta de outra forma, por favor? :)"
            )
