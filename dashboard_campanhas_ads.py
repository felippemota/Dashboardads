
# Dashboard interativo com Streamlit para análise de campanhas

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados (certifique-se de que o arquivo esteja no mesmo diretório)
df = pd.read_excel("analise_completa_53_campanhas_ads_lewis (1).xlsx")

st.set_page_config(page_title="Dashboard Campanhas Ads", layout="wide")
st.title("📊 Análise de Campanhas Ads - CapriShop")

# Filtros laterais
st.sidebar.header("Filtros")
nome_campanha = st.sidebar.multiselect("Selecionar campanha", df['name'].unique(), default=df['name'].unique())

filtro_df = df[df['name'].isin(nome_campanha)]

# Métricas principais
col1, col2, col3, col4 = st.columns(4)
col1.metric("Custo Total", f"R$ {filtro_df['cost'].sum():.2f}")
col2.metric("Conversões", int(filtro_df['units_quantity'].sum()))
col3.metric("ROAS Médio", f"{filtro_df['roas'].mean():.2f}")
col4.metric("ACOS Médio", f"{filtro_df['acos'].mean():.2f}%")

st.markdown("---")

# Gráfico de dispersão ACOS vs ROAS
st.subheader("Performance por Campanha")
fig, ax = plt.subplots()
ax.scatter(filtro_df['acos'], filtro_df['roas'], color='blue')
ax.set_xlabel("ACOS (%)")
ax.set_ylabel("ROAS")
ax.set_title("Dispersão ACOS x ROAS")
st.pyplot(fig)

# Tabela com recomendações
st.subheader("Detalhamento das Campanhas")
st.dataframe(filtro_df[['name', 'budget', 'cost', 'clicks', 'units_quantity', 'acos', 'roas', 'recomendação']])
