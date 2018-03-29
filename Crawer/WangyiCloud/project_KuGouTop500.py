import time

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient()
songs = client.kugou_db.songs
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

def get_songs(url):
    web_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(web_data.text,"lxml")
    ranks = soup.select(".pc_temp_num")
    titles = soup.select(".pc_temp_songlist>ul>li>a")
    song_times = soup.select(".pc_temp_time")

    for rank,title,song_time in zip(ranks,titles,song_times):
        data = {
            "rank":rank.get_text().strip(),
            "singer":title.get_text().split('-')[0].strip(),
            "song":title.get_text().split('-')[1].strip(),
            "time":song_time.get_text().strip()
        }
        print(data)
        

if __name__ == "__main__":
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(str(i)) for i in range(1,2)]
    for url in urls:
        get_songs(url)
        time.sleep(1)