# hatebpy の使用方法

hatebpyは、はてなブックマークAPIを簡単に利用するためのPythonライブラリです。このドキュメントでは、主な機能の使用方法を説明します。

## インストール

pipを使用してインストールできます：

```bash
pip install hatebpy
```

## 認証

はてなブックマークAPIを使用するには、OAuthによる認証が必要です。以下のコマンドを実行して認証を行います：

```bash
hatebpy <consumer_key> <consumer_secret>
```

表示されるURLにアクセスし、認証後に表示されるPINコードを入力してください。認証が成功すると、アクセストークンが表示されます。

## 基本的な使用方法

### クライアントの初期化

```python
from hatebpy import HatenaBookmarkClient, OAuth1Auth

auth = OAuth1Auth(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
client = HatenaBookmarkClient(auth)
```

### ブックマークの取得

```python
from hatebpy.model import Bookmark

bookmark: Bookmark = client.get_bookmark("https://example.com")
print(bookmark)
```

### ブックマークの更新

```python
updated_bookmark: Bookmark = client.update_bookmark(
    url="https://example.com",
    comment="example.com test",
    tags=["example", "test"]
)
print(updated_bookmark)
```

### ブックマークの削除

```python
result: int = client.delete_bookmark("https://example.com")
print(result)
```

### エントリー情報の取得

```python
from hatebpy.model import Entry, NotFoundEntry

entry: Union[Entry, NotFoundEntry] = client.get_entry("https://example.com")
print(entry)
```

### タグの取得

```python
from hatebpy.model import Tags

tags: Tags = client.get_tags()
print(tags)
```

### ユーザー情報の取得

```python
from hatebpy.model import UserInfo

user_info: UserInfo = client.get_user_info()
print(user_info)
```

### ブックマーク数の取得

```python
count: int = client.get_bookmark_count(url="https://example.com")
print(count)
```

### 複数URLのブックマーク数取得

```python
counts: Dict[str, int] = client.get_bookmark_counts(
    urls=["https://example.com", "https://example.org"]
)
print(counts)
```

## フィード検索

HatenaBookmarkFeedClientを使用して、はてなブックマークのフィードを検索できます：

```python
from hatebpy import HatenaBookmarkFeedClient
from hatebpy.model import FeedEntry
from datetime import date

fc = HatenaBookmarkFeedClient()
start = date(2024, 7, 1)
end = date(2024, 7, 31)

results: List[FeedEntry] = fc.search(
    search_type="text",
    q="Python",
    sort="recent",
    users=100,
    date_begin=f"{start:%Y-%m-%d}",
    date_end=f"{end:%Y-%m-%d}",
    max_pages=2
)

print(results)
print(len(results))
```

これらの例を参考に、hatebpyを使ってはてなブックマークAPIの機能を活用してください。型アノテーションを活用することで、IDEの補完機能やタイプチェッカーを効果的に利用できます。
