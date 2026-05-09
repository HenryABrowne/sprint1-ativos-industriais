import streamlit as st
import pandas as pd

CAMINHO_CSV = "data/equipamentos.csv"


def carregar_equipamentos():
    return pd.read_csv(CAMINHO_CSV)


def salvar_dataframe(df):
    df.to_csv(CAMINHO_CSV, index=False)


def render_equipamentos():
    st.title("Gerenciamento de Equipamentos")

    st.write(
        "Nesta área, o operador pode cadastrar, editar e excluir equipamentos "
        "industriais de forma centralizada."
    )

    aba_cadastro, aba_editar, aba_excluir = st.tabs(
        [
            "Cadastro Técnico",
            "Editar dados",
            "Excluir dados"
        ]
    )

    # =========================================================
    # ABA 1 - CADASTRO TÉCNICO
    # =========================================================

    with aba_cadastro:
        st.header("Cadastro Técnico")

        st.info(
            "Preencha os dados técnicos do motor para que o sistema conheça "
            "as características básicas do ativo."
        )

        with st.form("form_cadastro"):
            tag = st.text_input(
                "TAG de identificação",
                placeholder="Ex: MTR-004"
            )

            modelo = st.text_input(
                "Modelo",
                placeholder="Ex: W22"
            )

            fabricante = st.text_input(
                "Fabricante",
                placeholder="Ex: WEG"
            )

            col1, col2 = st.columns(2)

            with col1:
                potencia = st.number_input(
                    "Potência (CV)",
                    min_value=0.0,
                    step=0.5
                )

                tensao = st.number_input(
                    "Tensão nominal (V)",
                    min_value=0
                )

            with col2:
                corrente = st.number_input(
                    "Corrente nominal (A)",
                    min_value=0.0,
                    step=0.1
                )

                rpm = st.number_input(
                    "RPM nominal",
                    min_value=0
                )

            status = st.selectbox(
                "Status",
                ["Ativo", "Manutenção", "Inativo"]
            )

            enviar = st.form_submit_button(
                "Cadastrar equipamento"
            )

        if enviar:
            if not tag or not modelo or not fabricante:
                st.error("Preencha TAG, modelo e fabricante.")
                return

            df = carregar_equipamentos()

            if tag in df["tag"].values:
                st.warning("Já existe um equipamento com essa TAG.")
                return

            novo_equipamento = {
                "tag": tag,
                "modelo": modelo,
                "fabricante": fabricante,
                "potencia": potencia,
                "tensao": tensao,
                "corrente_nominal": corrente,
                "rpm": rpm,
                "status": status,
            }

            novo_df = pd.DataFrame([novo_equipamento])
            df = pd.concat([df, novo_df], ignore_index=True)

            salvar_dataframe(df)
            st.cache_data.clear()

            st.success("Equipamento cadastrado com sucesso!")
            st.info("O novo equipamento já está disponível na tela de consulta.")

    # =========================================================
    # ABA 2 - EDITAR DADOS
    # =========================================================

    with aba_editar:
        st.header("Editar dados do equipamento")

        st.info(
            "Selecione um equipamento já cadastrado e atualize suas informações técnicas."
        )

        df = carregar_equipamentos()

        if df.empty:
            st.warning("Nenhum equipamento cadastrado.")
        else:
            tags = df["tag"].tolist()

            tag_selecionada = st.selectbox(
                "Selecione a TAG do equipamento",
                tags,
                key="editar_tag"
            )

            equipamento = df[df["tag"] == tag_selecionada].iloc[0]

            st.subheader("Dados atuais")

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
                        "Status"
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

            with st.form("form_edicao"):
                novo_modelo = st.text_input(
                    "Modelo",
                    value=str(equipamento["modelo"])
                )

                novo_fabricante = st.text_input(
                    "Fabricante",
                    value=str(equipamento["fabricante"])
                )

                col1, col2 = st.columns(2)

                with col1:
                    nova_potencia = st.number_input(
                        "Potência (CV)",
                        value=float(equipamento["potencia"]),
                        step=0.5
                    )

                    nova_tensao = st.number_input(
                        "Tensão nominal (V)",
                        value=int(equipamento["tensao"])
                    )

                with col2:
                    nova_corrente = st.number_input(
                        "Corrente nominal (A)",
                        value=float(equipamento["corrente_nominal"]),
                        step=0.1
                    )

                    novo_rpm = st.number_input(
                        "RPM nominal",
                        value=int(equipamento["rpm"])
                    )

                status_opcoes = ["Ativo", "Manutenção", "Inativo"]

                status_atual = str(equipamento["status"])

                if status_atual not in status_opcoes:
                    status_atual = "Ativo"

                novo_status = st.selectbox(
                    "Status",
                    status_opcoes,
                    index=status_opcoes.index(status_atual)
                )

                salvar_edicao = st.form_submit_button(
                    "Salvar alterações"
                )

            if salvar_edicao:
                df.loc[df["tag"] == tag_selecionada, "modelo"] = novo_modelo
                df.loc[df["tag"] == tag_selecionada, "fabricante"] = novo_fabricante
                df.loc[df["tag"] == tag_selecionada, "potencia"] = nova_potencia
                df.loc[df["tag"] == tag_selecionada, "tensao"] = nova_tensao
                df.loc[df["tag"] == tag_selecionada, "corrente_nominal"] = nova_corrente
                df.loc[df["tag"] == tag_selecionada, "rpm"] = novo_rpm
                df.loc[df["tag"] == tag_selecionada, "status"] = novo_status

                salvar_dataframe(df)
                st.cache_data.clear()

                st.success("Equipamento atualizado com sucesso!")
                st.rerun()

    # =========================================================
    # ABA 3 - EXCLUIR DADOS
    # =========================================================

    with aba_excluir:
        st.header("Excluir dados do equipamento")

        st.warning(
            "Use esta opção apenas para remover registros incorretos ou equipamentos "
            "que não devem mais aparecer no sistema."
        )

        df = carregar_equipamentos()

        if df.empty:
            st.warning("Nenhum equipamento cadastrado.")
        else:
            tags = df["tag"].tolist()

            tag_selecionada = st.selectbox(
                "Selecione a TAG para excluir",
                tags,
                key="excluir_tag"
            )

            equipamento = df[df["tag"] == tag_selecionada].iloc[0]

            st.subheader("Equipamento selecionado")

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
                        "Status"
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

            st.error(
                "A exclusão removerá permanentemente este equipamento do arquivo CSV."
            )

            confirmar = st.checkbox(
                "Confirmo que desejo excluir este equipamento",
                key="confirmar_exclusao"
            )

            if confirmar:
                excluir = st.button(
                    "Excluir equipamento",
                    type="primary"
                )

                if excluir:
                    df = df[df["tag"] != tag_selecionada]

                    salvar_dataframe(df)
                    st.cache_data.clear()

                    st.success("Equipamento excluído com sucesso!")
                    st.rerun()