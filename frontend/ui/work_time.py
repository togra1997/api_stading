"""このモジュールは、工数データを登録、削除、および取得するためのStreamlitアプリケーションのUIクラスを提供します.

クラス:
    WorkTimeUi: 工数データを管理するためのUIクラス。

メソッド:
    WorkTimeUi.registar_work_time: 工数データを登録するためのメソッド。
    WorkTimeUi.delete_work_time: 工数データを削除するためのメソッド。
    WorkTimeUi.get_work_time: 工数データを取得するためのメソッド。
"""

from datetime import time

import pandas as pd
import streamlit as st
from aip_cliant.api_cliant import ApiCliant


class WorkTimeUi:
    """工数データを管理するためのUIクラス."""

    def __init__(self, url: str) -> None:
        """WorkTimeUiのコンストラクタ.

        Args:
            url (str): APIのベースURL。

        """
        self.url = url
        self.cliant = ApiCliant(self.url)

    def registar_work_time(self) -> None:
        """工数データを登録するための関数.

        固定の工数データをAPIに送信して登録します。
        """
        with st.expander("工数登録"):
            columns = st.columns(2)

            with columns[0]:
                start: time = st.time_input("開始時間", key="start_time")

            with columns[1]:
                end: time = st.time_input("終了時間", key="end_time")

            task_name = st.text_input("タスク名", key="task_name_list")
            effort_assignmen = st.text_input("工数", key="effort_assignmen")

            data = {
                "start": f"{start}",
                "end": f"{end}",
                "task": f"{task_name}",
                "effort_assignmen": f"{effort_assignmen}",
            }

            if st.button("登録", key="registar_work_time"):
                res = self.cliant.post(data)

                st.write("登録に成功しました")

    def delete_work_time(self) -> None:
        """工数データを登録するための関数.

        固定の工数データをAPIに送信して登録します。
        """
        with st.expander("工数削除"):
            target_id = st.text_input("削除対象の工数ID", key="delete_work_time_txt")
            if st.button("削除", key="delete_work_time"):
                res = self.cliant.delete(target_id=target_id)

                st.write("削除に成功しました")

    def get_work_time(self) -> None:
        """工数データを取得するための関数.

        APIから工数データを取得して表示します。
        """
        res = self.cliant.get()
        return_df = pd.DataFrame()
        for data in res:
            tmp_df = pd.DataFrame(data, index=[0])
            return_df = pd.concat([return_df, tmp_df], axis=0, ignore_index=True)

        st.write(return_df)
