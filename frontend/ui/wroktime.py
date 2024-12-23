"""このモジュールは、作業時間の登録と表示を行うための関数を提供します.

関数:
    fetch_data(client: ApiCliant) -> list[dict[str, Any]]:
        APIからデータを取得する関数。

    display_selectbox(label: str, data_list: list[dict[str, Any]]) -> str:
        選択ボックスを表示する関数。

    registar_worktime() -> None:
        登録タブの内容を表示する関数。

    delete_worktime() -> None:
        削除タブの内容を表示する関数。
"""

from typing import Any

import streamlit as st
from aip_cliant.api_cliant import ApiCliant

cliant = ApiCliant(url="http://localhost:8000/work-time")


def fetch_data(client: ApiCliant) -> list[dict[str, Any]]:
    """APIからデータを取得する関数.

    Args:
        client (ApiCliant): APIクライアントインスタンス
        endpoint (str): APIのエンドポイント

    Returns:
        List[Dict[str, Any]]: 取得したデータのリスト

    """
    res = client.get()
    if res.status_code == 200:
        return res.json()["data"]
    return []


def display_selectbox(label: str, data_list: list[dict[str, Any]]) -> str:
    """選択ボックスを表示する関数.

    Args:
        label (str): 選択ボックスのラベル
        data_list (List[Dict[str, Any]]): 選択肢のデータリスト

    Returns:
        str: 選択された値

    """
    return st.selectbox(label, [d["name"] for d in data_list])


def registar_worktime() -> None:
    """登録タブの内容を表示する関数.

    Returns:
        None

    """
    st.header("登録 :memo:")
    col1, col2 = st.columns(2)
    with col1:
        start = st.time_input("開始時刻を入力:")
    with col2:
        end = st.time_input("終了時刻を入力:")

    effort_assignment_client = ApiCliant(url="http://localhost:8000/effort-assignment")
    effort_assignment_list = fetch_data(effort_assignment_client)
    effort_assignment = display_selectbox("工数付け先選択:", effort_assignment_list)

    task_client = ApiCliant(url="http://localhost:8000/tasks")
    task_list = fetch_data(task_client)
    task = display_selectbox("タスクを選択:", task_list)

    if st.button("登録"):
        data = {
            "start": f"{start}",
            "end": f"{end}",
            "task": f"{task}",
            "effort_assignment": f"{effort_assignment}",
        }
        res = cliant.post(data=data)
        if res.status_code == 200:
            st.success("登録しました！")

    res1 = cliant.get()
    if res1.status_code == 200:
        data = res1.json()
        st.table(data["data"])


def delete_worktime() -> None:
    """削除タブの内容を表示する関数.

    Returns:
        None

    """
    st.header("削除 :memo:")
    target_id = st.text_input("削除するID:")
    if st.button("削除"):
        res = cliant.delete(target_id=target_id)
        if res.status_code == 200:
            st.success("削除しました！")

    res1 = cliant.get()
    if res1.status_code == 200:
        data = res1.json()
        st.table(data["data"])
