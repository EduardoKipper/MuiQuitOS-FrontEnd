import streamlit as st
import pandas as pd
from src.views.post_data import post_data_dialog
from src.controllers.get_data import get_data

def data():
    st.title(":material/dashboard: Dados de mosquitos :material/bug_report:")

    if st.button("Fazer uma publicação", icon=":material/add:", use_container_width=True):
        post_data_dialog()

    with st.spinner("Buscando dados..."):
        dados = get_data()

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
