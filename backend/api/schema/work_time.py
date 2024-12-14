"""工数管理のためのモデルを定義します.

このモジュールには、工数データの取得と追加を行うためのPydanticモデルが含まれています。
"""

import ibis
import pandas as pd
from pydantic import BaseModel


class BaseWorkTime(BaseModel):
    """基本的な工数管理のクラスを定義します."""

    date: str  # 工数の日付
    start: str  # 作業開始時刻
    end: str  # 作業終了時刻
    task: str  # タスク名
    effort_assignmen: str  # 工数付け先


class GetWorkTime(BaseWorkTime):
    """工数を取得するためのモデルを定義します."""

    id: int  # 工数のID


class AddWorkTime(BaseWorkTime):
    """工数を追加するためのモデルを定義します."""

    def make_worktimedata(self) -> ibis.Table:
        """工数データを作成します.

        Returns:
            ibis.Table: 作成された工数データのテーブル。

        """
        return_df = pd.DataFrame(
            {
                "date": f"{self.date}",
                "start": f"{self.start}",
                "end": f"{self.end}",
                "task": f"{self.task}",
                "effort_assignmen": f"{self.effort_assignmen}",
            },
            index=[0],
        )
        return ibis.memtable(return_df)


if __name__ == "__main__":
    import ibis

    ibis.set_backend("polars")
    table = ibis.read_csv("api/datas/worktimedata.csv")
    work_time_data = table.execute().to_dict(orient="records")
    test = [GetWorkTime(**work_data) for work_data in work_time_data]
    print(test)
