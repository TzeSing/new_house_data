from selenium.webdriver import Firefox
from time import sleep

# from webdriver_manager.chrome import ChromeDriverManager

# ChromeDriverManager().install()

# driver = webdriver.Chrome()

driver = Firefox()

url = "https://gz.lianjia.com/chengjiao/108404338634.html"
driver.get(url)

# 4.操作cookie
# 4.1 获取cookie
cookies = driver.get_cookies()
for cookie in cookies:
    # 值打印cookie中的name和value
    print("%s -> %s" % (cookie['name'], cookie['value']))

sleep(300)
