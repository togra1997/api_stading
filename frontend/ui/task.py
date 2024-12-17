import pandas as pd
import streamlit as st
from aip_cliant.api_cliant import ApiCliant


class TaskUi:
    """工数データを管理するためのUIクラス."""

    def __init__(self, url: str) -> None:
        """WorkTimeUiのコンストラクタ.

        Args:
            url (str): APIのベースURL。

        """
        self.url = url
        self.cliant = ApiCliant(self.url)

    def registar_task(self) -> None:
        with st.expander("タスク登録"):
            name = st.text_input("タスク名", key="task_name")
            data = {
                "name": f"{name}",
            }

            if st.button("登録", key="registar_task"):
                res = self.cliant.post(data)

                st.write("登録に成功しました")

    def delete_task(self) -> None:
        with st.expander("タスク削除"):
            target_id = st.text_input("削除対象のタスクID", key="delete_task_id")
            if st.button("削除", key="delete_task"):
                res = self.cliant.delete(target_id=target_id)

                st.write("削除に成功しました")

    def update_task(self) -> None:
        with st.expander("タスク更新"):
            target_id = st.text_input("更新対象のタスクID", key="update_task_id")

            update_data = st.selectbox(
                "ステータス",
                options=[True, False],
                key="update_task_complete",
            )

            if st.button("更新", key="update_task"):
                data = {
                    "name": "",
                    "completed": update_data,
                }
                res = self.cliant.put(target_id=target_id, data=data)

                st.write("更新に成功しました")

    def get_task(self) -> None:
        res = self.cliant.get()
        return_df = pd.DataFrame()
        for data in res:
            tmp_df = pd.DataFrame(data, index=[0])
            return_df = pd.concat([return_df, tmp_df], axis=0, ignore_index=True)

        st.write(return_df)
