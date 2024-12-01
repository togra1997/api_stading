"""registar data function."""

import datetime
from dataclasses import asdict

import ibis
import pandas as pd

ibis.set_backend("polars")


def registar_data(data):
    today = str(datetime.datetime.today().date())

    df = pd.DataFrame(asdict(data), index=[0])

    table = ibis.memtable(df).mutate(
        経過時間=(
            datetime.datetime.strptime(today + data.end_time, "%Y-%m-%d%H:%M")
            - datetime.datetime.strptime(today + data.start_time, "%Y-%m-%d%H:%M")
        ).total_seconds(),
        date=today,
    )

    read_table = ibis.read_csv("./records.csv")

    output_table = ibis.memtable(pd.concat([table.execute(), read_table.execute()]))
    output_table.to_csv("./records.csv")

    return output_table.execute().to_json()
