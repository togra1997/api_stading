"""get data."""

import datetime
import json

import ibis

ibis.set_backend("polars")


def get_data() -> json:
    """当日のデータ取得.

    Returns:
        json: _description_

    """
    today = str(datetime.datetime.now(tz=datetime.UTC).date())
    table = ibis.read_csv("./records.csv")

    return_table = table.filter(table["日付"] == today)

    return return_table.execute().to_json()
