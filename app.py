import streamlit as st

from state.session import inicializar_sessao
from features.dashboard import render_dashboard
from features.cadastro import render_cadastro
from features.sensores import render_sensores

st.set_page_config(
    page_title="Sistema de Ativos Industriais",
    layout="wide"
)

inicializar_sessao()

st.sidebar.title("Menu")
st.sidebar.write("Sprint 1 - Fundamentos do Ativo")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Consulta de Equipamentos",
        "Cadastro Técnico",
        "Dados Brutos do Ativo"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "Sistema inicial para cadastro e visualização técnica de motores industriais."
)

if pagina == "Consulta de Equipamentos":
    render_dashboard()

elif pagina == "Cadastro Técnico":
    render_cadastro()

elif pagina == "Dados Brutos do Ativo":
    render_sensores()