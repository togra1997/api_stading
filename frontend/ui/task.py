import streamlit as st
from aip_cliant.api_cliant import ApiCliant


class TaskUi:
    def __init__(self, url: str) -> None:
        self.url = url

    def registar_task(self) -> None:
        """タスクを登録するための関数.

        ユーザーが入力したタスク名をAPIに送信して登録します。
        """
        cliant = ApiCliant(self.url)

        task_name = st.text_input("タスク名")

        if st.button("登録", key="registar_task"):
            data = {"name": task_name}
            res = cliant.post(data)
            st.write(res)
