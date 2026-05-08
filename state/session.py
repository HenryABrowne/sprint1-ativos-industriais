import streamlit as st

def inicializar_sessao():
    if "equipamento_selecionado" not in st.session_state:
        st.session_state.equipamento_selecionado = None

    if "mensagem_sucesso" not in st.session_state:
        st.session_state.mensagem_sucesso = ""