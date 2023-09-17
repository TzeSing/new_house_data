import json

from absl import app, flags
from selenium import webdriver
from selenium.webdriver.common.by import By

FLAGS = flags.FLAGS
flags.DEFINE_bool('virtual_display', False, 'use virtual_display')
flags.DEFINE_bool('headless', False, 'headless option')


def main(_):
    virtual_display = FLAGS.virtual_display
    headless = FLAGS.headless
    
    if virtual_display:
        from pyvirtualdisplay import Display
        display = Display(visible=False, size=(800, 600))
        display.start()
    
    # chrome_options.add_argument("--proxy-server=http://代理服务器地址:代理服务器端口号")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    print('init driver')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    # TODO:让其自动生成cookies
    with open('cookies.json', 'r') as f:
        cookie_list = json.load(f)
    
    driver.get('https://gz.lianjia.com/')
    for item in cookie_list:
        driver.add_cookie(item)
    
    print('start...')
    
    # TODO: 从redis获取剩下的
    driver.get('https://gz.lianjia.com/chengjiao/108401507869.html')
    driver.implicitly_wait(1)
    
    # 点击
    # 交通-教育-医疗-购物-生活
    # 地铁站-公交站
    # 幼儿园-小学-中学-大学
    # 医院-药店x
    # 商场x-超市-市场
    # 银行-ATMx-餐厅x-咖啡馆x
    
    # for i in range(1, 1):
    
    # 点击交通
    # 点击地铁
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)
    
    # 点击公交
    target_elem = driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/div[1]/div[2]')
    driver.execute_script('arguments[0].click()', target_elem)
    
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)
    
    # 点击教育
    target_elem = driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/ul/li[2]')
    driver.execute_script('arguments[0].click()', target_elem)
    
    # 幼儿园
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)
    
    # 点击小学
    target_elem = driver.find_element(By.XPATH, '//*[@id="around"]/div/div[2]/div[1]/div[2]')
    driver.execute_script('arguments[0].click()', target_elem)
    
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[2]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[1]/span[4]').text)
    print(driver.find_element(By.XPATH, '//*[@id="mapListContainer"]/ul/li[1]/div/div[2]').text)
    
    print()
    
    # TODO: 写入mysql
    
    driver.quit()
    if virtual_display:
        display.stop()


if __name__ == '__main__':
    app.run(main)
