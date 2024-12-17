import json

import requests


class ApiCliant:
    """APIクライアントクラス.

    指定されたURLに対してGET、POST、PUT、DELETEリクエストを送信するメソッドを提供します。

    Attributes:
        url (str): リクエストを送信する対象のURL。

    """

    def __init__(self, url: str) -> None:
        """ApiCliantのコンストラクタ.

        Args:
            url (str): リクエストを送信する対象のURL。

        """
        self.url = url

    def get(self):
        """GETリクエストを送信する.

        Returns:
            Response: リクエストのレスポンスオブジェクト。

        """
        return requests.get(self.url, timeout=10).json()

    def post(self, data: dict):
        """POSTリクエストを送信する.

        Args:
            data (dict): リクエストボディに含めるデータ。

        Returns:
            Response: リクエストのレスポンスオブジェクト。

        """
        return requests.post(url=self.url, data=json.dumps(data), timeout=10).json()

    def put(self, data: dict, target_id: str):
        """PUTリクエストを送信する.

        Args:
            data (dict): リクエストボディに含めるデータ。
            target_id (str): 更新対象のリソースID。

        Returns:
            Response: リクエストのレスポンスオブジェクト。

        """
        return requests.put(
            f"{self.url}/{target_id}",
            data=json.dumps(data),
            timeout=10,
        ).json()

    def delete(self, target_id: str):
        """DELETEリクエストを送信する.

        Args:
            target_id (str): 削除対象のリソースID。

        Returns:
            Response: リクエストのレスポンスオブジェクト。

        """
        return requests.delete(f"{self.url}/{target_id}", timeout=10).json()
