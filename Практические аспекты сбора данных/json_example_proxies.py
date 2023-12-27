import requests
import json
import pandas as pd

cookies = {
    'is_seo_or_robot': 'seo',
    'srv_menu_gender': 'women',
    'lid': 'ZEACoGVNHiRL43Ugt0usAgA=',
    '_gcl_au': '1.1.2080383149.1699552806',
    'wt_cdbeid': '1',
    'wt3_sid': '%3B717012440280310',
    'sessionId': '16995528074799726604',
    'is_synced': 'true',
    'uxs_uid': 'd15bb8e0-7f29-11ee-b78b-c174e6b40039',
    '_gid': 'GA1.2.435705918.1699552809',
    'tmr_lvid': 'f293e5c0a97f358d969e4f2cc29bbb83',
    'tmr_lvidTS': '1699552808711',
    '_sp_ses.d14a': '*',
    '_ym_uid': '1699552809498784634',
    '_ym_d': '1699552809',
    'lmda_site_version': '23.11.09_2',
    'qrator_ssid': '1699552809.959.CeGRFYV64K6VQNNZ-gko9r8gnqer2s305dpvh827o6i2hk8co',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'search_gender': '',
    'XCookieNotifyWasShown': 'true',
    'wt_geid': '68934a3e9455fa72420237eb',
    'LMDA': '',
    'lmda_adBlocker': '0',
    'wt3_eid': '%3B717012440280310%7C2169955280769646215%232169955291767827497',
    '_sp_id.d14a': '2bcc3c88-efa5-4032-9f60-2cc37e26570e.1699552809.1.1699552918..c2a8a330-db30-443c-9f44-693362cdca46..4c6a647e-8ee0-4209-bb15-c9a1ff847c14.1699552808735.16',
    '_ga': 'GA1.1.1393014591.1699552809',
    'tmr_detect': '0%7C1699552920166',
    'wt_rla': '717012440280310%2C11%2C1699552807478',
    'sid': 'M2FiNGVhOGFlYzk2NWRjYzBhMzJjODZmOGIyNmZkYjk=|1699551175|a6ea3b5726064183c8666048e84197c760382fca',
    '_ga_120XMWN72V': 'GS1.1.1699552808.1.1.1699552975.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'is_seo_or_robot=seo; srv_menu_gender=women; lid=ZEACoGVNHiRL43Ugt0usAgA=; _gcl_au=1.1.2080383149.1699552806; wt_cdbeid=1; wt3_sid=%3B717012440280310; sessionId=16995528074799726604; is_synced=true; uxs_uid=d15bb8e0-7f29-11ee-b78b-c174e6b40039; _gid=GA1.2.435705918.1699552809; tmr_lvid=f293e5c0a97f358d969e4f2cc29bbb83; tmr_lvidTS=1699552808711; _sp_ses.d14a=*; _ym_uid=1699552809498784634; _ym_d=1699552809; lmda_site_version=23.11.09_2; qrator_ssid=1699552809.959.CeGRFYV64K6VQNNZ-gko9r8gnqer2s305dpvh827o6i2hk8co; _ym_isad=2; _ym_visorc=b; search_gender=; XCookieNotifyWasShown=true; wt_geid=68934a3e9455fa72420237eb; LMDA=; lmda_adBlocker=0; wt3_eid=%3B717012440280310%7C2169955280769646215%232169955291767827497; _sp_id.d14a=2bcc3c88-efa5-4032-9f60-2cc37e26570e.1699552809.1.1699552918..c2a8a330-db30-443c-9f44-693362cdca46..4c6a647e-8ee0-4209-bb15-c9a1ff847c14.1699552808735.16; _ga=GA1.1.1393014591.1699552809; tmr_detect=0%7C1699552920166; wt_rla=717012440280310%2C11%2C1699552807478; sid=M2FiNGVhOGFlYzk2NWRjYzBhMzJjODZmOGIyNmZkYjk=|1699551175|a6ea3b5726064183c8666048e84197c760382fca; _ga_120XMWN72V=GS1.1.1699552808.1.1.1699552975.0.0.0',
    'Referer': 'https://www.lamoda.ru/c/15/shoes-women/?sitelink=topmenuW&l=4',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'sitelink': 'topmenuW',
    'l': '4',
    'page': '2',
    'shift': '0',
    'json': '1',
}

http_proxy  = "http://60.210.40.190"
https_proxy = "https://60.210.40.190"

proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy
            }
prox = [

]

yeild 
next
try:
    response = requests.get('https://www.lamoda.ru/c/15/shoes-women/'
                            , params=params
                            , cookies=cookies
                            , headers=headers
                            , proxies=proxies)
    response.raise_for_status()
except Exception as e:
    print(e)

analyze_data = json.loads(response.text)
products = analyze_data['payload']['products']

df = pd.DataFrame(columns=['name', 'price', 'sku'])

df['name'] = [p['name'] for p in products]
df['price'] = [p['price_amount'] for p in products]
df['sku'] = [p['sku'] for p in products]

print(df)
# сохраняем в csv
# делаем цикл по страницам
# делаем цикл по времени