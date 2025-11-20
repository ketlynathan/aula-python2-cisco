🚀 Projeto Avançado de Python: Gerenciador Web de Eventos
🎯 Objetivo do Exercício
O objetivo desta fase é transformar o Gerenciador de Eventos e Agendamento Simples de um programa de terminal para um aplicativo web interativo. Isso será feito migrando a persistência de dados de um arquivo .json para um banco de dados SQLite e construindo uma arquitetura de serviço (API) e interface de usuário (Dashboard) separadas.

🐍 Tecnologias e Módulos a Adicionar
Categoria	Tecnologia	Uso no Projeto	Conceito Principal
Banco de Dados	sqlite3 (Módulo Padrão)	Gerenciar a persistência de dados (CRUD) dos eventos no banco de dados.	Conexão, Cursor, Linguagem SQL (DDL e DML).
Serviço (API)	FastAPI	Criar endpoints HTTP para permitir que o front-end interaja com o banco de dados.	Roteamento, Modelos Pydantic, Requisições HTTP (GET, POST, PUT, DELETE).
Front-end	Streamlit	Criar a interface de usuário (Dashboard) para o Gerenciador de Eventos.	Widgets (botões, inputs), Estrutura de layouts, Renderização de dados.
Manutenção	requests	Dentro do Streamlit, será usado para fazer chamadas HTTP para a API do FastAPI.	Clientes HTTP.
Manutenção	datetime, calendar	Continuam sendo usados para manipulação e visualização das datas.	Reforço de conceitos.
🏛️ Arquitetura do Projeto
O projeto será dividido em três camadas principais:

Camada de Dados: Banco de dados SQLite (eventos.db).
Camada de Serviço (Backend): Aplicação FastAPI rodando em uma porta específica (ex: 8000).
Camada de Visualização (Frontend): Aplicação Streamlit rodando em outra porta (ex: 8501).
🛠️ Etapas do Desenvolvimento e Funcionalidades
Parte 1: Camada de Dados (sqlite3)
Inicialização do Banco: Criar uma função inicializar_db() que:
Cria a conexão com o arquivo eventos.db.
Executa uma query SQL (DDL) para criar a tabela eventos (com colunas como id, nome, data_hora).
Módulo CRUD (Create, Read, Update, Delete):
Criar funções que utilizam sqlite3 para interagir com a tabela:
criar_evento(nome, data_hora)
listar_eventos()
atualizar_evento(id, nome, data_hora)
deletar_evento(id)
Parte 2: Camada de Serviço (FastAPI)
Modelos Pydantic: Definir os modelos de dados para validação de entrada e saída (ex: Evento, EventoCreate).
Definição de Rotas (Endpoints):
POST /eventos/: Recebe dados do evento e chama a função criar_evento().
GET /eventos/: Chama a função listar_eventos() e retorna a lista.
PUT /eventos/{id}: Recebe o ID e novos dados, chama atualizar_evento().
DELETE /eventos/{id}: Recebe o ID e chama deletar_evento().
Parte 3: Camada de Visualização (Streamlit)
Esta é a interface final que o usuário irá interagir. Usará a biblioteca requests para consumir os endpoints do FastAPI.

Dashboard Principal:
Exibir todos os eventos futuros listados.
Funcionalidades CRUD na Interface:
Inclusão: Formulário (widgets st.text_input, st.date_input, st.time_input) que envia um POST para a API.
Alteração: Tabela de eventos com opção de selecionar um evento e abrir um formulário de edição (enviando um PUT).
Deleção: Botão de exclusão para cada evento, enviando um DELETE para a API.
Visualização no Calendário (calendar):
Criar uma seção lateral ou uma página dedicada que exiba o calendário mensal (usando calendar e marcadores visuais para os dias que possuem eventos).
⭐ Desafios Extras
Filtro Dinâmico (Streamlit): Implementar um widget de filtro que permita ao usuário listar apenas os eventos de uma determinada semana ou mês.
Notificação de Sucesso (Streamlit): Após qualquer operação (inclusão, alteração, deleção), usar st.success() ou st.error() para fornecer feedback ao usuário.
Refatoração do datetime (API): Assegurar que os objetos datetime sejam manipulados corretamente entre o banco de dados (SQLite armazena como string ou timestamp), o modelo Pydantic e o front-end Streamlit.