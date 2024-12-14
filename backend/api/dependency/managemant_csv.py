"""このモジュールは、Polarsバックエンドを使用してCSVデータを管理するためのクラスを提供します.

クラス:
- ManagedCsv: CSVデータを読み込むためのメソッドを提供します.
"""

import ibis

# Polarsバックエンドを設定
ibis.set_backend("polars")


class ManagedTaskCsv:
    """CSVデータを管理するためのクラスです.

    メソッド:
    - read_csv_data: CSVデータを読み込みます.
    """

    def read_csv_data(self) -> ibis.Table:
        """CSVデータを読み込みます."""
        return ibis.read_csv("api/datas/taskdata.csv")

    def save_csv_data(self, table: ibis.Table) -> None:
        """CSVデータを読み込みます."""
        table.to_csv("api/datas/taskdata.csv")
