import requests
from bs4 import BeautifulSoup

cookies = {
    '__ddg1_': 'bz8bsgGaQdNumhaVCWoB',
    'advcake_track_id': '555b4cc5-bc39-21a9-5224-22b6686c49a6',
    'advcake_session_id': '11d84717-3081-a092-56dd-db635ca5bef6',
    '_gcl_au': '1.1.2114635074.1699552795',
    '_gid': 'GA1.2.755840517.1699552795',
    '_userGUID': '0:lorhupsx:cpoKTPUumVVy_deC3CHk4eoeDsUze_tj',
    'dSesn': '957c54a4-1bee-4c78-d2a5-03e733addb64',
    '_dvs': '0:lorhupsx:QZXItFK6vY8zLPdQ95VIlkbC4NGoxh5b',
    '_ym_uid': '1699552797168765647',
    '_ym_d': '1699552797',
    'tmr_lvid': '22d4913b844d0774a6010c9b6cd61e85',
    'tmr_lvidTS': '1699552797464',
    'rrpvid': '701062268354648',
    'g4c_x': '1',
    '_ym_isad': '2',
    'rcuid': '654d1e1fc04f6047607b81c9',
    '_ym_visorc': 'w',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': '1380a64c-e53c-4d8e-be95-92f46f72dc4c',
    '_dc_gtm_UA-15866208-1': '1',
    '_ym_b': '3c59dc048e8850243be8079a5c74d079',
    '_ga': 'GA1.1.144623230.1699552795',
    'enPop_sessionId': 'eb720008-7f2c-11ee-bcc7-226825693e1a',
    'rrwpswu': 'true',
    'tmr_detect': '0%7C1699554140416',
    'clv_UserID_118573': 'ccefc6b8-77ab-a153-e96f-c7eda951e3b8.118573',
    'analytic_id': '1699554144417054',
    'r2UserId': '1699554144552292',
    '_ga_XC9DJE7QFL': 'GS1.1.1699552795.1.1.1699554148.49.0.0',
}

headers = {
    'authority': 'brandshop.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=bz8bsgGaQdNumhaVCWoB; advcake_track_id=555b4cc5-bc39-21a9-5224-22b6686c49a6; advcake_session_id=11d84717-3081-a092-56dd-db635ca5bef6; _gcl_au=1.1.2114635074.1699552795; _gid=GA1.2.755840517.1699552795; _userGUID=0:lorhupsx:cpoKTPUumVVy_deC3CHk4eoeDsUze_tj; dSesn=957c54a4-1bee-4c78-d2a5-03e733addb64; _dvs=0:lorhupsx:QZXItFK6vY8zLPdQ95VIlkbC4NGoxh5b; _ym_uid=1699552797168765647; _ym_d=1699552797; tmr_lvid=22d4913b844d0774a6010c9b6cd61e85; tmr_lvidTS=1699552797464; rrpvid=701062268354648; g4c_x=1; _ym_isad=2; rcuid=654d1e1fc04f6047607b81c9; _ym_visorc=w; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=1380a64c-e53c-4d8e-be95-92f46f72dc4c; _dc_gtm_UA-15866208-1=1; _ym_b=3c59dc048e8850243be8079a5c74d079; _ga=GA1.1.144623230.1699552795; enPop_sessionId=eb720008-7f2c-11ee-bcc7-226825693e1a; rrwpswu=true; tmr_detect=0%7C1699554140416; clv_UserID_118573=ccefc6b8-77ab-a153-e96f-c7eda951e3b8.118573; analytic_id=1699554144417054; r2UserId=1699554144552292; _ga_XC9DJE7QFL=GS1.1.1699552795.1.1.1699554148.49.0.0',
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

# Check if the request was successful
if response.ok:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.select('div.product-card')

    for product in products:
        # Extract product name
        name = product.select_one('.product-name').text.strip()
        # Extract product price
        price = product.select_one('.product-price').text.strip()
        
        print(f'Product Name: {name}, Price: {price}')

else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')