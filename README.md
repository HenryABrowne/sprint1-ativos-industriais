# Sistema Inteligente de Cadastro e Monitoramento de Ativos Industriais

## Challenge Sprint 1 — Front-End & Mobile Development

Aplicação desenvolvida em **Streamlit** para cadastro técnico inicial de motores industriais, consulta de equipamentos cadastrados e visualização de dados brutos simulados de sensores.

---

## Objetivo da Sprint

Desenvolver uma interface funcional que permita ao operador cadastrar um equipamento industrial e visualizar sua ficha técnica completa, deixando a aplicação preparada para receber dados de sensores nas próximas fases.

---

## Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Streamlit | Interface web |
| Pandas | Manipulação de dados |
| Plotly | Gráficos interativos |
| CSV | Persistência simples dos dados |

---

## Funcionalidades Implementadas

### Consulta de Equipamentos

- Tela inicial com listagem dos motores cadastrados;
- Tabela com TAG, modelo, fabricante, potência, tensão, RPM e status;
- Visualização resumida da ficha técnica do equipamento selecionado.

### Cadastro Técnico

- Formulário para cadastro de novos motores;
- Campos técnicos como TAG, modelo, fabricante, potência, tensão, corrente nominal, RPM e status;
- Salvamento dos dados em arquivo CSV.

### Visualização de Dados Brutos

- Exibição de leituras simuladas dos sensores;
- Conversão de valores brutos para unidades compreensíveis;
- Visualização de corrente, tensão, RPM e vibração;
- Status operacional por sensor.

### Monitoramento Temporal

- Cada sensor possui várias leituras ao longo do tempo;
- Gráfico temporal interativo;
- Comparação da última leitura de cada sensor;
- Identificação de estados Normal, Alerta e Crítico.

---

## Estrutura do Projeto

```text
sprint1-ativos-industriais/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── equipamentos.csv
│   └── sensores.csv
│
├── features/
│   ├── dashboard.py
│   ├── cadastro.py
│   └── sensores.py
│
├── pipelines/
│   └── conversoes.py
│
├── providers/
│   └── dados_fake.py
│
├── state/
│   └── session.py
│
└── ui/
    └── components.py
```

---

## Arquitetura do Projeto

O projeto foi organizado com separação de responsabilidades para evitar que a interface, a lógica de negócio e o processamento dos dados fiquem misturados no mesmo arquivo.

### `app.py`

Arquivo principal da aplicação.

Responsável por:

- Configurar a página do Streamlit;
- Inicializar a sessão;
- Criar o menu lateral;
- Direcionar o usuário para cada tela.

### `features/`

Contém as principais telas da aplicação.

- `dashboard.py`: tela de consulta dos equipamentos cadastrados;
- `cadastro.py`: módulo de cadastro técnico;
- `sensores.py`: tela de visualização dos dados brutos e convertidos.

### `pipelines/`

Contém a lógica de processamento dos dados.

- `conversoes.py`: responsável por converter valores brutos dos sensores em unidades compreensíveis.

### `data/`

Armazena os arquivos CSV usados como base simulada.

- `equipamentos.csv`: dados técnicos dos motores;
- `sensores.csv`: leituras simuladas dos sensores.

### `state/`

Gerencia informações mantidas durante a sessão do usuário.

- `session.py`: inicialização de variáveis em `st.session_state`.

### `ui/`

Contém componentes visuais reutilizáveis.

- `components.py`: funções auxiliares para mensagens e métricas.

### `providers/`

Reservado para futuras integrações com fontes externas de dados, APIs, sensores reais ou banco de dados.

---

## Fluxo da Aplicação

```text
Usuário acessa a aplicação
↓
Streamlit carrega o app.py
↓
Menu lateral exibe as telas disponíveis
↓
Usuário escolhe uma funcionalidade
↓
A feature correspondente é renderizada
↓
A aplicação lê dados dos arquivos CSV
↓
Os pipelines processam ou convertem os dados
↓
A interface exibe tabelas, métricas, gráficos e alertas
```

