import streamlit as st
import pandas as pd
from src.views.post_data import post_data_dialog
from src.controllers.get_data import get_data
from datetime import date, timedelta
import random

datas = [(date.today() - timedelta(days=i)).isoformat() for i in range(20)]

dados_mock = {
    "Cidade": [
        "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Curitiba", "Recife", "Porto Alegre", "Manaus", "Brasília","São Paulo", 
        "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza",
        "Curitiba", "Recife", "Porto Alegre", "Manaus", "Brasília"
    ],
    "Intensidade": [random.randint(1, 10) for _ in range(20)],
    "Data": datas
}

def data():
    st.title(":material/dashboard: MuiQuitOS Dashboard :material/bug_report:")

    if st.button("Fazer uma publicação", icon=":material/add:", use_container_width=True):
        post_data_dialog()

    # with st.spinner("Buscando dados..."):
        # dados = get_data()
    dados = dados_mock

    cols = st.columns(3)

    # --- DataFrame ---
    df = pd.DataFrame(dados)

    # --- Exibição de Dados ---
    st.dataframe(df)

    # --- Line Chart: Intensidade ao longo do tempo ---
    line_df = df.set_index('Data')['Intensidade']
    cols[0].line_chart(line_df, color="#1bd072")

    # --- Bar Chart: Intensidade por Cidade ---
    bar_df = df.set_index('Cidade')['Intensidade']
    cols[1].bar_chart(bar_df, color="#1bd072")

    # --- Area Chart: Intensidade ao longo do tempo ---
    cols[2].area_chart(line_df, color="#1bd072")
