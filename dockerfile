FROM python:3.12
# Define o diretório de trabalho dentro do contêiner
WORKDIR /app
# Copia os arquivos do projeto para o contêiner
COPY pyproject.toml poetry.lock /app/
# Instala o Poetry
RUN pip install --no-cache-dir poetry
# Instala as dependências do projeto usando o Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi
# Copia o restante dos arquivos do projeto
COPY . /app
# Expõe a porta padrão do Streamlit
EXPOSE 8501
# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]