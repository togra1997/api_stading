import streamlit as st
from ui import task, work_time

task_ui = task.TaskUi(url="http://localhost:8000/tasks")
work_time_ui = work_time.WorkTimeUi(url="http://localhost:8000/work-time")


tabs = st.tabs(["工数", "タスク"])

with tabs[0]:
    work_time_ui.registar_work_time()
    work_time_ui.delete_work_time()
    work_time_ui.get_work_time()

with tabs[1]:
    task_ui.registar_task()
    task_ui.delete_task()
    task_ui.update_task()
    task_ui.get_task()
st.stop()
