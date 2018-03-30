import requests
url = "https://www.douban.com/accounts/login"

params = {
    "source":"index_nav",
    "form_email":"17342061167",
    "form_password":"xt123123654.."
}
html = requests.post(url,params)
print(html)
print('=============================')
print(html.text)

