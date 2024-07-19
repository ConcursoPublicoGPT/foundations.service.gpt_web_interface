import streamlit as st
import requests
import json
from src.agents.agent_reasoner import AgentReasoner
import os


class ChatWidget:
    @staticmethod
    def display(topic, model="a"):

        host = os.getenv("MAIN_HOST")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Faça a sua pergunta aqui ..."):

            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("user"):

                st.markdown(prompt)

            with st.chat_message("assistant"):

                model_name = {"a": "BigBang 🪐", "c": "Parallels 🔀"}

                model_content = (
                    f"Nesta resposta, eu usarei o modelo **{model_name.get(model)}:**"
                )
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": model_content,
                    }
                )

                st.markdown(model_content)

                response = requests.get(
                    url=f"{host}/v1_0_0/ask/infra_{model}",
                    params={
                        "query": prompt,
                        "topic": topic,
                    },
                )

                if response.status_code == 200:

                    data = json.loads(response.content).get("body")

                    context = data.get("context")

                    references = ""
                    for reference in data.get("references"):
                        references = references + f"- {reference}\n"

                    if model == "a":
                        stream = AgentReasoner.from_full_context(
                            query=prompt,
                            document=context,
                        )
                    elif model == "b":
                        stream = AgentReasoner.from_full_context(
                            query=prompt,
                            document=context,
                            model="gpt-3.5-turbo",
                        )
                    elif model == "c":
                        stream = AgentReasoner.from_quotes(
                            query=prompt,
                            document=context,
                        )
                    elif model == "d":
                        stream = AgentReasoner.from_quotes(
                            query=prompt,
                            document=context,
                            model="gpt-3.5-turbo",
                        )
                    else:
                        raise Exception("Você deve definir o valor de 'model'.")

                    response = st.write_stream(stream)

                else:

                    response = (
                        f"Tivemos uma falha de infraestrutura.\n\n{response.text}"
                    )

            st.session_state.messages.append({"role": "assistant", "content": response})

            st.download_button(
                label="Download das fontes utilizadas pelo modelo.",
                data=context,
                file_name="model_sources.txt",
            )
