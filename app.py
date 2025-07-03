import streamlit as st
from src.views.data import data
from src.views.login import login_dialog, register_user_dialog

st.set_page_config(layout="wide", page_icon=":material/bug_report:", page_title="MuiQuitOS")

data_page = st.Page(data, title="Dados", icon=":material/dashboard:")

if not st.session_state.get("login_or_register"):
    st.session_state["login_or_register"] = "login"

if not st.session_state.get("authorized"):
    if st.session_state["login_or_register"] == "login":
        login_dialog()
    else:
        register_user_dialog()
    
if st.session_state.get('authorized'):
    pg = st.navigation([data_page])
    pg.run()
