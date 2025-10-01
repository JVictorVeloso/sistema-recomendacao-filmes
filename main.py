import pandas as pd

print("Iniciando o sistema de recomendação...")

try:
    # --- Carregamento dos Dados ---
    # Lendo os arquivos com a extensão .gz, como estão na sua pasta agora
    print("Carregando dados de títulos...")
    basics_df = pd.read_csv("title.basics.tsv.gz", sep="\t", low_memory=False)

    print("Carregando dados de notas...")
    ratings_df = pd.read_csv("title.ratings.tsv.gz", sep="\t")

    # --- Junção e Limpeza dos Dados ---
    print("Juntando e limpando os dados... (Isso pode levar um momento)")

    # Juntar (merge) os dois dataframes
    filmes_df = pd.merge(basics_df, ratings_df, on="tconst")

    # Filtrar para manter apenas filmes ('movie')
    filmes_df = filmes_df[filmes_df["titleType"] == "movie"]

    # Converter colunas para tipos numéricos, tratando erros
    filmes_df["startYear"] = pd.to_numeric(filmes_df["startYear"], errors="coerce")
    filmes_df["averageRating"] = pd.to_numeric(
        filmes_df["averageRating"], errors="coerce"
    )
    filmes_df["numVotes"] = pd.to_numeric(filmes_df["numVotes"], errors="coerce")

    # Remover filmes com poucos votos para ter resultados mais relevantes
    # Um bom limiar é ter pelo menos 5000 votos
    filmes_df = filmes_df[filmes_df["numVotes"] > 5000]

    print("Dados prontos para análise!")

    # --- Lógica de Recomendação ---
    def recomendar_por_genero(df, genero):
        """
        Filtra o dataframe por um gênero e retorna os 10 melhores filmes.
        """
        # Filtra filmes que contêm o gênero na coluna 'genres' (ignorando maiúsculas/minúsculas)
        filmes_do_genero = df[df["genres"].str.contains(genero, na=False, case=False)]

        # Ordenar pela nota (do maior para o menor)
        top_10 = filmes_do_genero.sort_values(by="averageRating", ascending=False).head(
            10
        )

        # Retorna apenas as colunas que nos interessam
        return top_10[["primaryTitle", "startYear", "averageRating", "genres"]]

    # --- Interface com o Usuário (no terminal) ---
    if __name__ == "__main__":
        # Loop infinito para permitir várias buscas
        while True:
            genero_usuario = input(
                "\nQual seu gênero de filme favorito? (ou digite 'sair' para fechar): "
            )

            if genero_usuario.lower() == "sair":
                break

            recomendacoes = recomendar_por_genero(filmes_df, genero_usuario)

            if recomendacoes.empty:
                print(
                    f"\nDesculpe, não encontrei filmes populares do gênero '{genero_usuario}'. Tente outro (ex: Action, Comedy, Drama)."
                )
            else:
                print(
                    f"\n--- Top 10 filmes de '{genero_usuario.capitalize()}' recomendados para você ---"
                )
                print(recomendacoes.to_string(index=False))

except FileNotFoundError:
    print(
        "\nERRO: Arquivos de dados ('title.basics.tsv.gz' ou 'title.ratings.tsv.gz') não encontrados!"
    )
    print(
        "Por favor, certifique-se de que os arquivos estão na mesma pasta que o script 'main.py'."
    )
