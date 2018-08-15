import json
import math
import time

import pymongo
import requests

client = pymongo.MongoClient()
mydb = client['mydb']
lagou = mydb['lagoutest']

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Length':'55',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'user_trace_token=20180330161217-0f9abd84-33f2-11e8-a528-525400f775ce; LGUID=20180330161217-0f9ac0fe-33f2-11e8-a528-525400f775ce; JSESSIONID=ABAAABAAADEAAFI773E2874660835931B64CB13913D83AD; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3Fcity%3D%25E6%259D%25AD%25E5%25B7%259E%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; X_HTTP_TOKEN=5793d4c000446a245356c9619322230b; LG_LOGIN_USER_ID=ed5718e75616ebe9c9dd6c0ac1f1201d8dd3531c3611084f; _putrc=947FFA9CE2737286; login=true; unick=%E5%BE%90%E6%B6%9B; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=40; gate_login_token=f9bc591b6557549fdfe9cd5c16884725585ded4b4ce4a05f; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528429234,1528429240,1528439349; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528439497; _gid=GA1.2.478708984.1528429234; _ga=GA1.2.849008269.1522397537; LGSID=20180608142908-3ff8f614-6ae5-11e8-96c6-525400f775ce; LGRID=20180608143137-98693fd4-6ae5-11e8-942d-5254005c3644; SEARCH_ID=8ac3d404f7594f3c82042bc49a11670a; index_location_city=%E5%85%A8%E5%9B%BD',
    'Host':'www.lagou.com',
    'Origin':'https://www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.5194.400 QQBrowser/9.7.13272.400',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest'
}

def get_page(url,params):
    html = requests.post(url,data=params,headers=headers)
    json_data = json.loads(html.text)
    total_count = json_data['content']['positionResult']['totalCount']
    page_number = math.ceil(total_count/15) if math.ceil(total_count/15) else 30
    get_info(url,page_number)

def get_info(url,page):
    for pn in range(1,page+1):
        params = {
            'first':'false',
            'pn':str(pn),
            'kd':'数据分析'
        }

        try:
            html = requests.post(url,data=params,headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                info = {
                    'businessZones':result['businessZones'],   
                    'city':result['city'],
                    'companyFullName':result['companyFullName'],
                    'companyLabelList':result['companyLabelList'],
                    'companyShortName':result['companyShortName'],
                    'companySize':result['companySize'],
                    'district':result['district'],
                    'education':result['education'],
                    'financeStage':result['financeStage'],
                    'firstType':result['firstType'],
                    'industryField':result['industryField'],
                    'industryLables':result['industryLables'],
                    'jobNature':result['jobNature'],
                    'positionAdvantage':result['positionAdvantage'],
                    'positionLables':result['positionLables'],
                    'positionName':result['positionName'],
                    'salary':result['salary'],
                    'secondType':result['secondType'],
                    'workYear':result['workYear']
                }
                print('+++++++++++++++++++++++++++++++++++++++')
                print(info)
                lagou.insert_one(info)
            time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass
            

if __name__ == '__main__':
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first':'true',
        'pn':'1',
        'kd':'数据分析'
    }

    get_page(url,params)