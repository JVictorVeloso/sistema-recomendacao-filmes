# 🎬 Sistema de Recomendação de Filmes

Uma aplicação web interativa construída com Python e Streamlit que recomenda filmes com base na vasta base de dados do IMDb. Este projeto foi desenvolvido como parte do meu portfólio de Data Science/Análise de Dados.

![Screenshot da Aplicação](https://github.com/JVictorVeloso/sistema-recomendacao-filmes/blob/main/img.png)

---

## 📜 Sobre o Projeto

O objetivo deste projeto é demonstrar o ciclo completo de uma aplicação de dados, desde a coleta e limpeza de grandes volumes de dados até a criação de uma interface de usuário amigável e funcional para apresentar os resultados. A aplicação permite que o usuário selecione um gênero de filme e recebe em troca uma lista dos 10 filmes mais bem avaliados daquele gênero, de acordo com as notas do IMDb.

---

## ✨ Funcionalidades (Features)

- **Interface Web Interativa:** Construída com Streamlit para uma experiência de usuário limpa e moderna.
- **Seleção de Gênero:** Um menu dropdown permite ao usuário escolher facilmente entre dezenas de gêneros.
- **Processamento de Dados em Larga Escala:** Utiliza a biblioteca Pandas para carregar, limpar e processar milhões de registros da base de dados do IMDb.
- **Cache Inteligente:** O Streamlit armazena os dados processados em cache para garantir que a aplicação seja rápida e responsiva após o primeiro carregamento.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas de Dados:** Pandas
- **Framework Web:** Streamlit
- **Versionamento de Código:** Git e GitHub

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação no seu próprio computador.

```bash
# 1. Clone o repositório
git clone [https://github.com/JVictorVeloso/sistema-recomendacao-filmes.git](https://github.com/JVictorVeloso/sistema-recomendacao-filmes.git)

# 2. Navegue até a pasta do projeto
cd sistema-recomendacao-filmes

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
# source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Rode a aplicação Streamlit
streamlit run app.py
```

**Observação:** Os arquivos de dados do IMDb não estão incluídos neste repositório por excederem o limite de tamanho do GitHub. Para rodar o projeto, é necessário baixar os arquivos `title.basics.tsv.gz` e `title.ratings.tsv.gz` do site oficial do [IMDb Datasets](https://www.imdb.com/interfaces/) e colocá-los na pasta raiz do projeto.

---
