# import requests
# response = requests.get('http://www.baidu.com')
# print(response.text)
# print('==========================================')
# print(response.headers)
# print('==========================================')
# print(response.status_code)

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://m.weibo.com')