"""工数管理APIのエンドポイントを定義します.

エンドポイント:
- GET /work_time: すべての工数データを取得します。
- POST /work_time: 新しい工数データを追加します。
- DELETE /work_time/{target_id}: 指定されたIDの工数データを削除します。
"""

from typing import Annotated

import ibis
import pandas as pd
from api.dependency.managemant_csv import ManagedEffortAssignmentCsv
from api.schema import effort_assignment
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("", response_model=effort_assignment.GetAllEffortAssingment)
def get_effort_assignment(
    work_time_data_manager: Annotated[
        ManagedEffortAssignmentCsv,
        Depends(ManagedEffortAssignmentCsv),
    ],
) -> effort_assignment.GetAllEffortAssingment:
    work_time_data = (
        work_time_data_manager.read_csv_data().execute().to_dict(orient="records")
    )
    return effort_assignment.GetAllEffortAssingment(
        data=[
            effort_assignment.GetEffortAssingment(**work_data)
            for work_data in work_time_data
        ],
    )


@router.post("", response_model=effort_assignment.GetAllEffortAssingment)
def add_effort_assignment(
    work_time_data: effort_assignment.AddEffortAssingment,
    work_time_data_manager: Annotated[
        ManagedEffortAssignmentCsv,
        Depends(ManagedEffortAssignmentCsv),
    ],
) -> effort_assignment.GetAllEffortAssingment:
    work_time_table = work_time_data.make_effort_assignment_data()

    return_df = pd.concat(
        [work_time_data_manager.read_csv_data().execute(), work_time_table.execute()],
    )
    return_df["id"] = return_df.reset_index(drop=True).index
    work_time_data_manager.save_csv_data(ibis.memtable(return_df))

    return effort_assignment.GetAllEffortAssingment(
        data=[
            effort_assignment.GetEffortAssingment(**work_data)
            for work_data in return_df.to_dict(orient="records")
        ],
    )


@router.delete(
    "/{target_id}",
    response_model=effort_assignment.GetAllEffortAssingment,
)
def delete_effort_assignment(
    target_id: str,
    work_time_data_manager: Annotated[
        ManagedEffortAssignmentCsv,
        Depends(ManagedEffortAssignmentCsv),
    ],
) -> effort_assignment.GetAllEffortAssingment:
    work_time_data = work_time_data_manager.read_csv_data()
    return_df = work_time_data.filter(
        work_time_data["id"] != int(target_id),
    ).execute()

    return_df["id"] = return_df.reset_index(drop=True).index
    work_time_data_manager.save_csv_data(ibis.memtable(return_df))
    return effort_assignment.GetAllEffortAssingment(
        data=[
            effort_assignment.GetEffortAssingment(**work_data)
            for work_data in return_df.to_dict(orient="records")
        ],
    )
