from typing import Annotated

import ibis
from api.dependency.managemant_csv import ManagedWorkTimeCsv
from fastapi import APIRouter, Depends

router = APIRouter()
ibis.set_backend("pandas")


@router.get("")
def calc_work_time(
    work_time_data_manager: Annotated[ManagedWorkTimeCsv, Depends(ManagedWorkTimeCsv)],
):
    """すべての工数データを取得します.

    パラメータ:
    - work_time_data_manager: CSVデータを管理するための依存関係インスタンス。

    戻り値:
    - List[work_time.GetWorkTime]: 取得した工数データのリスト。
    """
    table = work_time_data_manager.read_csv_data()

    table = table.mutate(
        start_time=table["start"].cast("timestamp"),
        end_time=table["end"].cast("timestamp"),
    )
    table = table.mutate(work_time=table["end_time"] - table["start_time"])
    print(table.execute())

    # return calculation.Calc(data=data[0])
