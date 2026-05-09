import streamlit as st

from state.session import inicializar_sessao
from features.dashboard import render_dashboard
from features.equipamentos import render_equipamentos
from features.sensores import render_sensores
from features.manual import render_manual


st.set_page_config(
    page_title="Sistema de Ativos Industriais",
    layout="wide"
)


inicializar_sessao()


if "pagina" not in st.session_state:
    st.session_state.pagina = "Consulta de Equipamentos"


paginas = [
    "Consulta de Equipamentos",
    "Gerenciamento de Equipamentos",
    "Dados Brutos do Ativo",
    "Manual de Uso"
]


st.sidebar.title("Menu")
st.sidebar.write("Sprint 1 - Fundamentos do Ativo")


pagina = st.sidebar.radio(
    "Navegação",
    paginas,
    index=paginas.index(st.session_state.pagina)
)


st.session_state.pagina = pagina


st.sidebar.divider()

st.sidebar.info(
    "Sistema inicial para cadastro, edição, exclusão e visualização técnica "
    "de motores industriais."
)


if pagina == "Consulta de Equipamentos":
    render_dashboard()

elif pagina == "Gerenciamento de Equipamentos":
    render_equipamentos()

elif pagina == "Dados Brutos do Ativo":
    render_sensores()

elif pagina == "Manual de Uso":
    render_manual()