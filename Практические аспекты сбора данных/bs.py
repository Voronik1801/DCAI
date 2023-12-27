import requests
from bs4 import BeautifulSoup

cookies = {
    '__ddg1_': 'bz8bsgGaQdNumhaVCWoB',
    'advcake_track_id': '555b4cc5-bc39-21a9-5224-22b6686c49a6',
    'advcake_session_id': '11d84717-3081-a092-56dd-db635ca5bef6',
    '_gcl_au': '1.1.2114635074.1699552795',
    '_gid': 'GA1.2.755840517.1699552795',
    '_userGUID': '0:lorhupsx:cpoKTPUumVVy_deC3CHk4eoeDsUze_tj',
    '_ym_uid': '1699552797168765647',
    '_ym_d': '1699552797',
    'tmr_lvid': '22d4913b844d0774a6010c9b6cd61e85',
    'tmr_lvidTS': '1699552797464',
    'rrpvid': '701062268354648',
    'g4c_x': '1',
    'rcuid': '654d1e1fc04f6047607b81c9',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '1380a64c-e53c-4d8e-be95-92f46f72dc4c',
    'enPop_sessionId': 'eb720008-7f2c-11ee-bcc7-226825693e1a',
    'clv_UserID_118573': 'ccefc6b8-77ab-a153-e96f-c7eda951e3b8.118573',
    'analytic_id': '1699554144417054',
    'r2UserId': '1699554144552292',
    'digi_uc': 'W10=',
    '_ga_XC9DJE7QFL': 'GS1.1.1699628039.2.0.1699628039.60.0.0',
    '_ga': 'GA1.2.144623230.1699552795',
    '_ym_b': 'c81e728d9d4c2f636f067f89cc14862c',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'dSesn': '0ad74fe3-d7db-c7fb-1bb2-6d467055bcaf',
    '_dvs': '0:losqnesx:APLQe_VnWS8YBUOrMvj55gtAm9YaEc2a',
    'rrwpswu': 'true',
    'tmr_detect': '0%7C1699628042547',
}

headers = {
    'authority': 'brandshop.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=bz8bsgGaQdNumhaVCWoB; advcake_track_id=555b4cc5-bc39-21a9-5224-22b6686c49a6; advcake_session_id=11d84717-3081-a092-56dd-db635ca5bef6; _gcl_au=1.1.2114635074.1699552795; _gid=GA1.2.755840517.1699552795; _userGUID=0:lorhupsx:cpoKTPUumVVy_deC3CHk4eoeDsUze_tj; _ym_uid=1699552797168765647; _ym_d=1699552797; tmr_lvid=22d4913b844d0774a6010c9b6cd61e85; tmr_lvidTS=1699552797464; rrpvid=701062268354648; g4c_x=1; rcuid=654d1e1fc04f6047607b81c9; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=1380a64c-e53c-4d8e-be95-92f46f72dc4c; enPop_sessionId=eb720008-7f2c-11ee-bcc7-226825693e1a; clv_UserID_118573=ccefc6b8-77ab-a153-e96f-c7eda951e3b8.118573; analytic_id=1699554144417054; r2UserId=1699554144552292; digi_uc=W10=; _ga_XC9DJE7QFL=GS1.1.1699628039.2.0.1699628039.60.0.0; _ga=GA1.2.144623230.1699552795; _ym_b=c81e728d9d4c2f636f067f89cc14862c; _ym_isad=2; _ym_visorc=b; dSesn=0ad74fe3-d7db-c7fb-1bb2-6d467055bcaf; _dvs=0:losqnesx:APLQe_VnWS8YBUOrMvj55gtAm9YaEc2a; rrwpswu=true; tmr_detect=0%7C1699628042547',
    'if-none-match': 'W/"66328-3VNelgNTTuFaH9JC0K6K9smZhfc"',
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

response = requests.get('https://brandshop.ru/zhenskoe/', cookies=cookies, headers=headers)

if response.ok:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.select('div.product-card')

    for product in products:
        # Extract product name
        name = product.select_one('.product-card__title').text
        # Extract product price
        price = product.select_one('.product-card__price').text
        img = product.select_one('img')
        print(f'Product Name: {name}, Price: {price}')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')