import streamlit as st
import pandas as pd


# 1. Função para carregar e preparar os dados (com cache)
@st.cache_data
def carregar_dados():
    print(
        "Carregando e limpando os dados... (Isso só deve acontecer uma vez por sessão)"
    )
    try:
        # --- ALTERAÇÃO PRINCIPAL AQUI ---
        # Lendo os arquivos de AMOSTRA (sample), que são mais leves para o deploy.
        basics_df = pd.read_csv(
            "sample_title.basics.tsv.gz", sep="\t", low_memory=False
        )
        ratings_df = pd.read_csv("sample_title.ratings.tsv.gz", sep="\t")
    except FileNotFoundError:
        st.error(
            "Arquivos de dados de amostra não encontrados! Execute o script `create_sample.py` primeiro e envie as alterações para o GitHub."
        )
        return None

    filmes_df = pd.merge(basics_df, ratings_df, on="tconst")
    filmes_df = filmes_df[filmes_df["titleType"] == "movie"]
    filmes_df["startYear"] = pd.to_numeric(filmes_df["startYear"], errors="coerce")
    filmes_df["averageRating"] = pd.to_numeric(
        filmes_df["averageRating"], errors="coerce"
    )
    filmes_df["numVotes"] = pd.to_numeric(filmes_df["numVotes"], errors="coerce")

    # Reduzimos o filtro de votos para a amostra, para garantir que teremos resultados
    filmes_df = filmes_df[filmes_df["numVotes"] > 1000]
    print("Dados prontos!")
    return filmes_df


# 2. Função de recomendação (a mesma que você já tinha)
def recomendar_por_genero(df, genero):
    filmes_do_genero = df[df["genres"].str.contains(genero, na=False, case=False)]
    top_10 = filmes_do_genero.sort_values(by="averageRating", ascending=False).head(10)
    return top_10[["primaryTitle", "startYear", "averageRating", "genres"]]


# --- Interface da Aplicação Web ---

st.set_page_config(layout="wide")  # Deixa a página mais larga
st.title("🎬 Sistema de Recomendação de Filmes")
# Alteramos a descrição para informar que é uma amostra
st.write(
    "Uma aplicação web simples para recomendar filmes baseada em uma amostra da base de dados do IMDb."
)

# Carrega os dados
filmes_df = carregar_dados()

if filmes_df is not None:
    # Cria uma lista de gêneros únicos para o usuário escolher
    generos = sorted(pd.unique(filmes_df["genres"].str.split(",").explode()))

    # Adiciona um item inicial "Selecione" para guiar o usuário
    generos.insert(0, "Selecione um gênero")

    # Cria a interface na tela
    genero_selecionado = st.selectbox("Escolha um gênero:", generos)

    # Mostra as recomendações se um gênero válido for escolhido
    if genero_selecionado != "Selecione um gênero":
        recomendacoes = recomendar_por_genero(filmes_df, genero_selecionado)
        st.write(f"Top 10 filmes do gênero: **{genero_selecionado}**")
        st.dataframe(recomendacoes, use_container_width=True)
