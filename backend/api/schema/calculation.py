"""このモジュールは、タスク管理のためのPydanticモデルを定義します.

クラス:
- BaseTask: 基本的なタスクモデルを定義します。
- AddTask: タスクを追加するためのモデルを定義します。
- UpdateTask: タスクを更新するためのモデルを定義します。
- DeleteTask: タスクを削除するためのモデルを定義します。
- GetTask: タスクを取得するためのモデルを定義します。
"""

import ibis
from pydantic import BaseModel

ibis.set_backend("polars")


class Calc(BaseModel):
    """基本的な集計モデルを定義します."""

    data: list