Fluxo resumido:

```text
Usuário
↓
Interface Streamlit
↓
Features
↓
Pipelines
↓
Dados CSV
↓
Visualização e feedback
```

---

## Demonstração das Funcionalidades

### 1. Dashboard Principal

Na tela inicial, o operador visualiza todos os equipamentos cadastrados em uma tabela.

Ao selecionar uma TAG, o sistema exibe a ficha técnica resumida do motor.

Funcionalidades demonstradas:

- Consulta dos ativos cadastrados;
- Exibição organizada dos atributos básicos;
- Status visual do equipamento.

### 2. Cadastro Técnico

No módulo de cadastro, o operador preenche os dados técnicos do motor.

Campos disponíveis:

- TAG de identificação;
- Modelo;
- Fabricante;
- Potência;
- Tensão nominal;
- Corrente nominal;
- RPM nominal;
- Status.

Após o envio, o sistema salva o novo equipamento no arquivo CSV.

### 3. Dados Brutos do Ativo

Nesta tela, o usuário seleciona um equipamento e visualiza leituras simuladas de sensores.

O sistema mostra:

- Valor bruto;
- Valor convertido;
- Unidade de medida;
- Horário da leitura;
- Status operacional.

### 4. Gráficos Interativos

A aplicação apresenta gráficos com Plotly para facilitar a análise visual dos sensores.

Gráficos disponíveis:

- Monitoramento temporal dos sensores;
- Comparação da última leitura convertida.

### 5. Feedback Visual

A interface utiliza mensagens visuais para orientar o usuário:

- Verde para funcionamento normal;
- Amarelo para alerta;
- Vermelho para estado crítico;
- Spinner para indicar processamento.

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/HenryABrowne/Sprint1-Ativos_Industriais
```

### 2. Entrar na pasta do projeto

```bash
cd sprint1-ativos-industriais
```

### 3. Criar ambiente virtual

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Após executar o comando, o navegador abrirá a aplicação localmente.

---

## Conceitos Aplicados da Disciplina

### Streamlit como Framework Front-End

A aplicação utiliza Streamlit para criar uma interface web funcional com Python, sem necessidade inicial de HTML, CSS ou JavaScript.

### Sidebar como Menu de Navegação

O menu lateral organiza as telas da aplicação e já prepara a estrutura para crescimento nas próximas sprints.

### Session State

O `st.session_state` é usado para manter informações durante a sessão do usuário, como o equipamento selecionado.

### Inputs e Formulários

A aplicação utiliza componentes como:

- `st.text_input`;
- `st.number_input`;
- `st.selectbox`;
- `st.form`;
- `st.form_submit_button`.

### Visualização de Dados

São utilizados:

- `st.dataframe`;
- `st.metric`;
- Gráficos interativos com Plotly.

### UX para Aplicações Inteligentes

Foram aplicados conceitos de:

- Design para latência;
- Feedback visual;
- Cores semânticas;
- Transparência dos dados;
- Human-in-the-loop.

### Arquitetura Desacoplada

O projeto separa:

- Interface;
- Features;
- Processamento;
- Estado;
- Dados.

Isso permite evoluir o backend, integrar modelos de IA ou trocar tecnologias sem reescrever toda a aplicação.

### Pipeline de Conversão

A conversão dos dados brutos dos sensores fica isolada em `pipelines/conversoes.py`, facilitando manutenção e evolução futura.

---

## Possíveis Evoluções Futuras

- Integração com sensores reais;
- Comunicação com dispositivos IoT;
- Banco de dados relacional;
- API com FastAPI;
- Dashboard em tempo real;
- Sistema de autenticação;
- Histórico completo dos ativos;
- Alertas automáticos por nível de risco;
- Integração com Machine Learning;
- Predição de falhas;
- Deploy em nuvem;
- Aplicativo mobile com FlutterFlow ou outra tecnologia;
- Relatórios técnicos exportáveis;
- Integração com sistemas corporativos de manutenção.
