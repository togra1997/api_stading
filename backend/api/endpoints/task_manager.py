"""タスク管理APIのエンドポイントを定義します。

エンドポイント:
- GET /tasks: すべてのタスクを取得します。
- POST /tasks: 新しいタスクを追加します。
- DELETE /tasks: タスクを削除します。
"""

import ibis
import pandas as pd
from api.dependency.managemant_csv import ManagedTaskCsv
from api.schema import task
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[task.GetTask])
def get_tasks(task_csv: ManagedTaskCsv = Depends(ManagedTaskCsv)) -> list[task.GetTask]:
    """すべてのタスクを取得します。"""
    task_data = task_csv.read_csv_data().execute().to_dict(orient="records")
    return [task.GetTask(**t) for t in task_data]


@router.post("", response_model=list[task.GetTask])
def add_task(
    task_data: task.AddTask,
    task_csv: ManagedTaskCsv = Depends(ManagedTaskCsv),
) -> list[task.GetTask]:
    """新しいタスクを追加します。"""
    task_table = task_data.make_taskdata()

    return_df = pd.concat([task_csv.read_csv_data().execute(), task_table.execute()])
    return_df["id"] = return_df.reset_index(drop=True).index
    task_csv.save_csv_data(ibis.memtable(return_df))

    return [task.GetTask(**t) for t in return_df.to_dict(orient="records")]


@router.delete("/{target_id}")
def delete_task(target_id: str, task_csv: ManagedTaskCsv = Depends(ManagedTaskCsv)):
    """タスクを削除します。"""
    task_table = task_csv.read_csv_data()
    df = task_table.filter(task_table["id"] != int(target_id)).execute()
    df["id"] = df.reset_index(drop=True).index
    task_csv.save_csv_data(ibis.memtable(df))

    return [task.GetTask(**t) for t in df.to_dict(orient="records")]
