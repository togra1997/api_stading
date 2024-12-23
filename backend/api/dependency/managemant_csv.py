"""このモジュールは、Polarsバックエンドを使用してCSVデータを管理するためのクラスを提供します.

クラス:
- ManagedCsv: CSVデータを読み込むためのメソッドを提供します.
"""

import ibis

# Polarsバックエンドを設定
ibis.set_backend("polars")


class ManagedTaskCsv:
    """CSVデータを管理するためのクラスです.

    このクラスは、タスクデータを含むCSVファイルの読み込みと書き込みを管理���ます。
    Polarsバックエンドを使用して効率的にデータを処理します。

    メソッド:
    - read_csv_data: CSVデータを読み込みます。
    - save_csv_data: CSVデータを書き込みます。
    """

    target_csv = "api/datas/taskdata.csv"

    def read_csv_data(self) -> ibis.Table:
        """CSVデータを読み込みます.

        指定されたCSVファイルからタスクデータを読み込み、ibis.Tableオブジェクトとして返します。

        戻り値:
            ibis.Table: 読み込まれたタスクデータを含むテーブルオブジェクト。
        """
        return ibis.read_csv(self.target_csv)

    def save_csv_data(self, table: ibis.Table) -> None:
        """CSVデータを書き込みます.

        受け取ったibis.Tableオブジェクトのデータを指定されたCSVファイルに保存します。

        パラメータ:
            table (ibis.Table): 保存するタスクデータのテーブル。

        戻り値:
            None
        """
        table.to_csv(self.target_csv)


class ManagedWorkTimeCsv:
    """CSVデータを管理するためのクラスです.

    このクラスは、タスクデータを含むCSVファイルの読み込みと書き込みを管理���ます。
    Polarsバックエンドを使用して効率的にデータを処理します。

    メソッド:
    - read_csv_data: CSVデータを読み込みます。
    - save_csv_data: CSVデータを書き込みます。
    """

    target_csv = "api/datas/worktimedata.csv"

    def read_csv_data(self) -> ibis.Table:
        """CSVデータを読み込みます.

        指定されたCSVファイルからタスクデータを読み込み、ibis.Tableオブジェクトとして返します。

        戻り値:
            ibis.Table: 読み込まれたタスクデータを含むテーブルオブジェクト。
        """
        return ibis.read_csv(self.target_csv)

    def save_csv_data(self, table: ibis.Table) -> None:
        """CSVデータを書き込みます.

        受け取ったibis.Tableオブジェクトのデータを指定されたCSVファイルに保存します。

        パラメータ:
            table (ibis.Table): 保存するタスクデータのテーブル。

        戻り値:
            None
        """
        table.to_csv(self.target_csv)


class ManagedEffortAssignmentCsv:
    """CSVデータを管理するためのクラスです.

    このクラスは、タスクデータを含むCSVファイルの読み込みと書き込みを管理���ます。
    Polarsバックエンドを使用して効率的にデータを処理します。

    メソッド:
    - read_csv_data: CSVデータを読み込みます。
    - save_csv_data: CSVデータを書き込みます。
    """

    target_csv = "api/datas/effort_assignment_data.csv"

    def read_csv_data(self) -> ibis.Table:
        """CSVデータを読み込みます.

        指定されたCSVファイルからタスクデータを読み込み、ibis.Tableオブジェクトとして返します。

        戻り値:
            ibis.Table: 読み込まれたタスクデータを含むテーブルオブジェクト。
        """
        return ibis.read_csv(self.target_csv)

    def save_csv_data(self, table: ibis.Table) -> None:
        """CSVデータを書き込みます.

        受け取ったibis.Tableオブジェクトのデータを指定されたCSVファイルに保存します。

        パラメータ:
            table (ibis.Table): 保存するタスクデータのテーブル。

        戻り値:
            None
        """
        table.to_csv(self.target_csv)
