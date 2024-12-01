"""登録UI."""

import json

import pandas as pd
import requests
import streamlit as st


def registar_ui() -> None:
    """登録UI."""
    col1, col2 = st.columns(2)

    with col1:
        start_time = st.time_input("開始時間")

    with col2:
        end_time = st.time_input("終了時間")

    kousuutukesaki = st.text_input("工数付け先")
    annkenn = st.text_input("案件名")
    work = st.text_input("作業")

    if st.button("登録"):
        url = "http://127.0.0.1:8000"

        res = requests.post(
            url=url,
            data=json.dumps(
                {
                    "start_time": f"{start_time}",
                    "end_time": f"{end_time}",
                    "annkenn": f"{annkenn}",
                    "work": f"{work}",
                    "kousuutukesaki": f"{kousuutukesaki}",
                },
            ),
            timeout=100,
        )

        st.write(pd.read_json(res.json()))
