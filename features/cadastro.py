import streamlit as st
import pandas as pd
import os

CAMINHO_CSV = "data/equipamentos.csv"

def salvar_equipamento(novo_equipamento):
    df = pd.read_csv(CAMINHO_CSV)

    novo_df = pd.DataFrame([novo_equipamento])
    df = pd.concat([df, novo_df], ignore_index=True)

    df.to_csv(CAMINHO_CSV, index=False)

def render_cadastro():
    st.title("Cadastro Técnico do Equipamento")

    st.write(
        "Preencha os dados técnicos do motor para que o sistema conheça "
        "as características básicas do ativo."
    )

    with st.form("form_cadastro"):
        tag = st.text_input("TAG de identificação", placeholder="Ex: MTR-004")
        modelo = st.text_input("Modelo", placeholder="Ex: W22")
        fabricante = st.text_input("Fabricante", placeholder="Ex: WEG")

        potencia = st.number_input("Potência (CV)", min_value=0.0, step=0.5)
        tensao = st.number_input("Tensão nominal (V)", min_value=0)
        corrente = st.number_input("Corrente nominal (A)", min_value=0.0, step=0.1)
        rpm = st.number_input("RPM nominal", min_value=0)

        status = st.selectbox("Status", ["Ativo", "Manutenção", "Inativo"])

        enviar = st.form_submit_button("Cadastrar equipamento")

    if enviar:
        if not tag or not modelo or not fabricante:
            st.error("Preencha TAG, modelo e fabricante antes de cadastrar.")
            return

        novo_equipamento = {
            "tag": tag,
            "modelo": modelo,
            "fabricante": fabricante,
            "potencia": potencia,
            "tensao": tensao,
            "corrente_nominal": corrente,
            "rpm": rpm,
            "status": status
        }

        salvar_equipamento(novo_equipamento)

        st.success("Equipamento cadastrado com sucesso!")
        st.info("Volte para a tela de consulta para visualizar o novo equipamento.")