import streamlit as st


def set_prompt(prompt):
    st.session_state["prompt"] = prompt


class TopicSelectorWidget:
    @staticmethod
    def display():
        # st.write("Qual o tópico que você deseja tirar dúvidas?")
        # st.subheader(":orange[• Tópicos]")
        topic = st.selectbox(
            # "",
            "Qual o tópico que você deseja aprender?",
            [*TopicSelectorWidget.mapping().keys()],
            # label_visibility="hidden",
            on_change=set_prompt,
            kwargs={"prompt": ""},
        )

        return topic

    @staticmethod
    def mapping():
        return {
            # "Políticas Públicas": "",
            # "Desafios do Estado de Direito": "",
            # "Ética e Integridade": "",
            # "Diversidade e Inclusão": "",
            "Administração Pública": "administracao_publica",
            "Finanças Públicas": "financas_publicas",
            "Edital nº1 : Infra., Exatas e Engenharias": "edital_1_2024",
            "Edital nº2 : Tech., Dados e Informação": "edital_2_2024",
            "Edital nº3 : Ambiental, Agrário e Bio.": "edital_3_2024",
            "Edital nº4 : Trabalho e Saúde do Servidor": "edital_4_2024",
            "Edital nº5 : Educação, Saúde, Desenv. Social e Direitos Humanos": "edital_5_2024",
            "Edital nº6 : Setores Econômicos e Regulação": "edital_6_2024",
            "Edital nº7 : Gestão Gov. e Administração Pública": "edital_7_2024",
            "Edital nº8 : Nível Intermediário": "edital_8_2024",
            "Edital nº 9 : Adiatamento das Provas": "edital_9_2024",
        }
