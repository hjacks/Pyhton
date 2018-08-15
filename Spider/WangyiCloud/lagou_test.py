import re
import time
import math
import json

import requests
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
mydb = client['mydb']
lagou = mydb['lagou']

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "25",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "WEBTJ-ID=20180330161217-16275f6e36775-042f8b47f66289-3447755e-2073600-16275f6e368554; user_trace_token=20180330161217-0f9abd84-33f2-11e8-a528-525400f775ce; LGUID=20180330161217-0f9ac0fe-33f2-11e8-a528-525400f775ce; X_HTTP_TOKEN=5793d4c000446a245356c9619322230b; LG_LOGIN_USER_ID=36f57973aaee11baaeb45d344c0e573a05a8ae1f6031d53b; _putrc=947FFA9CE2737286; JSESSIONID=ABAAABAAADEAAFI41BAFAB046085D8F468B6413ED8FBD59; login=true; unick=%E5%BE%90%E6%B6%9B; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=40; gate_login_token=46eb14186b7feb2177c8a2ae6a3ecd228f43687f7b131d91; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522397537; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522397640; _ga=GA1.2.849008269.1522397537; _gid=GA1.2.259001917.1522397537; LGRID=20180330161359-4cab71b9-33f2-11e8-b663-5254005c3644; SEARCH_ID=d22c6f5c71404212ad0a822712821bb7; index_location_city=%E5%85%A8%E5%9B%BD",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    "X-Requested-With": "XMLHttpRequest"
}

def get_page(url, params):
    html = requests.post(url, data=params, headers=headers)
    json_data = json.loads(html.text)
    total_count = json_data['content']['positionResult']['totalCount']
    page_num = math.ceil(total_count/15) if math.ceil(total_count/15)<30 else 30
    get_info(url,page_num)

def get_info(url,page_num):
    for pn in range(1,page_num+1):
        params = {
            "first": "true",
            "pn": str(pn),
            "kd": "python"
        }

        try:
            html = requests.post(url, data=params, headers=headers)
            json_data = json.loads(html.text)
            results = json_data['content']['positionResult']['result']
            for result in results:
                data = {
                    "businessZones": result['businessZones'],
                    "city": result['city'],
                    "companyFullName": result['companyFullName'],
                    "companyLabelList": result['companyLabelList'],
                    "companySize": result['companySize'],
                    "district": result['district'],
                    "education": result['education'],
                    "financeStage": result['financeStage'],
                    "firstType": result['firstType'],
                    "formatCreateTime": result['formatCreateTime'],
                    "gradeDescription": result['gradeDescription'],
                    "imState": result['imState'],
                    "industryField": result['industryField'],
                    "jobNature": result['jobNature'],
                    "positionAdvantage": result['positionAdvantage'],
                    "positionLables": result['positionLables'],
                    "positionName": result['positionName'],
                    "salary": result['salary'],
                    "secondType": result['secondType'],
                    "workYear": result['workYear']
                }
                print("==============================================")
                print(data)
                lagou.insert(data)
            time.sleep(2)
        except requests.exceptions.ConnectionError:
            pass


if __name__ == "__main__":
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {
        "first": "true",
        "pn": "1",
        "kd": "python"
    }

    get_page(url,params)