"""链家历年成交爬虫

需要实现以下功能：
- 分布式爬取
- ip代理池
- 端点续爬
- 每天更新
"""

import requests
from lxml import etree
from io import StringIO
from tqdm import tqdm
from fake_useragent import UserAgent

import time
import random

parser = etree.HTMLParser()

# api_url = "https://dps.kdlapi.com/api/getdps?secret_id=o1fjh1re9o28876h7c08&signature=oxf0n0g59h7wcdyvz2uo68ph2s&num=10&format=json&sep=1"
#
# # API接口返回的ip
# proxy_ip = requests.get(api_url).json()['data']['proxy_list']
#
# # 用户名密码认证(私密代理/独享代理)
# username = "t19431637290594"
# password = "9dmn4zm0"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password, 'proxy': random.choice(proxy_ip)}
# }

with open('done_urls.txt', 'r') as f:
    done_urls = f.read().strip().split('\n')
    done_urls = set(done_urls)

with open('new_urls.txt', 'r') as f, open('done_urls.txt', 'w') as fw1, open('detail.csv', 'w') as fw2, open('fail_urls.txt', 'w') as fw3:
    urls = f.read()
    urls = urls.strip().split('\n')
    
    # 写回去
    for done_url in done_urls:
        fw1.write(done_url + '\n')
    
    ua = UserAgent()
    for url in tqdm(urls):
        if url in done_urls:
            continue
        headers = {
            'User-Agent': ua.random,
            'Cookie': 'lianjia_uuid=ada170e4-3eff-4b7d-bb9e-f446debce2e3; _smt_uid=64c61682.1d08ef21; _jzqy=1.1690703492.1690703492.1.jzqsr=baidu.-; _ga=GA1.2.356894055.1692718380; _ga_6F76ZVFRYC=GS1.2.1692718381.1.0.1692718381.0.0.0; _gid=GA1.2.1081873728.1694182824; _jzqc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1694183031; crosSdkDT2019DeviceId=3wfgi6--7dndw7-6xy9qsenkt8gnck-t3mv7jufx; ftkrc_=af918d02-5fe5-4555-bc3e-a658fbf6bbad; lfrc_=d3085b68-3460-42cb-be8a-43ebac626165; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22189a5c7f0cbf32-09b804fb2c6652-1a525634-2007040-189a5c7f0cc100b%22%2C%22%24device_id%22%3A%22189a5c7f0cbf32-09b804fb2c6652-1a525634-2007040-189a5c7f0cc100b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; login_ucid=2000000023004788; lianjia_token=2.00132968826ad3031a028441b3c8b45b21; lianjia_token_secure=2.00132968826ad3031a028441b3c8b45b21; security_ticket=L18As9IkUlwLRE7VSLtKWKXDj7jYZ9knk1cwldWvd+MDXWbGZtPHUmzwo1pIpeP3E2wx0eDlQveVtpRMXY2qDOLDskqJfs+v6ElOH6XntDHlT8UBGjKpM+30ksbfjDcSRP+7qIQr2lIQUa3Q1yFTjPY51WmVAzHK0bxrDVceAO8=; _jzqckmp=1; _ga_654P0WDKYN=GS1.2.1694312891.1.0.1694312891.0.0.0; lianjia_ssid=6d7ed7cb-6067-440d-9393-b400a3b539a8; select_city=440100; _jzqa=1.1621836079642192100.1690703492.1694316246.1694355607.10; _jzqx=1.1694220347.1694355607.3.jzqsr=gz%2Elianjia%2Ecom|jzqct=/chengjiao/huangcun/pg10/.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1694355611; _jzqb=1.2.10.1694355607.1'
        }
        try:
            resp = requests.get(url, headers=headers)
        except OSError:
            print('OSError: Tunnel connection failed: 503 Service Unavailable')
            
        if resp.status_code == 200:
            tree = etree.parse(StringIO(resp.text), parser)
            
            detail_page_urls = tree.xpath('//ul[@class="listContent"]/li/a/@href')
            ul = tree.xpath('//ul[@class="listContent"]/li')
            for i, li in enumerate(ul):
                detail_page_url = detail_page_urls[i]
                
                title = li.xpath('div/div[@class="title"]/a/text()')
                title = title[0] if title else ''
                
                house_info = li.xpath('div/div[@class="address"]/div[@class="houseInfo"]/text()')
                house_info = house_info[0] if house_info else ''
                
                deal_date = li.xpath('div/div[@class="address"]/div[@class="dealDate"]/text()')
                deal_date = deal_date[0] if deal_date else ''
                
                total_price = li.xpath('div/div[@class="address"]/div[@class="totalPrice"]/span/text()')
                total_price = total_price[0] if total_price else ''
                
                position_info = li.xpath('div/div[@class="flood"]/div[@class="positionInfo"]/text()')
                position_info = position_info[0] if position_info else ''
                
                unit_price = li.xpath('div/div[@class="flood"]/div[@class="unitPrice"]/span/text()')
                unit_price = unit_price[0] if unit_price else ''
                
                deal_house_info_list = li.xpath('div/div[@class="dealHouseInfo"]/span[@class="dealHouseTxt"]/span/text()')
                deal_house_info_list = deal_house_info_list[0] if deal_house_info_list else ''
                
                deal_cycle_info = li.xpath('div/div[@class="dealCycleeInfo"]/span[@class="dealCycleTxt"]/span[1]/text()')
                deal_cycle_info = deal_cycle_info[0] if deal_cycle_info else ''
                
                deal_cycle_txt = li.xpath('div/div[@class="dealCycleeInfo"]/span[@class="dealCycleTxt"]/span[2]/text()')
                deal_cycle_txt = deal_cycle_txt[0] if deal_cycle_txt else ''
                
                agent = li.xpath('div/div[@class="agentInfoList"]/a/text()')
                agent = agent[0] if agent else ''
                
                fw2.write(
                    f'{detail_page_url},{title},{house_info},{deal_date},{total_price},{position_info},{unit_price},{deal_cycle_info},{deal_cycle_txt},{agent}')
                fw2.write('\n')
                fw2.flush()
            
            fw1.write(url + '\n')
            fw1.flush()
            time.sleep(2 + random.random())
        else:
            print(f'失败的url:{url}')
            fw3.write(url + '\n')
            
