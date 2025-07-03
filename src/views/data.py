import streamlit as st
import pandas as pd
import pydeck as pdk
from src.views.post_data import post_data_dialog
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
    # --- DataFrame ---
    df = pd.DataFrame(dados_mock)
    df_exemplo = pd.read_csv("database/registers.csv")
    st.title(":material/dashboard: MuiQuitOS Dashboard :material/bug_report:")

    if st.button("Fazer uma publicação", icon=":material/add:", use_container_width=True):
        post_data_dialog()

    # --- Mapa dos Registros ---
    st.markdown("### Mapa de Registros de Focos de Mosquitos")
    
    # Preparar dados para o mapa
    map_data = df_exemplo.copy()
    map_data = map_data.dropna(subset=['latitude', 'longitude'])
    
    # Configurar o mapa
    view_state = pdk.ViewState(
        latitude=-27.5954,
        longitude=-48.5480,
        zoom=9,
        pitch=0,
    )

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_data,
        get_position='[longitude, latitude]',
        get_color='[200, 30, 0, 160]',
        get_radius='intensity * 100',
        radius_scale=1,
        radius_min_pixels=5,
        radius_max_pixels=50,
        pickable=True,
    )

    tooltip = {
        "html": "<b>Bairro:</b> {neighbourhood}<br/>"
                "<b>Dificuldade de Acesso:</b> {access_difficulty}<br/>"
                "<b>Presença de Larvas:</b> {larvae}",
                "<b>Intensidade:</b> {intensity}<br/>"
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="mapbox://styles/mapbox/light-v9",
        tooltip=tooltip
    )

    st.pydeck_chart(r)

    cols = st.columns(3)
    cols2 = st.columns(2)


    # --- Exibição de Dados ---
    cols2[0].dataframe(df)
    cols2[1].dataframe(df_exemplo)

    # --- Line Chart: Intensidade ao longo do tempo ---
    cols[0].markdown("### Intensidade de focos de mosquitos ao longo do tempo")
    line_df = df.set_index('Data')['Intensidade']
    cols[0].line_chart(line_df, color="#1bd072")

    # --- Bar Chart: Intensidade por Cidade ---
    cols[1].markdown("### Intensidade de focos de mosquitos por cidade")
    bar_df = df.set_index('Cidade')['Intensidade']
    cols[1].bar_chart(bar_df, color="#1bd072")

    # --- Area Chart: Intensidade ao longo do tempo ---
    cols[2].markdown("### Registros de focos ao longo do tempo")
    cols[2].area_chart(line_df, color="#1bd072")
