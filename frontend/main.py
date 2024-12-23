"""このモジュールは、Streamlitアプリケーションのメインエントリーポイントを提供します.

関数:
    display_sidebar() -> str:
        サイドバーの設定を行い、選択されたタブを返す関数。

    display_worktime_management() -> None:
        工数管理タブの表示を行う関数。

    display_worktime_calculation() -> None:
        工数集計タブの表示を行う関数。

    display_task_management() -> None:
        タスク管理タブの表示を行う関数。

    display_settings() -> None:
        設定タブの表示を行う関数。

    main() -> None:
        メイン関数。
"""

import streamlit as st
from ui import effort_assignment, task, wroktime, wroktime_calucration


def display_sidebar() -> str:
    """サイドバーの設定を行い、選択されたタブを返す関数."""
    with st.sidebar:
        st.header("UI設定 :gear:")
        selected_tab = st.radio(
            "表示するタブを選択",
            (
                "工数管理 :clipboard:",
                "工数集計 :bar_chart:",
                "タスク管理 :memo:",
                "設定 :gear:",
            ),
        )
    return selected_tab


def display_worktime_management() -> None:
    """工数管理タブの表示を行う関数."""
    st.title("工数管理 :clipboard:")
    tabs = st.tabs(["登録 :inbox_tray:", "削除 :outbox_tray:"])
    with tabs[0]:
        wroktime.registar_worktime()
    with tabs[1]:
        wroktime.delete_worktime()


def display_worktime_calculation() -> None:
    """工数集計タブの表示を行う関数."""
    st.title("工数集計 :bar_chart:")
    wroktime_calucration.calc_worktime()


def display_task_management() -> None:
    """タスク管理タブの表示を行う関数."""
    st.title("タスク管理 :memo:")
    tabs = st.tabs(["登録 :inbox_tray:", "更新 :pencil:", "削除 :outbox_tray:"])
    with tabs[0]:
        task.regist_task()
    with tabs[1]:
        task.update_task()
    with tabs[2]:
        task.delete_task()


def display_settings() -> None:
    """設定タブの表示を行う関数."""
    st.title("設定 :gear:")
    tabs = st.tabs(["工数登録 :inbox_tray:", "削除 :outbox_tray:"])
    with tabs[0]:
        effort_assignment.registr()
    with tabs[1]:
        effort_assignment.delete()


def main() -> None:
    """メイン関数."""
    selected_tab = display_sidebar()

    if "工数管理" in selected_tab:
        display_worktime_management()
    elif "工数集計" in selected_tab:
        display_worktime_calculation()
    elif "タスク管理" in selected_tab:
        display_task_management()
    elif "設定" in selected_tab:
        display_settings()

    st.stop()


if __name__ == "__main__":
    main()
