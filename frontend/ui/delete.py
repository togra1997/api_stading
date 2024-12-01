"""削除UI."""

from io import StringIO

import pandas as pd
import requests
import streamlit as st


def delete_ui() -> None:
    """削除UI."""
    id = st.text_input("削除するID")
    url = "http://127.0.0.1:8000"
    if st.button("削除"):
        res = requests.delete(
            url=f"{url}/{id}",
            timeout=100,
        )
        st.write(pd.read_json(StringIO(res.json())))
    # res = requests.get(url=url, timeout=100)
