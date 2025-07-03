import streamlit as st
from time import sleep

@st.dialog("Incluir registro", width="large")
def post_data_dialog():
    user_options = ["Usar meu local :material/distance:", "Registrar em outro endereço :material/globe_location_pin:"]
    opt = st.radio("O registro é do seu local atual ou de outro endereço?", options=user_options)
    if opt == user_options[1]:
        st.text_input("CEP", icon=":material/pin_drop:")
    st.markdown("## Estime, com um valor de 1 a 10 (mais próximo de 1 = menor, mais próximo de 10 = maior), os seguintes dados referentes ao registro:")
    st.number_input("Dificuldade de acesso ao local", min_value=1, max_value=10, icon=":material/hiking:")
    st.number_input("Tamanho da área afetada", min_value=1, max_value=10, icon=":material/nature_people:")
    st.toggle("Há larvas :material/gesture:")
    st.markdown("Se possível, anexe uma evidência para seu registro. Isso aumenta a confiabilidade do dado.")
    st.file_uploader("Evidência (opcional)")
    if st.button("Publicar", icon=":material/send:", use_container_width=True):
        with st.spinner("Publicando dado..."):
            sleep(1.5)
        st.success("Dado publicado com sucesso!", icon=":material/check:")
        with st.spinner(" "):
            sleep(1.5)
        st.rerun()