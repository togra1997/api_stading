from ui import task, work_time

task_ui = task.TaskUi("http://localhost:8000/tasks")
work_time_ui = work_time.WorkTimeUi("http://localhost:8000/work-time")

task_ui.registar_task()

work_time_ui.registar_work_time()
work_time_ui.delete_work_time()
