"""タスク管理APIのエンドポイントを定義します.

エンドポイント:
- GET /tasks: すべてのタスクを取得します。
- POST /tasks: 新しいタスクを追加します。
- DELETE /tasks: タスクを削除します。
"""

from typing import Annotated

import ibis
import pandas as pd
from api.dependency.managemant_csv import ManagedTaskCsv
from api.schema import task
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[task.GetTask])
def get_tasks(
    task_data_manager: Annotated[ManagedTaskCsv, Depends(ManagedTaskCsv)],
) -> list[task.GetTask]:
    """新しいタスクを追加します.

    パラメータ:
    - task_data: 追加するタスクのデータ。
    - task_csv: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[task.GetTask]: 追加後のタスクのリスト。
    """
    task_data = task_data_manager.read_csv_data().execute().to_dict(orient="records")
    return [task.GetTask(**t) for t in task_data]


@router.post("", response_model=list[task.GetTask])
def add_task(
    task_data: task.AddTask,
    task_data_manager: Annotated[ManagedTaskCsv, Depends(ManagedTaskCsv)],
) -> list[task.GetTask]:
    """新しいタスクを追加します.

    パラメータ:
    - task_data: 追加するタスクのデータ。
    - task_csv: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[task.GetTask]: 追加後のタスクのリスト。
    """
    task_table = task_data.make_taskdata()

    return_df = pd.concat(
        [task_data_manager.read_csv_data().execute(), task_table.execute()],
    )
    return_df["id"] = return_df.reset_index(drop=True).index
    task_data_manager.save_csv_data(ibis.memtable(return_df))

    return [task.GetTask(**t) for t in return_df.to_dict(orient="records")]


@router.delete("/{target_id}")
def delete_task(
    target_id: str,
    task_data_manager: Annotated[ManagedTaskCsv, Depends(ManagedTaskCsv)],
) -> list[task.GetTask]:
    """指定されたIDのタスクを削除します.

    パラメータ:
    - target_id: 削除対象のタスクID。
    - task_csv: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[task.GetTask]: 削除後のタスクのリスト。
    """
    task_table = task_data_manager.read_csv_data()
    return_df = task_table.filter(task_table["id"] != int(target_id)).execute()
    return_df["id"] = return_df.reset_index(drop=True).index
    task_data_manager.save_csv_data(ibis.memtable(return_df))

    return [task.GetTask(**t) for t in return_df.to_dict(orient="records")]
