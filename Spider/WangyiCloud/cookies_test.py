import requests

headers = {
    "Coolies":'ll="118172"; bid=uein-qifvcA; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1522394728%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DOKEl2NXcGlbSwNfI7M5ibyEBkSwJIbi_JDTUlWfYWu-xPskfyJYr3RNMkcXFBOLe%26wd%3D%26eqid%3D8ebac77900001e70000000035abde663%22%5D; _pk_id.100001.8cb4=a647dfffe55ce83b.1522394728.1.1522395568.1522394728.; _pk_ses.100001.8cb4=*; __utma=30149280.1955181715.1522394735.1522394735.1522394735.1; __utmb=30149280.18.10.1522394735; __utmc=30149280; __utmz=30149280.1522394735.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ps=y; dbcl2="176144025:nipm1RL2Ok0"; ck=ifqU; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17614; __yadk_uid=oU8fHvG8OIo7QnxH97yjEo445osFLmrX; __utmt=1; ap=1'
}

url = 'www.douban.com'
html = {url,headers=headers}
print(html.text)