import streamlit as st
from aip_cliant.api_cliant import ApiCliant


class WorkTimeUi:
    def __init__(self, url: str) -> None:
        self.url = url

    def registar_work_time(self) -> None:
        """工数データを登録するための関数.

        固定の工数データをAPIに送信して登録します。
        """
        cliant = ApiCliant(self.url)

        data = {
            "start": "string",
            "end": "string",
            "task": "string",
            "effort_assignmen": "string",
        }

        if st.button("登録", key="registar_work_time"):
            res = cliant.post(data)
            st.write(res)

    def delete_work_time(self) -> None:
        """工数データを登録するための関数.

        固定の工数データをAPIに送信して登録します。
        """
        cliant = ApiCliant(self.url)

        target_id = st.text_input("削除対象の工数ID", key="delete_work_time_txt")
        if st.button("削除", key="delete_work_time"):
            res = cliant.delete(target_id=target_id)
            st.write(res)
