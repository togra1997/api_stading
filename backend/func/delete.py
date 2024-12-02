"""delete index."""

import json

import ibis

ibis.set_backend("polars")


def delete_data(delet_id: str) -> json:
    """データ削除.

    Returns:
        _type_: _description_

    """
    table = ibis.read_csv("records.csv")

    table = table.filter(table["id"] != int(delet_id))

    outpt_df = table.execute()
    outpt_df["id"] = outpt_df.reset_index(drop=True).index
    output_table = ibis.memtable(outpt_df)

    output_table.to_csv("./records.csv")

    return output_table.execute().to_json()
