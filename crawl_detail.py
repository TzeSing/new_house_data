from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))
# display.start()
print('123')

# chrome_options.add_argument("--proxy-server=http://代理服务器地址:代理服务器端口号")

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

print('init driver')
driver = webdriver.Chrome(options=options)

# TODO:让其自动生成
cookie_list = [
    {'domain': '.lianjia.com', 'expiry': 1694827792, 'httpOnly': False, 'name': '_gat_dianpu_agent', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': '.lianjia.com', 'expiry': 1694827792, 'httpOnly': False, 'name': '_gat_new_global', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': '.lianjia.com', 'expiry': 1694827792, 'httpOnly': False, 'name': '_gat', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': '1'},
    {'domain': '.lianjia.com', 'expiry': 1694827792, 'httpOnly': False, 'name': '_gat_global', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': 'gz.lianjia.com', 'expiry': 1694829529, 'httpOnly': False, 'name': '_qzjb', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1.1694827728866.1.0.0.0'},
    {'domain': 'gz.lianjia.com', 'httpOnly': False, 'name': 'srcid', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': 'eyJ0Ijoie1wiZGF0YVwiOlwiMTZkNzdmYzNiM2MzMjY4MTc3MzljOTUzNmZhYzliMjViMWNmMTFlMzA1ZjkzNWUxYmM4NjE1OWU2OTNkZjY0OTE1NjYxNjdjMmE0Y2ZjMDViNzVlOWEyNTI2NGJlMTk1Mjk1MTY0ZDY3M2U5NWNmMDMwYzUyMGRkMDQxNGU2ZjU4MTc4MzkzZGNhMGFhNjNlODc3YjIxZjc3YzNjNTI0YjE5OTBjMDAzNjc5YmNiM2YzMmY5YjdkMzg3ZDk2NGFjNDg0MDY1MzA2YTMxYjBmYjY3YWExN2FjMTM3ZDM5MjgyMDZiOTc1M2I0OTk4ZWQxMTg2YTc2YjJjNGU2OTZjZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2YWQ0YmQ5Y1wifSIsInIiOiJodHRwczovL2d6LmxpYW5qaWEuY29tL2NoZW5namlhby8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='},
    {'domain': '.lianjia.com', 'expiry': 1694914128, 'httpOnly': False, 'name': '_jzqckmp', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': '.lianjia.com', 'httpOnly': False, 'name': 'Hm_lpvt_9152f8221cb6243a53c83b956842be8a', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1694827729'},
    {'domain': '.lianjia.com', 'httpOnly': False, 'name': '_jzqc', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com', 'expiry': 1729387700, 'httpOnly': False, 'name': 'crosSdkDT2019DeviceId', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '-ykpxm3--3vtehi-eecgwvqwxf0rdzj-v6jiualw0'},
    {'domain': '.lianjia.com', 'expiry': 1694927727, 'httpOnly': False, 'name': 'lianjia_token_secure', 'path': '/',
     'sameSite': 'None', 'secure': True, 'value': '2.001248a07f6bb2cbe703e5894e2ebd054d'},
    {'domain': '.lianjia.com', 'expiry': 1710595728, 'httpOnly': False, 'name': '_jzqx', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': '1.1694827729.1694827729.1.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/.-'},
    {'domain': '.lianjia.com', 'expiry': 1729387728, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
     'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '%7B%22distinct_id%22%3A%2218a9b9acf27787-08660ab15561b7-18525634-2007040-18a9b9acf281242%22%2C%22%24device_id%22%3A%2218a9b9acf27787-08660ab15561b7-18525634-2007040-18a9b9acf281242%22%2C%22props%22%3A%7B%7D%7D'},
    {'domain': 'gz.lianjia.com', 'httpOnly': False, 'name': '_qzjc', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com', 'expiry': 1694879999, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user',
     'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': 'gz.lianjia.com', 'expiry': 1729387729, 'httpOnly': False, 'name': '_qzja', 'path': '/',
     'sameSite': 'Lax', 'secure': False,
     'value': '1.1034839848.1694827728866.1694827728866.1694827728866.1694827728866.1694827728866.0.0.0.1.1'},
    {'domain': '.lianjia.com', 'expiry': 1729387728, 'httpOnly': False, 'name': '_smt_uid', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '650504d0.4a019236'},
    {'domain': '.lianjia.com', 'expiry': 1726363728, 'httpOnly': False,
     'name': 'Hm_lvt_9152f8221cb6243a53c83b956842be8a', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '1694827729'},
    {'domain': '.lianjia.com', 'expiry': 1729387728, 'httpOnly': False, 'name': '_jzqa', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': '1.2756595114066130400.1694827729.1694827729.1694827729.1'},
    {'domain': '.lianjia.com', 'expiry': 1702603727, 'httpOnly': True, 'name': 'ftkrc_', 'path': '/', 'sameSite': 'Lax',
     'secure': True, 'value': 'bbc915ef-e820-468c-b15f-4705188810c9'},
    {'domain': 'gz.lianjia.com', 'expiry': 1694880001, 'httpOnly': False, 'name': '_qzjto', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1.1.0'},
    {'domain': '.lianjia.com', 'expiry': 1694914132, 'httpOnly': False, 'name': '_gid', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': 'GA1.2.1997703701.1694827732'},
    {'domain': '.lianjia.com', 'expiry': 1694927727, 'httpOnly': False, 'name': 'security_ticket', 'path': '/',
     'sameSite': 'Lax', 'secure': False,
     'value': 'JjddaoXvmmAcn7yzEqnpF9ThL0eTXQH/BYG/qO/8G7bKQ4JqLK19QTzfHuzfDj72aQlsv/R8l+cuuMu0ah3viuo8BuLRS+PUfPbBCgaw1/FbgFdtEYFYqKWnMsYnQsmey0ZOHGE+5e9c47aA8E4W72wQyKNj4emrPHZ3QIubR7Y='},
    {'domain': '.lianjia.com', 'expiry': 1694927727, 'httpOnly': False, 'name': 'lianjia_token', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '2.001248a07f6bb2cbe703e5894e2ebd054d'},
    {'domain': '.lianjia.com', 'expiry': 1729387732, 'httpOnly': False, 'name': '_ga', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': 'GA1.2.553102834.1694827732'},
    {'domain': '.lianjia.com', 'expiry': 1694829529, 'httpOnly': False, 'name': '_jzqb', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': '1.1.10.1694827729.1'},
    {'domain': '.lianjia.com', 'expiry': 1694927727, 'httpOnly': True, 'name': 'login_ucid', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '2000000023004788'},
    {'domain': '.lianjia.com', 'expiry': 1694914099, 'httpOnly': False, 'name': 'select_city', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '440100'},
    {'domain': '.lianjia.com', 'expiry': 1726363727, 'httpOnly': True, 'name': 'lfrc_', 'path': '/', 'sameSite': 'Lax',
     'secure': True, 'value': '348c25a9-d7e0-4409-8cda-746ce572eb29'},
    {'domain': '.lianjia.com', 'expiry': 1694829531, 'httpOnly': False, 'name': 'lianjia_ssid', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': 'a229b024-7844-454f-a1a5-60b431d6e576'},
    {'domain': '.lianjia.com', 'expiry': 1729387699, 'httpOnly': False, 'name': 'lianjia_uuid', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '03c9e9b3-ed9a-4b8a-9cc8-1534c3479cef'}]

driver.get('https://gz.lianjia.com/')
for item in cookie_list:
    driver.add_cookie(item)

print('start...')

# TODO: 从redis获取剩下的
driver.get('https://gz.lianjia.com/chengjiao/108401507869.html')

# 滑动至最底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.implicitly_wait(2)

# WebDriverWait(driver, 10, 0.5).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]')
#                                    ))

# 点击
# 交通-教育-医疗-购物-生活
# 地铁站-公交站
# 幼儿园-小学-中学-大学
# 医院-药店x
# 商场x-超市-市场
# 银行-ATMx-餐厅x-咖啡馆x

# for i in range(1, 1):

# 点击交通
# driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/ul/li[1]').click()
# 点击地铁
# driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/div[1]/div[1]').click()

print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)

# 点击公交
driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/div[1]/div[2]').click()

print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)

# 点击教育
driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/ul/li[2]').click()

# 幼儿园
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)

# 点击小学
driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/div[1]/div[2]').click()

print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)

print()

# TODO: 写入mysql

driver.quit()
# display.stop()
