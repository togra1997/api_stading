"""このモジュールは、工数割り当ての登録、削除、および表示を行うための関数を提供します.

関数:
    fetch_and_display_data() -> None:
        APIからデータを取得し、テーブル形式で表示する関数。

    registr() -> None:
        工数割り当てを登録するフォームを表示し、登録処理を行う関数。

    delete() -> None:
        工数割り当てを削除するフォームを表示し、削除処理を行う関数。
"""

import streamlit as st
from aip_cliant.api_cliant import ApiCliant

api_cliant = ApiCliant(url="http://localhost:8000/effort-assignment")


def fetch_and_display_data() -> None:
    """APIからデータを取得し、テーブル形式で表示する関数.

    Returns:
        None

    """
    res = api_cliant.get()
    if res.status_code == 200:
        data = res.json()
        st.table(data["data"])


def registr() -> None:
    """工数割り当てを登録するフォームを表示し、登録処理を行う関数.

    Returns:
        None

    """
    st.title("タスクフォーム")

    name = st.text_input("タスク名", key="registar_task_name")

    if st.button("送信", key="registar_task_button"):
        data = {"name": name}

        res = api_cliant.post(data=data)
        if res.status_code == 200:
            st.success("登録しました！")

    fetch_and_display_data()


def delete() -> None:
    """工数割り当てを削除するフォームを表示し、削除処理を行う関数.

    Returns:
        None

    """
    st.title("タスクフォーム")

    target_id = st.text_input("削除するID", key="delete_target_id")

    if st.button("送信", key="delete_task_button"):
        res = api_cliant.delete(target_id=target_id)
        if res.status_code == 200:
            st.success("削除しました！")

    fetch_and_display_data()
