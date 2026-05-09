import streamlit as st


def render_manual():
    st.title("Manual de Uso")

    st.info(
        "Este manual orienta o operador sobre como utilizar as principais "
        "funcionalidades do sistema de cadastro e monitoramento de ativos."
    )

    st.header("1. Menu lateral")

    st.write(
        """
        O menu lateral permite navegar entre as telas do sistema:

        - **Consulta de Equipamentos**
        - **Gerenciamento de Equipamentos**
        - **Dados Brutos do Ativo**
        - **Manual de Uso**
        """
    )

    st.header("2. Consulta de Equipamentos")

    st.write(
        """
        Na tela **Consulta de Equipamentos**, o operador visualiza todos os motores
        cadastrados no sistema.

        A tabela apresenta informações como:

        - TAG
        - Modelo
        - Fabricante
        - Potência
        - Tensão
        - Corrente nominal
        - RPM
        - Status
        """
    )

    st.success(
        "Para visualizar a ficha técnica de um motor, selecione a TAG desejada "
        "no campo de seleção da tela."
    )

    st.header("3. Gerenciamento de Equipamentos")

    st.write(
        """
        Na tela **Gerenciamento de Equipamentos**, o operador pode realizar as ações
        principais do cadastro técnico:

        - **Cadastro Técnico**
        - **Editar dados**
        - **Excluir dados**

        Essas opções ficam disponíveis dentro do próprio módulo técnico.
        """
    )

    st.subheader("3.1 Cadastro Técnico")

    st.write(
        """
        No cadastro técnico, o operador pode registrar um novo motor industrial.

        Os campos disponíveis são:

        - TAG de identificação
        - Modelo
        - Fabricante
        - Potência
        - Tensão nominal
        - Corrente nominal
        - RPM nominal
        - Status operacional
        """
    )

    st.warning(
        "A TAG, o modelo e o fabricante são informações essenciais para o cadastro."
    )

    st.subheader("3.2 Editar dados")

    st.write(
        """
        Na opção **Editar dados**, o operador seleciona uma TAG já cadastrada
        e pode atualizar as informações técnicas do equipamento.
        """
    )

    st.info(
        "Essa função é útil para corrigir dados cadastrados incorretamente "
        "ou atualizar o status operacional do motor."
    )

    st.subheader("3.3 Excluir dados")

    st.write(
        """
        Na opção **Excluir dados**, o operador pode remover um equipamento do sistema.
        Antes da exclusão, o sistema exibe os principais dados do equipamento selecionado.
        """
    )

    st.error(
        "A exclusão remove o equipamento do arquivo CSV. Use essa opção com cuidado."
    )

    st.header("4. Dados Brutos do Ativo")

    st.write(
        """
        Na tela **Dados Brutos do Ativo**, o operador seleciona um equipamento
        e visualiza as leituras simuladas dos sensores.

        O sistema mostra:

        - Valor bruto
        - Valor convertido
        - Unidade de medida
        - Horário da leitura
        - Status operacional
        """
    )

    st.header("5. Conversão dos sensores")

    st.write(
        """
        Os valores brutos dos sensores são convertidos automaticamente para unidades
        compreensíveis pelo operador.
        """
    )

    st.table(
        {
            "Sensor": ["Corrente", "Tensão", "RPM", "Vibração"],
            "Unidade convertida": ["Ampères (A)", "Volts (V)", "RPM", "mm/s"],
        }
    )

    st.header("6. Status operacional")

    st.write(
        """
        A aplicação utiliza cores semânticas para facilitar a interpretação dos dados.
        """
    )

    st.success("Verde: funcionamento normal.")
    st.warning("Amarelo: estado de alerta.")
    st.error("Vermelho: estado crítico.")

    st.header("7. Gráficos interativos")

    st.write(
        """
        A tela de sensores possui gráficos interativos para acompanhar o comportamento
        do equipamento ao longo do tempo.

        Os gráficos ajudam o operador a identificar:

        - Variações nas leituras
        - Possíveis falhas
        - Tendências de funcionamento
        - Sensores em alerta ou estado crítico
        """
    )

    st.header("8. Encerramento")

    st.write(
        """
        Para encerrar a aplicação, o operador deve voltar ao terminal onde o Streamlit
        está rodando e pressionar:
        """
    )

    st.code("CTRL + C", language="bash")