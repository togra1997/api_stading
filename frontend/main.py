"""front end ui."""

import json

import pandas as pd
import requests
import streamlit as st

if st.button("post"):
    url = "http://127.0.0.1:8000"

    res = requests.post(
        url=url,
        data=json.dumps(
            {
                "start_time": "10:30",
                "end_time": "11:00",
                "annkenn": "d",
                "work": "e",
                "kousuutukesaki": "f",
            },
        ),
        timeout=100,
    )
    st.write(pd.read_json(res.json()))
