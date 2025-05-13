import streamlit as st
from src.views.data import data
from src.views.login import login_dialog

st.set_page_config(layout="wide")

data_page = st.Page(data, title="Dados", icon=":material/dashboard:")

if not st.session_state.get("authorized"):
    login_dialog()
    
if st.session_state.get('authorized'):
    pg = st.navigation([data_page])
    pg.run()
