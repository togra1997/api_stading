"""このモジュールは、FastAPIを使用してAPIを構築するための基本的な設定を行います.

- `api.api`モジュールから`router`をインポートし、APIのエンドポイントを定義します。
- FastAPIフレームワークの`FastAPI`クラスを使用してアプリケーションインスタンスを作成します.
- インポートした`router`をアプリケーションに組み込みます。

使用方法:
    uvicorn main:app --reload
"""

from api.api import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router, prefix="")
