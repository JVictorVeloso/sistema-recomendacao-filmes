import pandas as pd

print("Criando amostra dos arquivos de dados...")

# Nomes dos arquivos originais
basics_original = "title.basics.tsv.gz"
ratings_original = "title.ratings.tsv.gz"

# Nomes dos novos arquivos de amostra
basics_sample = "sample_title.basics.tsv.gz"
ratings_sample = "sample_title.ratings.tsv.gz"

try:
    # Processa o arquivo 'basics'
    print(f"Lendo uma parte de {basics_original}...")
    # Lê as primeiras 500,000 linhas para criar a amostra
    df_basics_sample = pd.read_csv(
        basics_original, sep="\t", low_memory=False, nrows=500000
    )
    df_basics_sample.to_csv(basics_sample, sep="\t", index=False, compression="gzip")
    print(f"Arquivo '{basics_sample}' criado com sucesso!")

    # Processa o arquivo 'ratings'
    print(f"Lendo uma parte de {ratings_original}...")
    df_ratings_sample = pd.read_csv(
        ratings_original, sep="\t", low_memory=False, nrows=500000
    )
    df_ratings_sample.to_csv(ratings_sample, sep="\t", index=False, compression="gzip")
    print(f"Arquivo '{ratings_sample}' criado com sucesso!")

    print("\nProcesso de criação de amostras concluído.")

except FileNotFoundError as e:
    print(
        f"\nERRO: Arquivo não encontrado. Certifique-se que os arquivos de dados originais estão na pasta."
    )
    print(e)
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
