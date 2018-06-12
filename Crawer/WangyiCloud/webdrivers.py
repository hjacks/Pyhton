# 模拟浏览器操作
# from selenium import webdriver

# driver = webdriver.PhantomJS()
# driver.get('https://www.douban.com/')
# driver.implicitly_wait(5)
# driver.find_element_by_id('form_email').clear()
# driver.find_element_by_id('form_email').send_keys('17342061167')
# driver.find_element_by_id('form_email').clear()
# driver.find_element_by_id('form_email').send_keys('xt123123654..')
# driver.find_element_by_class_name('bn-submit').click()
# print(driver.page_source)
# with open('hello.html','w',encoding='utf-8') as f:
#     f.write(driver.page_source)

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('https://www.jianshu.com/p/5c1d1b0d133a')
include_title = []
driver.implicitly_wait(20)
author = driver.find_element_by_xpath('//span[@class="name"]/a').text
date = driver.find_element_by_xpath('//span[@class="publish-time"]').text
words = driver.find_element_by_xpath('//span[@class="wordage"]').text
views = driver.find_element_by_xpath('//span[@class="views-count"]').text
comments = driver.find_element_by_xpath('//span[@class="comments-count"]').text
likes = driver.find_element_by_xpath('//span[@class="likes-count"]').text
inclues_names = driver.find_elements_by_xpath('//div[@class="include-collection"]/a/div')
for i in inclues_names:
    include_title.append(i.text)
print(author,date,words,views,comments,likes,include_title)
