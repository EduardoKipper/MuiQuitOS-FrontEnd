import streamlit as st
from src.controllers.login import login

@st.dialog("Login", width="large")
def login_dialog():
    st.markdown("## Insira suas credenciais para acessar o sistema")
    user = st.text_input("Usuário", icon=":material/person:")
    password = st.text_input("Senha", icon=":material/key:", type="password")
    if st.button("Entrar", use_container_width=True):
        with st.spinner("Validando informações..."):
            success = login(user=user, password=password)
        if success:
            st.session_state["user"] = user
            st.session_state["authorized"] = True
            st.rerun()
        else:
            st.error("Informações incorretas", icon=":material/error:")
