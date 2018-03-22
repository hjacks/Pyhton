import requests

# 无参数
# r = requests.get("http://httpbin.org/get")
# print(r.url)

# 有参数
# pyload={
#     'key1':'value1',
#     'key2':'value2'
# }
# r = requests.get("http://httpbin.org/get",params=pyload)
# print(r.url)

# 设置header
# headers = {
#     'hello':'world'
# }
# r = requests.get('http://httpbin.org/get',headers = headers)
# print(r.text)

# 有数据
# pyload = {
#     'hello':'world'
# }
# r = requests.post('http://httpbin.org/post',data=pyload)
# print(r.text)

# 有数据(json)
# import json
# pyload = {
#     'hello':'world'
# }
# r = requests.post('http://httpbin.org/post',data=json.dumps(pyload))
# print(r.text)

# 传送文件
# url = 'http://httpbin.org/post'
# files = {
#     'file':open('test.txt','rb')
# }

# r = requests.post(url,files=files)
# print(r.text)

# Cookies
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are = 'working')

# r = requests.get(url,cookies = cookies)
# print(r.text)

# 请求超时
# url = 'http://github.com'
# r = requests.get(url,timeout=0.01)#设置1000就可以
# print(r.text)

# 持久会话
# url = 'http://httpbin.org/cookies/set/sessioncookie/123456789'#设置cookies
# s = requests.Session()#无这步，无法返回上传的cookies
# s.get(url)
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 代理IP
proxies = {
    'https':'http:41.118.132.69:4433'
}
r = requests.post('https://www.baidu.com',proxies=proxies)
print(r.status_code)
