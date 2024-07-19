import streamlit as st
from src.pages.infra_a import PageInfraA
from src.pages.infra_c import PageInfraC
from src.pages.documents import PageDocuments

st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="RAG Validação",
    page_icon="🛠",
)

st.sidebar.title(
    "RAG Validation \n Esta aplicação web é direcionada à validação das múltiplas infraestruturas."
)

pages = ["BigBang", "Parallels", "Documentos"]

selected_page = st.sidebar.selectbox("Selecione uma das páginas", pages)

if selected_page == "BigBang":
    PageInfraA.display()
elif selected_page == "Parallels":
    PageInfraC.display()
elif selected_page == "Documentos":
    PageDocuments.display()
