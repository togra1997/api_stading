"""front end ui."""

import streamlit as st
from ui import delete_ui, registar_ui, totaling_ui

st.title("工数管理アプリ(メインAPI)")

tab = st.tabs(["登録", "集計", "削除"])

with tab[0]:
    registar_ui()
with tab[1]:
    totaling_ui()
with tab[2]:
    delete_ui()
