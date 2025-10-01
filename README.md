🎬 Sistema de Recomendação de Filmes
➡️ Ver a Aplicação Online
Uma aplicação web interativa construída com Python e Streamlit que recomenda filmes com base numa amostra da vasta base de dados do IMDb. Este projeto foi desenvolvido como parte do meu portfólio de Análise de Dados e Engenharia de Software.

📜 Sobre o Projeto
O objetivo deste projeto é demonstrar o ciclo completo de uma aplicação de dados, desde a recolha e limpeza de dados até à criação de uma interface de utilizador funcional (UI). A versão online utiliza uma amostra dos dados para garantir um desempenho rápido e cumprir os limites de memória do ambiente de deploy gratuito.

A aplicação permite que o utilizador selecione um género de filme e receba em troca uma lista dos 10 filmes mais bem avaliados daquele género.

✨ Funcionalidades
Interface Web Interativa: Construída com Streamlit para uma experiência de utilizador limpa e moderna.

Seleção de Género: Um menu dropdown permite ao utilizador escolher facilmente entre dezenas de géneros.

Processamento de Dados com Pandas: Utiliza a biblioteca Pandas para carregar, limpar e processar os ficheiros de dados.

Cache Inteligente: O Streamlit armazena os dados processados em cache para garantir que a aplicação seja rápida e responsiva após o primeiro carregamento.

Deploy Contínuo: A aplicação está hospedada no Streamlit Community Cloud e é atualizada automaticamente a cada push para a branch main.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Bibliotecas de Dados: Pandas

Framework Web: Streamlit

Versionamento de Código: Git & GitHub

Hospedagem: Streamlit Community Cloud

🚀 Como Executar o Projeto Localmente
Siga os passos abaixo para rodar a aplicação no seu próprio computador.

# 1. Clone o repositório
git clone [https://github.com/JVictorVeloso/sistema-recomendacao-filmes.git](https://github.com/JVictorVeloso/sistema-recomendacao-filmes.git)

# 2. Navegue até à pasta do projeto
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

Observação sobre os dados: A versão online utiliza ficheiros de amostra (sample_...) para otimização. Os dados originais e completos podem ser descarregados do IMDb Datasets.