from selenium import webdriver
from lxml import etree
import time 
import pymongo

client = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
taobao = mydb['taobao']

driver = webdriver.PhantomJS()
driver.maximize_window()

def get_info(url,page):
    page = page+1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    with open('hello.html','w',encoding='utf-8') as f:
        f.write(driver.page_source)
    

def next_page():
    pass

if __name__ == '__main__':
    url = 'https://www.taobao.com'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')
    driver.find_element_by_class_name('btn-search').click()
    get_info(driver.current_url,1)

