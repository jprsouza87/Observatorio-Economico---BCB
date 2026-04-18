import streamlit as st
import pandas as pd
from bcb import sgs
import plotly.express as px

# 1. Configuração inicial da página
st.set_page_config(page_title="Observatório Econômico", page_icon="📊", layout="centered")

st.title("📊 Observatório de Indicadores Econômicos")
st.markdown("Acompanhe as principais taxas do mercado atualizadas direto do Banco Central.")

# 2. Barra Lateral (Filtros do Usuário)
st.sidebar.header("Indicadores")

# Dicionário inteligente mapeando o nome amigável para o código do BCB
indicadores = {
    "Taxa Selic (% a.a.)": 432,
    "IPCA (% ao mês)": 433,
    "IGP-M (% ao mês)": 189,
    "Dólar - Taxa de Venda": 10813,
    "INCC - Custo da Construção": 192,
    "Inadimplência PF (%)": 21082,
    "Desemprego - PNADC (%)": 24369,
    "Saldo da Poupança (Milhões R$)": 195
}

# O usuário escolhe o nome, o código descobre o número
escolha_indicador = st.sidebar.selectbox("Selecione o Indicador:", list(indicadores.keys()))
codigo_selecionado = indicadores[escolha_indicador]

# Um slider interativo para escolher quantos meses analisar
meses_historico = st.sidebar.slider("Período de análise (meses):", min_value=1, max_value=36, value=12, step=1)

# 3. Motor de Dados Robustecido
@st.cache_data
def carregar_dados(codigo, meses):
    try:
        data_inicio = pd.Timestamp.today() - pd.DateOffset(months=meses)
        data_inicio_str = data_inicio.strftime('%Y-%m-%d')
        
        # Tentativa de busca
        df = sgs.get({'valor': codigo}, start=data_inicio_str)
        
        if df is None or df.empty:
            return pd.DataFrame() # Retorna vazio se não achar nada
            
        df = df.reset_index()
        
        # Ajuste dinâmico: o BCB às vezes chama a coluna de 'Date', 'index' ou 'data'
        # Vamos renomear a primeira coluna (que é a data) para 'Data_Ref' para garantir
        df.rename(columns={df.columns[0]: 'Data_Ref'}, inplace=True)
        
        return df
    except Exception as e:
        return pd.DataFrame()

# Executando a função
dados_df = carregar_dados(codigo_selecionado, meses_historico)

# 4. Construindo o Visual Principal com verificação de segurança
if not dados_df.empty:
    ultimo_valor = dados_df['valor'].iloc[-1]
    # Usamos a nossa coluna garantida 'Data_Ref'
    ultima_data = dados_df['Data_Ref'].iloc[-1].strftime('%d/%m/%Y')

    st.subheader(f"Evolução Histórica: {escolha_indicador}")
    st.metric(label=f"Valor mais recente (Data ref: {ultima_data})", value=f"{ultimo_valor:.2f}")

    fig = px.line(dados_df, x='Data_Ref', y='valor', markers=True)
    fig.update_layout(xaxis_title="Data", yaxis_title="Valor", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error(f"Não foi possível obter dados para {escolha_indicador} no momento. Tente um período menor ou outro indicador.")

st.markdown(
    """
    <div style="
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #30363d;
        color: #8b949e;
        font-size: 0.8rem;
        text-align: center;
    ">
        Desenvolvido por João Paulo R. de Souza
    </div>
    """,
    unsafe_allow_html=True,
)
