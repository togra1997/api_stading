"""このモジュールは、FastAPIを使用してAPIを構築するための基本的な設定を行います.

- `api.api`モジュールから`router`をインポートし、APIのエンドポイントを定義します。
- FastAPIフレームワークの`FastAPI`クラスを使用してアプリケーションインスタンスを作成します.
- インポートした`router`をアプリケーションに組み込みます。

使用方法:
    uvicorn main:app --reload
"""

from api.api import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 必要に応じて許可するオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],  # 必要に応じて許可するHTTPメソッドを指定
    allow_headers=["*"],  # 必要に応じて許可するHTTPヘッダーを指定
)
app.include_router(router, prefix="")
