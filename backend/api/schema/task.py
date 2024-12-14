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
    completed: bool


class AddTask(BaseTask):
    """タスクを追加するためのモデルを定義します."""

    def make_taskdata(self) -> ibis.Table:
        self.completed = False
        df = pd.DataFrame({"name": [self.name], "completed": [self.completed]})
        return ibis.memtable(df)


class GetTask(BaseTask):
    """タスクを取得するためのモデルを定義します."""

    id: int
