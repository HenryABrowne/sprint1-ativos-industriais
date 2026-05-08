import streamlit as st
import pandas as pd
import plotly.express as px
from pipelines.conversoes import converter_sensor


@st.cache_data
def carregar_sensores():
    return pd.read_csv("data/sensores.csv")


def render_sensores():
    st.title("Visualização de Dados Brutos do Ativo")

    st.write(
        "Nesta tela, os sinais brutos simulados dos sensores são convertidos "
        "para unidades compreensíveis pelo operador."
    )

    df = carregar_sensores()

    tags = df["tag"].unique().tolist()
    tag_selecionada = st.selectbox("Selecione o equipamento:", tags)

    dados = df[df["tag"] == tag_selecionada].copy()

    with st.spinner("Convertendo dados brutos dos sensores..."):
        dados["valor_convertido"] = dados.apply(
            lambda linha: converter_sensor(linha["sensor"], linha["valor_bruto"])[0],
            axis=1
        )

        dados["unidade"] = dados.apply(
            lambda linha: converter_sensor(linha["sensor"], linha["valor_bruto"])[1],
            axis=1
        )

    st.success("Dados convertidos com sucesso.")

    st.subheader("Tabela de dados brutos e convertidos")
    st.dataframe(dados, use_container_width=True)

    st.subheader("Última leitura por sensor")

    ultimas_leituras = (
        dados.sort_values("timestamp")
        .groupby("sensor")
        .tail(1)
        .reset_index(drop=True)
    )

    for _, linha in ultimas_leituras.iterrows():
        st.metric(
            label=linha["sensor"].capitalize(),
            value=f"{linha['valor_convertido']} {linha['unidade']}",
            delta=f"Status: {linha['status']}"
        )

        if linha["status"] == "Normal":
            st.success(f"{linha['sensor'].capitalize()} operando normalmente.")

        elif linha["status"] == "Alerta":
            st.warning(f"{linha['sensor'].capitalize()} apresenta comportamento fora do ideal.")

        elif linha["status"] == "Crítico":
            st.error(f"{linha['sensor'].capitalize()} em estado crítico.")

    st.subheader("Gráfico temporal dos sensores")

    fig_linha = px.line(
        dados,
        x="timestamp",
        y="valor_convertido",
        color="sensor",
        markers=True,
        title=f"Monitoramento temporal - {tag_selecionada}"
    )

    st.plotly_chart(fig_linha, use_container_width=True)

    st.subheader("Comparação da última leitura")

    fig_barra = px.bar(
        ultimas_leituras,
        x="sensor",
        y="valor_convertido",
        text="unidade",
        title=f"Última leitura convertida - {tag_selecionada}"
    )

    st.plotly_chart(fig_barra, use_container_width=True)

    st.info(
        "Os dados exibidos são simulados nesta Sprint. Nas próximas fases, "
        "essa estrutura poderá receber dados reais de sensores."
    )