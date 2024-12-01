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

    df_input = pd.DataFrame(asdict(data), index=[0])
    df_input["日付"] = today
    table = ibis.memtable(df_input)
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
