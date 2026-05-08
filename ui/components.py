import streamlit as st

def card_metrica(titulo, valor, unidade=""):
    st.metric(label=titulo, value=f"{valor} {unidade}")

def aviso_info(texto):
    st.info(texto)

def aviso_sucesso(texto):
    st.success(texto)

def aviso_alerta(texto):
    st.warning(texto)