import streamlit as st
from src.requesters.documents import DocumentsRequester
import pandas as pd


class PageDocuments:
    @staticmethod
    def display():
        st.title(":orange[Documentos] 📖🧐")
        st.write(
            "Listagem de todos os documentos que foram inseridos na plataforma e os seus respectivos tópicos."
        )

        with st.spinner("Obtendo os metadados dos documentos inseridos ..."):

            data = DocumentsRequester.get()

            if data:

                df = pd.DataFrame(data).reset_index(drop=True)

                st.table(df)

            else:

                st.write("Houve uma falha ao obter os metadados.")
