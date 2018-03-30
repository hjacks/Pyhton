# -*- coding:utf-8 -*-
import re

import time
import requests
from multiprocessing import Pool

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}

def re_scraper(url):
    res = requests.get(url,headers=headers)
    names = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote">.*?<i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    infos = list()
    for name,content,laugh,comment in zip(names,contents,laughs,comments):
        info = {
            'name':name,
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        infos.append(info)
        return infos
if __name__ == "__main__":
    urls = ['https://www.qiushibaike.com/8hr/page/{}/'.format(str(i)) for i in range(1,201)]
    # start_01 = time.time()
    # for url in urls:
    #     re_scraper(url)
    # end_01 = time.time()
    # print(u"串行性爬虫耗时：",end_01-start_01)

    # start_02 = time.time()
    # polls = Pool(processes=2)
    # polls.map(re_scraper,urls)
    # end_02 = time.time()
    # print(u"两爬虫耗时：",end_02-start_02)

    start_03 = time.time()
    polls = Pool(processes=4)
    polls.map(re_scraper,urls)
    end_03 = time.time()
    print(u"四爬虫耗时：",end_03-start_03)