import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configurações de estilo do Seaborn e Matplotlib
sns.set(style="whitegrid")
plt.style.use('ggplot')

# Título da aplicação
st.title("Análise de Renda")

# Carregar o arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploaded_file is not None:
    renda = pd.read_csv(uploaded_file)
    
    # Criar novas variáveis
    renda['idade_emprego_ratio'] = renda['tempo_emprego'] / (renda['idade'] + 1)
    renda['densidade_dependentes'] = renda['qtd_filhos'] / renda['qt_pessoas_residencia']
    renda['renda_per_capita'] = renda['renda'] / renda['qt_pessoas_residencia']
    renda['estabilidade_renda'] = renda['tipo_renda'].apply(lambda x: 1 if x in ['Assalariado', 'Empresário'] else 0)
    renda['posse_bens'] = renda['posse_de_veiculo'].astype(int) + renda['posse_de_imovel'].astype(int)
    renda['hist_emprego'] = renda['tempo_emprego'] / renda['idade']
    
    # Visualização 1: Idade vs. Renda
    st.subheader("Idade vs. Renda")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['idade'], renda['renda'], c='blue', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Idade', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Idade vs. Renda', fontsize=15)
    st.pyplot(fig)

    # Visualização 2: Posse de Veículo vs. Renda
    st.subheader("Posse de Veículo vs. Renda")
    fig, ax = plt.subplots()
    sns.boxplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax, palette="Set2")
    ax.set_xlabel('Posse de Veículo', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Posse de Veículo vs. Renda', fontsize=15)
    st.pyplot(fig)
    
    # Tabela de Contingência: Estado Civil vs. Tipo de Residência
    st.subheader("Tabela de Contingência: Estado Civil vs. Tipo de Residência")
    tabela_contingencia = pd.crosstab(renda['estado_civil'], renda['tipo_residencia'])
    st.write(tabela_contingencia)
    
    # Visualização 3: Tipo de Renda vs. Quantidade de Filhos
    st.subheader("Tipo de Renda vs. Quantidade de Filhos")
    fig, ax = plt.subplots()
    sns.barplot(x='tipo_renda', y='qtd_filhos', data=renda, estimator=sum, ax=ax, palette="viridis")
    ax.set_xlabel('Tipo de Renda', fontsize=12)
    ax.set_ylabel('Quantidade de Filhos', fontsize=12)
    ax.set_title('Tipo de Renda vs. Quantidade de Filhos', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 4: Idade vs. Tempo de Emprego
    st.subheader("Idade vs. Tempo de Emprego")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['idade'], renda['tempo_emprego'], c='green', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Idade', fontsize=12)
    ax.set_ylabel('Tempo de Emprego', fontsize=12)
    ax.set_title('Idade vs. Tempo de Emprego', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 5: Idade vs. Razão Idade/Tempo de Emprego
    st.subheader("Idade vs. Razão Idade/Tempo de Emprego")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['idade'], renda['idade_emprego_ratio'], c='purple', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Idade', fontsize=12)
    ax.set_ylabel('Razão Idade/Tempo de Emprego', fontsize=12)
    ax.set_title('Idade vs. Razão Idade/Tempo de Emprego', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 6: Densidade de Dependentes vs. Renda
    st.subheader("Densidade de Dependentes vs. Renda")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['densidade_dependentes'], renda['renda'], c='orange', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Densidade de Dependentes', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Densidade de Dependentes vs. Renda', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 7: Renda per Capita vs. Renda Total
    st.subheader("Renda per Capita vs. Renda Total")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['renda_per_capita'], renda['renda'], c='red', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Renda per Capita', fontsize=12)
    ax.set_ylabel('Renda Total', fontsize=12)
    ax.set_title('Renda per Capita vs. Renda Total', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 8: Estabilidade da Renda vs. Renda
    st.subheader("Estabilidade da Renda vs. Renda")
    fig, ax = plt.subplots()
    sns.boxplot(x='estabilidade_renda', y='renda', data=renda, ax=ax, palette="coolwarm")
    ax.set_xlabel('Estabilidade da Renda', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Estabilidade da Renda vs. Renda', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 9: Posse de Bens vs. Renda
    st.subheader("Posse de Bens vs. Renda")
    fig, ax = plt.subplots()
    sns.boxplot(x='posse_bens', y='renda', data=renda, ax=ax, palette="Paired")
    ax.set_xlabel('Posse de Bens', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Posse de Bens vs. Renda', fontsize=15)
    st.pyplot(fig)
    
    # Visualização 10: Histórico de Emprego vs. Renda
    st.subheader("Histórico de Emprego vs. Renda")
    fig, ax = plt.subplots()
    scatter = ax.scatter(renda['hist_emprego'], renda['renda'], c='brown', alpha=0.6, edgecolors='w', linewidth=0.5)
    ax.set_xlabel('Histórico de Emprego', fontsize=12)
    ax.set_ylabel('Renda', fontsize=12)
    ax.set_title('Histórico de Emprego vs. Renda', fontsize=15)
    st.pyplot(fig)
else:
    st.write("Por favor, faça o upload de um arquivo CSV.")
