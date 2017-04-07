# -*- coding: utf-8 -*-
import os
import math
from qiita_v2.client_base import QiitaClientBase


class QiitaClient(QiitaClientBase):
    def search_items(self, params=None, headers=None):
        """指定したクエリの投稿を返します。
        """
        return self.get("/items/", params, headers)


def search_posts(keywords='', n=100):
    access_token = os.environ('QiitaToken')
    client = QiitaClient(access_token=access_token)
    if n >= 100:
        pages = math.ceil(n / 100)
        per_page = 100
    else:
        pages = 1
        per_page = n
    res = []
    for page in range(1, pages + 1):
        items = client.search_items(params={'query': keywords, 'per_page': per_page, 'page': page})
        items = items.to_json()
        res.extend(items)
    return res[:n]

if __name__ == '__main__':
    items = search_posts(keywords="Python 機械学習", n=320)
    print(len(items))
