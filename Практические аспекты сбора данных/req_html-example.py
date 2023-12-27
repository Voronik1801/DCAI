from requests_html import HTMLSession


cookies = {
    'sessionid': 'O9FGaE5zJz_VmnwqZrFS2Os5Q64VB2avvn4OdPkqtJU:1qWIve:WsZ--IxPeSWOnxjRzaj4lDtRzxY',
    'uid': 'TfTb5GTc8l5Pch6vBVETAg==',
    'otaSelectedCurrencyCode': 'RUB',
    '_hcfnl_funnel_uid': 'ZNzyYWTc8mE95y8B5isgag==',
    '_hcfnl_incognito': '0',
    'riskified_sid': '70c26918-e678-4c0f-9c6c-8473e7a91c51',
    '_ym_uid': '1688706652522787780',
    '_ym_d': '1692201571',
    'intercom-id-uw75u6kt': '69bec1f7-da7f-4116-b172-3b7004c6e1b0',
    'intercom-device-id-uw75u6kt': 'cdf84373-4f03-49a6-8aeb-9c89d4c1dc64',
    '_yoid': 'ee7347f0-3760-4732-9377-efe17a726707',
    '_hcfnl_fpr': 'a2817c0890cf84faec94ee8beb858bcf',
    'adrcid': 'AaTtlmBHdhr5sPzE1_yFoGQ',
    '__exponea_etc__': 'be6421cf-2bdc-4e8b-bcc4-755545de2740',
    '_hcfnl_hash': '4941bf15-fd8b-4bc2-bdf2-aaab8014ebcd',
    'csrftoken': '0jbEjUyEZ5KCuMjGSLAduyYOkw29Lpu4aM8eEX9yZSKsrz2AyMU50K3Gmpzh3dJm',
    'messages': '',
    'user_language': 'ru',
    'otaPixelRatio': '1.25',
    'otaSearchFormFrom': '20231111',
    'otaSearchFormTo': '20231112',
    'otaSearchFormDestination': '%7B%22country%22%3A%22%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD%22%2C%22countryEn%22%3A%22Kazakhstan%22%2C%22id%22%3A354%2C%22multicompleteType%22%3A%22region%22%2C%22name%22%3A%22%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B%22%2C%22nameEn%22%3A%22Almaty%22%2C%22regionId%22%3A%22%22%2C%22type%22%3A%22City%22%2C%22slug%22%3A%22kazakhstan%2Falmaty%22%7D',
    'otaSearchFormRooms': '%5B%7B%22adults%22%3A2%2C%22ages%22%3A%5B%5D%7D%5D',
    'is_auth': '0',
    'userlucky': '83',
    '_gid': 'GA1.2.2103173630.1699555049',
    '_gat': '1',
    'ost_page_count': '1',
    '_ga_55ZZL6H3T7': 'GS1.2.1699555049.11.1.1699555049.60.0.0',
    '_ga_D1NGWXS6ER': 'GS1.1.1699555050.11.0.1699555050.0.0.0',
    '_ga': 'GA1.1.831855508.1692201570',
    'adrdel': '1',
    '_yosid': '835a10b9-dc24-4385-974e-4ef2c4672fb6',
    '_ym_isad': '2',
}

headers = {
    'authority': 'ostrovok.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'sessionid=O9FGaE5zJz_VmnwqZrFS2Os5Q64VB2avvn4OdPkqtJU:1qWIve:WsZ--IxPeSWOnxjRzaj4lDtRzxY; uid=TfTb5GTc8l5Pch6vBVETAg==; otaSelectedCurrencyCode=RUB; _hcfnl_funnel_uid=ZNzyYWTc8mE95y8B5isgag==; _hcfnl_incognito=0; riskified_sid=70c26918-e678-4c0f-9c6c-8473e7a91c51; _ym_uid=1688706652522787780; _ym_d=1692201571; intercom-id-uw75u6kt=69bec1f7-da7f-4116-b172-3b7004c6e1b0; intercom-device-id-uw75u6kt=cdf84373-4f03-49a6-8aeb-9c89d4c1dc64; _yoid=ee7347f0-3760-4732-9377-efe17a726707; _hcfnl_fpr=a2817c0890cf84faec94ee8beb858bcf; adrcid=AaTtlmBHdhr5sPzE1_yFoGQ; __exponea_etc__=be6421cf-2bdc-4e8b-bcc4-755545de2740; _hcfnl_hash=4941bf15-fd8b-4bc2-bdf2-aaab8014ebcd; csrftoken=0jbEjUyEZ5KCuMjGSLAduyYOkw29Lpu4aM8eEX9yZSKsrz2AyMU50K3Gmpzh3dJm; messages=; user_language=ru; otaPixelRatio=1.25; otaSearchFormFrom=20231111; otaSearchFormTo=20231112; otaSearchFormDestination=%7B%22country%22%3A%22%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD%22%2C%22countryEn%22%3A%22Kazakhstan%22%2C%22id%22%3A354%2C%22multicompleteType%22%3A%22region%22%2C%22name%22%3A%22%D0%90%D0%BB%D0%BC%D0%B0%D1%82%D1%8B%22%2C%22nameEn%22%3A%22Almaty%22%2C%22regionId%22%3A%22%22%2C%22type%22%3A%22City%22%2C%22slug%22%3A%22kazakhstan%2Falmaty%22%7D; otaSearchFormRooms=%5B%7B%22adults%22%3A2%2C%22ages%22%3A%5B%5D%7D%5D; is_auth=0; userlucky=83; _gid=GA1.2.2103173630.1699555049; _gat=1; ost_page_count=1; _ga_55ZZL6H3T7=GS1.2.1699555049.11.1.1699555049.60.0.0; _ga_D1NGWXS6ER=GS1.1.1699555050.11.0.1699555050.0.0.0; _ga=GA1.1.831855508.1692201570; adrdel=1; _yosid=835a10b9-dc24-4385-974e-4ef2c4672fb6; _ym_isad=2',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = {
    'sid': '9b1f6c04-2a33-463a-95fc-391bbeff8280',
}

session = HTMLSession()
r = session.get('https://ostrovok.ru/', params=params, cookies=cookies, headers=headers)
r.html.render()
print(r)