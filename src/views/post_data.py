import streamlit as st
from src.controllers.post_data import post_data
from time import sleep

@st.dialog("Incluir registro", width="large")
def post_data_dialog():
    cep = st.text_input("CEP", icon=":material/pin_drop:")
    intensity = st.number_input("Intensidade", min_value=1, max_value=5, icon=":material/device_thermostat:")
    if st.button("Publicar", icon=":material/send:", use_container_width=True):
        with st.spinner("Publicando dado..."):
            success = post_data(user=st.session_state['user'], cep=cep, intensity=intensity)
        if success:
            st.success("Dado publicado com sucesso!", icon=":material/check:")
            sleep(1.5)
            st.rerun()
        else:
            st.error("Erro ao publicar dado", icon=":material/error:")