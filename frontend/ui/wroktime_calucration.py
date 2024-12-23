"""このモジュールは、作業時間の計算と表示を行うための関数を提供します.

関数:
    fetch_data(client: ApiCliant) -> list[dict[str, Any]]:
        APIからデータを取得する関数。

    preprocess_data(data: list[dict[str, Any]]) -> pd.DataFrame:
        データの前処理を行う関数。

    calc_worktime() -> None:
        作業時間を計算して表示する関数。
"""

import re
from typing import Any

import pandas as pd
import streamlit as st
from aip_cliant.api_cliant import ApiCliant


def fetch_data(client: ApiCliant) -> list[dict[str, Any]]:
    """APIからデータを取得する関数.

    Args:
        client (ApiCliant): APIクライアントインスタンス

    Returns:
        List[Dict[str, Any]]: 取得したデータのリスト

    """
    res = client.get()
    if res.status_code == 200:
        return res.json()["data"]
    return []


def preprocess_data(data: list[dict[str, Any]]) -> pd.DataFrame:
    """データの前処理を行う関数.

    Args:
        data (List[Dict[str, Any]]): 前処理するデータのリスト

    Returns:
        pd.DataFrame: 前処理されたデータフレーム

    """
    pattern = re.compile(r"^\d{4}-\d{2}")
    df = pd.DataFrame(data)
    df["date_month"] = df["date"].apply(lambda x: re.match(pattern, x).group(0))
    df["start_time"] = pd.to_datetime(df["start"])
    df["end_time"] = pd.to_datetime(df["end"])
    df["work_time"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 3600
    return df


def calc_worktime() -> None:
    """作業時間を計算して表示する関数.

    Returns:
        None

    """
    st.header("登録 :memo:")
    select = st.multiselect(
        "集計する項目を選択してください",
        ["task", "effort_assignment"],
        default=["task"],
    )
    api_client = ApiCliant(url="http://localhost:8000/work-time")
    data = fetch_data(api_client)
    if data:
        df = preprocess_data(data)
        target_month_list = sorted(df["date_month"].unique())
        target_month = st.multiselect(
            "集計年月",
            target_month_list,
            default=target_month_list[0],
        )

        # 集計対象の月のみ抽出
        df = df[df["date_month"].isin(target_month)][[*select, "work_time"]]
        df = df.groupby(select).sum().reset_index()

        st.write(df)
