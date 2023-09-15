from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 创建一个无头浏览器对象
chrome_options = Options()
# 设置它为无框模式
chrome_options.add_argument('--headless')
# 如果在windows上运行需要加代码
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--proxy-server=http://代理服务器地址:代理服务器端口号")
browser = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

cookie_list = [
    {'domain': '.lianjia.com',
     'expiry': 1694703545,
     'httpOnly': False,
     'name': '_gat_dianpu_agent',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1694703545,
     'httpOnly': False,
     'name': '_gat_new_global',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1694703545,
     'httpOnly': False,
     'name': '_gat',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1694703545,
     'httpOnly': False,
     'name': '_gat_global',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': 'gz.lianjia.com',
     'expiry': 1694705282,
     'httpOnly': False,
     'name': '_qzjb',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1694703481826.1.0.0.0'},
    {'domain': 'gz.lianjia.com',
     'httpOnly': False,
     'name': 'srcid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'eyJ0Ijoie1wiZGF0YVwiOlwiMTZkNzdmYzNiM2MzMjY4MTc3MzljOTUzNmZhYzliMjUxYmVlN2ViNTc5OGU1NzAyMTEzMTA1NDk2ZWNlYzIyMDNiMGQyMGQ4NGIxZjRkYzFjNjgyY2E5YTBmNjJhOGVlODcyNTVjZTNiYzg4OTlhNGMxZDE4N2Y0YzBmNmE3MmI2NTMxZTQzYmI5YjdjYzU2NzllOTM0NWUzODE1OTdlMTIwNDI3ZjQyYzExMjI3NjBiZDI4ZWJjMjNhMzI1Njg1ODc5Mjk5MjYyZjI2YTc3ZTBjMTM0NDRkNDljMzdmZjM1NjlkZTAxYWY1ODIzY2Q5YzdmYmViOGY4ZjgxOTNjZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI4YmFhNmY5YVwifSIsInIiOiJodHRwczovL2d6LmxpYW5qaWEuY29tL2NoZW5namlhby8xMDg0MDE1MDc4NjkuaHRtbCIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'},
    {'domain': '.lianjia.com',
     'expiry': 1694789881,
     'httpOnly': False,
     'name': '_jzqckmp',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1694707199,
     'httpOnly': False,
     'name': 'sajssdk_2015_cross_new_user',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': 'gz.lianjia.com',
     'httpOnly': False,
     'name': '_qzjc',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1729263482,
     'httpOnly': False,
     'name': 'sensorsdata2015jssdkcross',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '%7B%22distinct_id%22%3A%2218a9432f4a7ada-0e1eae281e66ea-18525634-2007040-18a9432f4a8e15%22%2C%22%24device_id%22%3A%2218a9432f4a7ada-0e1eae281e66ea-18525634-2007040-18a9432f4a8e15%22%2C%22props%22%3A%7B%7D%7D'},
    {'domain': '.lianjia.com',
     'expiry': 1729263436,
     'httpOnly': False,
     'name': 'crosSdkDT2019DeviceId',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'jnejll--3vtehi-l8xmtzd7w0rl2fl-gtwnmbmqm'},
    {'domain': '.lianjia.com',
     'expiry': 1694803480,
     'httpOnly': False,
     'name': 'lianjia_token_secure',
     'path': '/',
     'sameSite': 'None',
     'secure': True,
     'value': '2.0015a433ba6c5e582204091a8b29541941'},
    {'domain': '.lianjia.com',
     'expiry': 1710471481,
     'httpOnly': False,
     'name': '_jzqx',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1694703482.1694703482.1.jzqsr=clogin%2Elianjia%2Ecom|jzqct=/.-'},
    {'domain': '.lianjia.com',
     'httpOnly': False,
     'name': 'Hm_lpvt_9152f8221cb6243a53c83b956842be8a',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1694703482'},
    {'domain': '.lianjia.com',
     'httpOnly': False,
     'name': '_jzqc',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1'},
    {'domain': '.lianjia.com',
     'expiry': 1726239481,
     'httpOnly': False,
     'name': 'Hm_lvt_9152f8221cb6243a53c83b956842be8a',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1694703482'},
    {'domain': 'gz.lianjia.com',
     'expiry': 1729263482,
     'httpOnly': False,
     'name': '_qzja',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1752647429.1694703481826.1694703481826.1694703481826.1694703481826.1694703481826.0.0.0.1.1'},
    {'domain': '.lianjia.com',
     'expiry': 1729263481,
     'httpOnly': False,
     'name': '_smt_uid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '65031f79.5a439e14'},
    {'domain': '.lianjia.com',
     'expiry': 1729263481,
     'httpOnly': False,
     'name': '_jzqa',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1950960363979249700.1694703482.1694703482.1694703482.1'},
    {'domain': '.lianjia.com',
     'expiry': 1702479480,
     'httpOnly': True,
     'name': 'ftkrc_',
     'path': '/',
     'sameSite': 'Lax',
     'secure': True,
     'value': 'e9352855-0da6-4a6a-a2e3-edcf2b3bd8af'},
    {'domain': 'gz.lianjia.com',
     'expiry': 1694707201,
     'httpOnly': False,
     'name': '_qzjto',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1.0'},
    {'domain': '.lianjia.com',
     'expiry': 1694789885,
     'httpOnly': False,
     'name': '_gid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'GA1.2.55927641.1694703486'},
    {'domain': '.lianjia.com',
     'expiry': 1694803480,
     'httpOnly': False,
     'name': 'security_ticket',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'aLe4y08Iuiw2lsWCvYXf6rUrkGsvvYmxyZkeIQXQyau9xNt+il5P9yHjD2EuEMlLOCr9ogkF7tOS/hcl8Rsbkvs9bw3qaVGUWhVcE7MrI+Ce2CsJJcbfc/LxI+eh+TkU2J/Qt1tgCM3wdM8GZPs0DbqjJT1I/9UiH2G89pfuzpI='},
    {'domain': '.lianjia.com',
     'expiry': 1694803480,
     'httpOnly': False,
     'name': 'lianjia_token',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '2.0015a433ba6c5e582204091a8b29541941'},
    {'domain': '.lianjia.com',
     'expiry': 1694789835,
     'httpOnly': False,
     'name': 'select_city',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '440100'},
    {'domain': 'gz.lianjia.com',
     'expiry': 1697295483,
     'httpOnly': False,
     'name': 'BMAP_SECKEY',
     'path': '/chengjiao',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'TzufXFzMip1e5KXGtqyuBlXtEgUz2B4TzLkIlrEaMqaVBgHs1fD_ekKmGDOdDGXJuidqpO1yLQiIfxjjkWtr0iyBGANTE4IOQ5xYWEnv41AYuiO-BnejChVwsfpzcWYD3P3Ah09Y16bB7tTMSPorEdXlufqIug3LVENQV4WrO_X4tLOF14COJb84Tetb4Je1'},
    {'domain': '.lianjia.com',
     'expiry': 1729263485,
     'httpOnly': False,
     'name': '_ga',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'GA1.2.1248027501.1694703486'},
    {'domain': '.lianjia.com',
     'expiry': 1694705282,
     'httpOnly': False,
     'name': '_jzqb',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '1.1.10.1694703482.1'},
    {'domain': '.lianjia.com',
     'expiry': 1694803480,
     'httpOnly': True,
     'name': 'login_ucid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '2000000023004788'},
    {'domain': '.lianjia.com',
     'expiry': 1729263435,
     'httpOnly': False,
     'name': 'lianjia_uuid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'affa6e0f-e0c1-4a8e-9331-4276c85d7170'},
    {'domain': '.lianjia.com',
     'expiry': 1726239480,
     'httpOnly': True,
     'name': 'lfrc_',
     'path': '/',
     'sameSite': 'Lax',
     'secure': True,
     'value': 'cd133fdf-0d0c-4c2f-b710-48445fadbc05'},
    {'domain': '.lianjia.com',
     'expiry': 1694705289,
     'httpOnly': False,
     'name': 'lianjia_ssid',
     'path': '/',
     'sameSite': 'Lax',
     'secure': False,
     'value': '9633ad02-4259-44a7-a3d5-650beb19b882'},
    {'domain': 'gz.lianjia.com',
     'expiry': 1697295482,
     'httpOnly': False,
     'name': 'SECKEY_ABVK',
     'path': '/chengjiao',
     'sameSite': 'Lax',
     'secure': False,
     'value': 'V7OwhSlPZppmUNtpDKOlMVPPksBzrAZjQmGxGBZVgpix//MizH0Xa56FIldPPgLV7W1MxivdNS5D95wkMxSATQ%3D%3D'}
]

driver.get('https://gz.lianjia.com/')
for item in cookie_list:
    driver.add_cookie(item)

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
