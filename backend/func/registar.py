"""registar data function."""

import datetime
import json
from dataclasses import asdict

import ibis
import pandas as pd
from datas import RegistarData

ibis.set_backend("pandas")


def registar_data(data: RegistarData) -> json:
    """Registar to csv.

    Args:
        data (RegistarData): _description_

    Returns:
        json: _description_

    """
    today = str(datetime.datetime.now(tz=datetime.UTC).date())

    input_df = pd.DataFrame(asdict(data), index=[0])
    input_df["日付"] = today
    input_df = input_df.rename(
        columns={
            "start_time": "開始時刻",
            "end_time": "終了時刻",
            "annkenn": "案件",
            "kousuutukesaki": "工数付け先",
            "work": "作業内容",
        },
    )
    table = ibis.memtable(input_df)
    table2 = table.mutate(
        経過時間=(
            datetime.datetime.strptime(
                today + data.end_time,
                "%Y-%m-%d%H:%M:%S",
            ).replace(
                tzinfo=datetime.UTC,
            )
            - datetime.datetime.strptime(
                today + data.start_time,
                "%Y-%m-%d%H:%M:%S",
            ).replace(tzinfo=datetime.UTC)
        ).total_seconds(),
    )

    read_table = ibis.read_csv("./records.csv")

    concat_table = ibis.memtable(
        pd.concat([table2.execute(), read_table.execute()]).reset_index(drop=True),
    )

    df_output = concat_table.execute()
    df_output["id"] = df_output.index
    concat_table = ibis.memtable(df_output)

    concat_table.to_csv("./records.csv")

    return_table = concat_table.filter(concat_table["日付"] == today)
    return return_table.execute().to_json()
