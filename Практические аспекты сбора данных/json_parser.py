import requests
import json
import pandas as pd

cookies = {
    '_ym_uid': '1699552809498784634',
    '_ym_d': '1699552809',
    'is_seo_or_robot': 'seo',
    'search_gender': '',
    'srv_menu_gender': 'women',
    'lid': 'ZEACnGWK4dsVfmp1HmsnAgA=',
    '_gcl_au': '1.1.650307889.1703600605',
    'uxs_uid': '55d4b960-a3fa-11ee-8c29-d51d52834b54',
    'lmda_site_version': '23.12.25',
    'wt_cdbeid': '1',
    'wt3_sid': '%3B717012440280310',
    'sessionId': '17036006081087296805',
    'qrator_ssid': '1703600608.383.4JbyHXGpSLNhjCWm-t304r7155caqdli5vctd2lk6c5cprmo9',
    'is_synced': 'true',
    '_gid': 'GA1.2.1408966087.1703600609',
    'tmr_lvid': '5c01716c013235657ca9080544a4310f',
    'tmr_lvidTS': '1703600608624',
    '_sp_ses.d14a': '*',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'wt_geid': '68934a3e9455fa72420237eb',
    'XCookieNotifyWasShown': 'true',
    'lmda_adBlocker': '0',
    'gd_city': '%D0%B3.%20%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0',
    'gd_aoid': '4400000300000',
    'gd_aoid_reg': '4400000000000',
    'LMDA': 'gd_lat=57.767915804407:gd_long=40.926914123787',
    'wt3_eid': '%3B717012440280310%7C2170360060832848692%232170360067042025123',
    'wt_rla': '717012440280310%2C2%2C1703600608107',
    '_ga': 'GA1.2.1975472522.1703600608',
    '_sp_id.d14a': '90f543b7-30bd-4d9a-9f80-fd2bc8cff317.1703600609.1.1703600671..692715ee-5fd7-4197-9315-b3fdcc4049e3..dfed569d-ebac-4078-9d91-d5f572ceca2f.1703600608823.2',
    'tmr_detect': '0%7C1703600673835',
    'sid': 'NDhkNGU3ZTM2ZmFlYjk0OThiMTA1Y2QzNzczMjM0Yjc=|1703598984|d99d68f1f09a23f70ed3333df84bde854d77e5d9',
    '_ga_120XMWN72V': 'GS1.1.1703600608.1.1.1703600784.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': '_ym_uid=1699552809498784634; _ym_d=1699552809; is_seo_or_robot=seo; search_gender=; srv_menu_gender=women; lid=ZEACnGWK4dsVfmp1HmsnAgA=; _gcl_au=1.1.650307889.1703600605; uxs_uid=55d4b960-a3fa-11ee-8c29-d51d52834b54; lmda_site_version=23.12.25; wt_cdbeid=1; wt3_sid=%3B717012440280310; sessionId=17036006081087296805; qrator_ssid=1703600608.383.4JbyHXGpSLNhjCWm-t304r7155caqdli5vctd2lk6c5cprmo9; is_synced=true; _gid=GA1.2.1408966087.1703600609; tmr_lvid=5c01716c013235657ca9080544a4310f; tmr_lvidTS=1703600608624; _sp_ses.d14a=*; _ym_isad=2; _ym_visorc=b; wt_geid=68934a3e9455fa72420237eb; XCookieNotifyWasShown=true; lmda_adBlocker=0; gd_city=%D0%B3.%20%D0%9A%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%BC%D0%B0; gd_aoid=4400000300000; gd_aoid_reg=4400000000000; LMDA=gd_lat=57.767915804407:gd_long=40.926914123787; wt3_eid=%3B717012440280310%7C2170360060832848692%232170360067042025123; wt_rla=717012440280310%2C2%2C1703600608107; _ga=GA1.2.1975472522.1703600608; _sp_id.d14a=90f543b7-30bd-4d9a-9f80-fd2bc8cff317.1703600609.1.1703600671..692715ee-5fd7-4197-9315-b3fdcc4049e3..dfed569d-ebac-4078-9d91-d5f572ceca2f.1703600608823.2; tmr_detect=0%7C1703600673835; sid=NDhkNGU3ZTM2ZmFlYjk0OThiMTA1Y2QzNzczMjM0Yjc=|1703598984|d99d68f1f09a23f70ed3333df84bde854d77e5d9; _ga_120XMWN72V=GS1.1.1703600608.1.1.1703600784.0.0.0',
    'Referer': 'https://www.lamoda.ru/c/15/shoes-women/?sitelink=topmenuW&l=4&page=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'sitelink': 'topmenuW',
    'l': '4',
    'page': '3',
    'json': '1',
}

response = requests.get('https://www.lamoda.ru/c/15/shoes-women/', params=params, cookies=cookies, headers=headers)
# print(response

# response = requests.post('https://www.lamoda.ru/c/15/shoes-women/', data=params, cookies=cookies, headers=headers)
if response.ok:
    analyze_data = json.loads(response.text)
    df = pd.DataFrame(columns=['name', 'price', 'sku', 'jpg'])
    products = analyze_data['payload']['products']
    df['name'] = [p['name'] for p in products]
    df['price'] = [p['price_amount'] for p in products]
    df['sku'] = [p['sku'] for p in products]
    df['jpg'] = [p['thumbnail'] for p in products]

for i in range(1, 10):
    params['page'] = i

# print(df)