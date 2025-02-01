### Web Screaping do site do mercado livre para análise de mercado (Python,pandas,Selenium,streamlit,docker)

## Descrição
Este projeto tem como objetivo extrair informações de produtos do site Mercado Livre utilizando Web Scraping com Selenium, realizar o tratamento dos dados com Pandas e visualizar as informações em um dashboard interativo utilizando Seaborn e Streamlit. Para facilitar a distribuição e execução do projeto, foi criado um ambiente Docker com dependências gerenciadas pelo Poetry.

## Tecnologias Utilizadas
- **Python**: Linguagem principal para desenvolvimento do projeto.
- **Selenium**: Biblioteca para automação do navegador e extração de informações do Mercado Livre.
- **Pandas**: Biblioteca para manipulação e tratamento dos dados coletados.
- **Seaborn**: Biblioteca para criação de visualizações gráficas.
- **Streamlit**: Ferramenta para criação do dashboard interativo.
- **Docker**: Containeração do projeto para facilitar a execução em diferentes ambientes.
- **Poetry**: Gerenciador de dependências do projeto dentro do container Docker.

## Estrutura do Projeto
```
projeto/
│-- src/
│   │-- web-scraping.py  # Script para extração de dados com Selenium
│   │-- app.py  # Criação do dashboard com Streamlit e Seaborn
│-- Dockerfile  # Configuração do container Docker
│-- pyproject.toml  # Arquivo de dependências gerenciado pelo Poetry
│-- README.md  # Documentação do projeto
```

## Como Executar o Projeto
### 1. Clonar o repositório
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Construir e Executar o Container Docker
```sh
docker build -t nome-do-projeto .
docker run -p 8501:8501 nome-do-projeto
```

### 3. Acessar o Dashboard
Após rodar o container, acesse o dashboard no navegador:
```
http://localhost:8501
```

## Funcionalidades
- **Web Scraping**: Extração automática de informações do Mercado Livre.
- **Tratamento de Dados**: Limpeza e organização dos dados para análise.
- **Dashboard Interativo**: Visualização dos dados em tempo real.
- **Deploy com Docker**: Execução simplificada do projeto em qualquer ambiente.


