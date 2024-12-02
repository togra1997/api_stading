import datetime
from io import StringIO

import pandas as pd
import requests
import streamlit as st


def totaling_ui():
    url = "http://127.0.0.1:8000"
    res = requests.get(url=f"{url}/all", timeout=100)

    list_df = pd.read_json(StringIO(res.json()))
    list_df["日付"] = list_df["日付"].apply(
        lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").replace(
            tzinfo=datetime.UTC,
        ),
    )
    list_df["年月"] = pd.to_datetime(list_df["日付"]).dt.strftime("%Y-%m")

    input_list = list_df["年月"].unique().tolist()

    target_month = st.selectbox(label="集計対象月", options=input_list)
    res1 = requests.get(url=f"{url}/{target_month}", timeout=100)

    st.write(pd.read_json(StringIO(res1.json())))
