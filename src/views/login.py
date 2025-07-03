import streamlit as st
from time import sleep

@st.dialog("Login", width="large")
def login_dialog():
    st.markdown("## Insira suas credenciais para acessar o sistema")
    user = st.text_input("Usuário", icon=":material/person:")
    st.text_input("Senha", icon=":material/key:", type="password")
    with st.container(border=True):
        cols = st.columns(2)
        cols[0].markdown("#### Alternativamente, cadastre-se")
        if cols[1].button("Cadastrar-se", use_container_width=True):
            st.session_state["login_or_register"] = "register"
            st.rerun()
    if st.button("Entrar", icon=":material/login:", use_container_width=True):
        with st.spinner("Validando informações..."):
            sleep(1.5)
        st.session_state["user"] = user
        st.session_state["authorized"] = True
        st.success("Sucesso", icon=":material/check:")
        with st.spinner(" "):
            sleep(1.5)
        st.rerun()

user_types = ["Comum", "Autoridade", "Entidade"]

@st.dialog("Registro", width="large")
def register_user_dialog():
    st.markdown("## Insira suas credenciais para se cadastrar no sistema")
    user = st.text_input("Insira um nome de usuário", icon=":material/person:")
    st.text_input("Crie uma senha", icon=":material/key:", type="password")
    user_type = st.pills("Tipo de usuário", options=user_types, default=user_types[0])
    if user_type != "Comum":
        st.file_uploader("Envie um comprovante para análise de seu status")
    if st.button("Registrar", icon=":material/login:", use_container_width=True):
        with st.spinner("Validando informações..."):
            sleep(1.5)
        st.session_state["user"] = user
        st.session_state["authorized"] = True
        st.success("Sucesso", icon=":material/check:")
        with st.spinner(" "):
            sleep(1.5)
        st.rerun()
