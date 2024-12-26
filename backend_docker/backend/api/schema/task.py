"""このモジュールは、タスク管理のためのPydanticモデルを定義します.

クラス:
- BaseTask: 基本的なタスクモデルを定義します。
- AddTask: タスクを追加するためのモデルを定義します。
- UpdateTask: タスクを更新するためのモデルを定義します。
- DeleteTask: タスクを削除するためのモデルを定義します。
- GetTask: タスクを取得するためのモデルを定義します。
"""

import ibis
import pandas as pd
from pydantic import BaseModel

ibis.set_backend("polars")


class BaseTask(BaseModel):
    """基本的なタスクモデルを定義します."""

    name: str


class AddTask(BaseTask):
    """タスクを追加するためのモデルを定義します."""

    def make_taskdata(self) -> ibis.Table:
        """タスクデータを作成し、完了フラグを設定します.

        Returns:
            ibis.Table: 作成されたタスクデータのテーブル。

        """
        completed = False
        return_df = pd.DataFrame({"name": [self.name], "completed": [completed]})
        return ibis.memtable(return_df)


class GetTask(BaseTask):
    """タスクを取得するためのモデルを定義します."""

    id: int
    completed: bool


class GetAllTask(BaseModel):
    """全てのタスクを取得するためのモデルを定義します."""

    data: list[GetTask]


class UpdateTask(BaseTask):
    """タスクを更新するためのモデルを定義します."""

    completed: bool
