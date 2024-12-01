"""delete index."""

import ibis

ibis.set_backend("polars")


def delete_data(id):
    table = ibis.read_csv("records.csv")

    table = table.filter(table["id"] != int(id))
    # table.to_csv("records.csv")

    return table.execute().to_json()
