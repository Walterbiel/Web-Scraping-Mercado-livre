import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
@st.cache_data
def load_data():
    # Substituir pelo caminho do seu dataset
    df = pd.read_csv('mercadolivre.csv')
    df = df.drop('Unnamed: 0',axis =1) 
    return df

df = load_data()

#df = load_data()

# Converter 'Nota' para numérico e tratar erros
df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")

# Sidebar para filtro de categoria
st.sidebar.header("Filtros")
categorias = df["Categoria"].dropna().unique()
categoria_selecionada = st.sidebar.selectbox("Selecione a Categoria", ["Todas"] + list(categorias))

# Filtrando os dados
if categoria_selecionada != "Todas":
    df_filtrado = df[df["Categoria"] == categoria_selecionada]
else:
    df_filtrado = df

st.title("Dashboard de Análise")

# Total de linhas
st.subheader("📌 Total de Linhas do Dataset")
st.write(len(df))

# Quantidade de valores nulos na coluna Nota
st.subheader("❌ Quantidade de Valores Nulos na Coluna 'Nota'")
st.write(df["Nota"].isna().sum())

# Nota Média por Categoria
st.subheader("⭐ Nota Média por Categoria")
nota_media = df.groupby("Categoria")["Nota"].mean().reset_index()
st.dataframe(nota_media)

# Preço Médio por Categoria
st.subheader("💰 Preço Médio por Categoria")
df["Preco"] = pd.to_numeric(df["Preco"], errors="coerce")  # Converter para numérico
preco_medio = df.groupby("Categoria")["Preco"].mean().reset_index()
st.dataframe(preco_medio)

# Histograma da distribuição de preços
st.subheader("📊 Distribuição de Preços")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df_filtrado["Preco"].dropna(), bins=20, kde=True, ax=ax)
ax.set_xlabel("Preço")
ax.set_ylabel("Frequência")
st.pyplot(fig)