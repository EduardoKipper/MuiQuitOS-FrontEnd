import streamlit as st
from datetime import date, timedelta
import random
import pandas as pd

datas = [(date.today() - timedelta(days=i)).isoformat() for i in range(10)]

dados = {
    "Nome": [
        "Ana Silva", "Bruno Costa", "Camila Rocha", "Daniel Souza", "Eduarda Lima",
        "Felipe Alves", "Gabriela Pinto", "Henrique Fernandes", "Isabela Moraes", "João Pereira"
    ],
    "Cidade": [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Curitiba", "Recife", "Porto Alegre", "Manaus", "Brasília"
    ],
    "Quantidade": [random.randint(1, 100) for _ in range(10)],
    "Data": datas
}

def data():
    st.title(":material/dashboard: Dados de mosquitos :material/bug_report:")
    cols = st.columns(3)

    # --- DataFrame ---
    df = pd.DataFrame(dados)

    # --- Exibição de Dados ---
    st.dataframe(df)

    # --- Line Chart: Quantidade ao longo do tempo ---
    line_df = df.set_index('Data')['Quantidade']
    cols[0].line_chart(line_df, color="#1bd072")

    # --- Bar Chart: Quantidade por Cidade ---
    bar_df = df.set_index('Cidade')['Quantidade']
    cols[1].bar_chart(bar_df, color="#1bd072")

    # --- Area Chart: Quantidade ao longo do tempo ---
    cols[2].area_chart(line_df, color="#1bd072")
