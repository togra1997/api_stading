"""_summary_."""

import ibis

ibis.set_backend("polars")


def calc_total(target_month: str):
    table = ibis.read_csv("records.csv")
    table = table.mutate(
        year=table["日付"].cast("date").year(),
        month=table["日付"].cast("date").month(),
    )
    date = target_month.split("-")
    table = table.filter(
        [
            table["year"] == int(date[0]),
            table["month"] == int(date[1]),
        ],
    )
    table = table.drop("year", "month")
    output_table = table.group_by(["工数付け先", "案件"]).aggregate(
        今月の合計時間=(table["経過時間"].sum()) / 3600,
    )
    return output_table.order_by(["工数付け先", "案件"]).execute().to_json()
