from datetime import date

from hatebpy import HatenaBookmarkClient, OAuth1Auth, HatenaBookmarkFeedClient

from environment_variables import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    OAUTH_TOKEN,
    OAUTH_TOKEN_SECRET,
)


def bookmark_api(client: HatenaBookmarkClient):
    r0 = client.get_bookmark("https://example.com")
    print(r0)
    r1 = client.update_bookmark(
        url="https://example.com",
        comment="example.com test",
        tags=["example", "test"],
    )
    print(r1)
    r2 = client.get_bookmark("https://example.com")
    print(r2)
    r3 = client.delete_bookmark("https://example.com")
    print(r3)
    r4 = client.get_bookmark("https://example.com")
    print(r4)


def entry_api(client: HatenaBookmarkClient):
    r0 = client.get_entry("https://example.com")
    print(r0)
    r1 = client.get_entry("https://example.tokyo-to")
    print(r1)


def tag_api(client: HatenaBookmarkClient):
    r0 = client.get_tags()
    print(r0)


def user_api(client: HatenaBookmarkClient):
    r0 = client.get_user_info()
    print(r0)


def bookmark_count(client: HatenaBookmarkClient):
    r0 = client.get_bookmark_count(url="https://example.com")
    print(r0)
    r1 = client.get_bookmark_counts(
        urls=["https://example.com", "https://example.com", "https://example.tokyo-to"]
    )
    print(r1)


def entry_info(client: HatenaBookmarkClient):
    r0 = client.get_entry_info(url="http://www.hatena.ne.jp/")
    print(r0)
    r1 = client.get_entry_info(url="http://www.hatena.ne.jp/", use_lite=True)
    print(r1)


def get_feed():
    fc = HatenaBookmarkFeedClient()
    start = date(2024, 7, 1)
    end = date(2024, 7, 31)
    res = fc.search(
        search_type="text",
        q="Python",
        sort="recent",
        users=100,
        date_begin=f"{start:%Y-%m-%d}",
        date_end=f"{end:%Y-%m-%d}",
        max_pages=2,
    )
    print(res[0])
    print(len(res))


def main():
    auth = OAuth1Auth(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    hbc = HatenaBookmarkClient(auth)
    bookmark_api(hbc)
    entry_api(hbc)
    tag_api(hbc)
    user_api(hbc)
    bookmark_count(hbc)
    entry_info(hbc)
    get_feed()


if __name__ == "__main__":
    main()
