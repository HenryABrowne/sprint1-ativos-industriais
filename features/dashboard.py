import streamlit as st
import pandas as pd

CAMINHO_CSV = "data/equipamentos.csv"


@st.cache_data
def carregar_equipamentos():
    return pd.read_csv(CAMINHO_CSV)


def render_dashboard():
    st.title("Consulta de Equipamentos")

    st.write(
        "Nesta tela, o operador visualiza os motores cadastrados "
        "e pode consultar a ficha técnica básica de cada ativo."
    )

    df = carregar_equipamentos()

    if df.empty:
        st.warning("Nenhum equipamento cadastrado ainda.")
        st.info("Acesse o menu Cadastro Técnico para registrar o primeiro equipamento.")
        return

    st.subheader("Equipamentos cadastrados")
    st.dataframe(df, use_container_width=True)

    st.subheader("Selecionar equipamento")

    tags = df["tag"].tolist()
    tag_selecionada = st.selectbox("Escolha um equipamento:", tags)

    equipamento = df[df["tag"] == tag_selecionada].iloc[0]

    st.session_state.equipamento_selecionado = tag_selecionada

    st.subheader("Ficha técnica resumida")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TAG", equipamento["tag"])
        st.metric("Fabricante", equipamento["fabricante"])

    with col2:
        st.metric("Modelo", equipamento["modelo"])
        st.metric("Potência", f"{equipamento['potencia']} CV")

    with col3:
        st.metric("Tensão", f"{equipamento['tensao']} V")
        st.metric("RPM", f"{equipamento['rpm']} RPM")

    st.subheader("Dados técnicos completos")

    st.table(
        {
            "Campo": [
                "TAG",
                "Modelo",
                "Fabricante",
                "Potência",
                "Tensão",
                "Corrente nominal",
                "RPM",
                "Status",
            ],
            "Valor": [
                equipamento["tag"],
                equipamento["modelo"],
                equipamento["fabricante"],
                f"{equipamento['potencia']} CV",
                f"{equipamento['tensao']} V",
                f"{equipamento['corrente_nominal']} A",
                f"{equipamento['rpm']} RPM",
                equipamento["status"],
            ],
        }
    )

    if equipamento["status"] == "Ativo":
        st.success("Equipamento em operação normal.")
    elif equipamento["status"] == "Manutenção":
        st.warning("Equipamento em manutenção.")
    elif equipamento["status"] == "Inativo":
        st.error("Equipamento inativo.")
    else:
        st.info("Status do equipamento indefinido.")

    st.info(
        "Use o menu lateral para acessar o Cadastro Técnico ou os Dados Brutos do Ativo."
    )