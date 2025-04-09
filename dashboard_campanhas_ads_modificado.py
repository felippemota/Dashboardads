
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do App
st.title("📊 Dashboard de Anúncios - Custo x Lucro")

# Carregando os dados
df = pd.read_excel("dashboard_campanhas_modificado.xlsx")

# Exibição da Tabela com foco
st.subheader("📋 Detalhamento das Campanhas")
st.dataframe(df, use_container_width=True)

# Gráfico de dispersão: Custo x Lucro
st.subheader("💸 Relação Custo x Lucro")

fig, ax = plt.subplots(figsize=(6, 4))
scatter = ax.scatter(df['cost'], df['lucro'], color='green', s=50)
ax.set_xlabel("Custo (R$)")
ax.set_ylabel("Lucro (R$)")
ax.set_title("Dispersão: Custo vs Lucro")
st.pyplot(fig)

# Rodapé
st.markdown("---")
st.caption("Criado por Lewis para o bebê empreendedor 💚")
