# Observatorio Economico - BCB
https://indicadoresbcb.streamlit.app/

  <h1>📊 Observatório Econômico Automatizado</h1>

  <p>
    <strong>Uma aplicação web interativa para monitoramento em tempo real de indicadores macroeconômicos brasileiros.</strong>
  </p>

  <a href="seu_link_do_streamlit_cloud_aqui">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit">
  </a>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Data_Science-Business_Intelligence-00ffcc?style=for-the-badge" alt="Data Science">
</div>

---

## 📝 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema comum no setor bancário e financeiro: a coleta manual e a visualização descentralizada de taxas de mercado. 

O **Observatório Econômico** automatiza a extração de dados oficiais diretamente do Banco Central do Brasil (BCB) e consolida essas séries temporais em um dashboard analítico interativo, permitindo análises rápidas sobre o cenário macroeconômico (como a relação entre a Taxa Selic e a Inadimplência ou o impacto do INCC no mercado imobiliário).

### 🚀 Principais Funcionalidades

* **Extração Automatizada (Web Scraping / API):** Consumo direto do Sistema Gerenciador de Séries Temporais (SGS) do Banco Central.
* **Mapeamento de Indicadores Chave:** Monitoramento de Selic, IPCA, Dólar, INCC, Inadimplência, Desemprego e Saldo da Poupança.
* **Motor de Dados Robusto:** Tratamento automático de exceções e instabilidades de APIs governamentais, garantindo a disponibilidade da aplicação.
* **Visualização Interativa:** Gráficos dinâmicos com *zoom*, *hover* de dados e ajuste de granularidade temporal, construídos com Plotly.
* **Design UI/UX:** Interface projetada em *Dark Mode* para ambientes corporativos, com foco na clareza da informação.

---

## 🛠️ Tecnologias Utilizadas

O ecossistema do projeto é 100% baseado em Python, dispensando ferramentas tradicionais de BI para demonstrar capacidade de desenvolvimento *End-to-End*:

* **[Streamlit](https://streamlit.io/):** Criação da interface Web e roteamento do Front-end.
* **[Pandas](https://pandas.pydata.org/):** Limpeza, estruturação e manipulação das séries temporais.
* **[python-bcb](https://github.com/wilsonfreitas/python-bcb):** Biblioteca especializada para consumo da API do Banco Central do Brasil.
* **[Plotly](https://plotly.com/python/):** Renderização dos gráficos interativos.

---

## ⚙️ Como executar o projeto localmente

Acesse: https://indicadoresbcb.streamlit.app/

---

## 👤 Autor

João Paulo R. Souza — [github.com/jprsouza87](https://github.com/jprsouza87)
