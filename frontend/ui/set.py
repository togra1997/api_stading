from io import StringIO

import pandas as pd
import requests
import streamlit as st


def setting():
    with st.expander("test"):
        url = "http://127.0.0.1:8000/task"
        res = requests.get(
            url=f"{url}",
            timeout=100,
        )
        st.write(pd.read_json(StringIO(res.json())))
