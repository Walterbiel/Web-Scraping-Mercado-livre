import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar estilo do Seaborn
sns.set_theme(style="whitegrid")

# Carregar os dados
@st.cache_data
def load_data():
    df = pd.read_csv('mercadolivre.csv')
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")  # Evita erro se a coluna não existir
    return df

df = load_data()

# Converter 'Nota' e 'Preco' para numérico, tratando erros
df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
df["Preco"] = pd.to_numeric(df["Preco"], errors="coerce")

# Sidebar para filtro de categoria
st.sidebar.header("Filtros")
categorias = df["Categoria"].dropna().unique().tolist()
categoria_selecionada = st.sidebar.selectbox("Selecione a Categoria", ["Todas"] + categorias)

# Filtrando os dados
df_filtrado = df if categoria_selecionada == "Todas" else df[df["Categoria"] == categoria_selecionada]

st.title("📊 Dashboard de Análise")

# Total de linhas
st.subheader("📌 Total de Linhas do Dataset")
st.write(len(df_filtrado))

# Quantidade de valores nulos na coluna 'Nota'
st.subheader("❌ Quantidade de Valores Nulos na Coluna 'Nota'")
st.write(df_filtrado["Nota"].isna().sum())

# Nota Média por Categoria
st.subheader("⭐ Nota Média por Categoria")
nota_media = df_filtrado.groupby("Categoria", as_index=False)["Nota"].mean()

fig, ax = plt.subplots(figsize=(8, 5))  # Criando figura e eixo
sns.barplot(data=nota_media, x="Nota", y="Categoria", ax=ax)  # Especificando `ax`
ax.set_xlabel("Nota Média")
ax.set_ylabel("Categoria")

st.pyplot(fig)  # Agora passando a figura corretamente
# Preço Médio por Categoria
st.subheader("💰 Preço Médio por Categoria")
preco_medio = df_filtrado.groupby("Categoria", as_index=False)["Preco"].mean()
st.dataframe(preco_medio)

# Histograma da distribuição de preços
st.subheader("📊 Distribuição de Preços")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df_filtrado["Preco"].dropna(), bins=20, kde=True, ax=ax)
ax.set_xlabel("Preço")
ax.set_ylabel("Frequência")
st.pyplot(fig)
