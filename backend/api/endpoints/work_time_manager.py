"""工数管理APIのエンドポイントを定義します.

エンドポイント:
- GET /work_time: すべての工数データを取得します。
- POST /work_time: 新しい工数データを追加します。
- DELETE /work_time/{target_id}: 指定されたIDの工数データを削除します。
"""

from typing import Annotated

import ibis
import pandas as pd
from api.dependency.managemant_csv import ManagedWorkTimeCsv
from api.schema import work_time
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=list[work_time.GetWorkTime])
def get_work_time(
    work_time_data_manager: Annotated[ManagedWorkTimeCsv, Depends(ManagedWorkTimeCsv)],
) -> list[work_time.GetWorkTime]:
    """すべての工数データを取得します.

    パラメータ:
    - work_time_data_manager: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[work_time.GetWorkTime]: 取得した工数データのリスト。
    """
    work_time_data = (
        work_time_data_manager.read_csv_data().execute().to_dict(orient="records")
    )
    return [work_time.GetWorkTime(**work_data) for work_data in work_time_data]


@router.post("", response_model=list[work_time.GetWorkTime])
def add_work_time(
    work_time_data: work_time.AddWorkTime,
    work_time_data_manager: Annotated[ManagedWorkTimeCsv, Depends(ManagedWorkTimeCsv)],
) -> list[work_time.GetWorkTime]:
    """新しい工数データを追加します.

    パラメータ:
    - work_time_data: 追加する工数データのモデル。
    - work_time_data_manager: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[work_time.GetWorkTime]: 追加後の工数データのリスト。
    """
    work_time_table = work_time_data.make_worktimedata()

    return_df = pd.concat(
        [work_time_data_manager.read_csv_data().execute(), work_time_table.execute()],
    )
    return_df["id"] = return_df.reset_index(drop=True).index
    work_time_data_manager.save_csv_data(ibis.memtable(return_df))

    return [
        work_time.GetWorkTime(**work_data)
        for work_data in return_df.to_dict(orient="records")
    ]


@router.delete("/{target_id}", response_model=list[work_time.GetWorkTime])
def delete_work_time(
    target_id: str,
    work_time_data_manager: Annotated[ManagedWorkTimeCsv, Depends(ManagedWorkTimeCsv)],
) -> list[work_time.GetWorkTime]:
    """指定されたIDの工数データを削除します.

    パラメータ:
    - target_id: 削除対象の工数データのID。
    - work_time_data_manager: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[work_time.GetWorkTime]: 削除後の工数データのリスト。
    """
    work_time_data = work_time_data_manager.read_csv_data()
    return_df = work_time_data.filter(
        work_time_data["id"] != int(target_id),
    ).execute()

    return_df["id"] = return_df.reset_index(drop=True).index
    work_time_data_manager.save_csv_data(ibis.memtable(return_df))
    return [
        work_time.GetWorkTime(**work_data)
        for work_data in return_df.to_dict(orient="records")
    ]
