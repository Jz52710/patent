import requests
import time
import base64

codeurl = 'http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml'

valcode = requests.get(codeurl)
print(valcode.content)

timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())

# 专利检索及分析图片验证码路径
path = r"C:\Users\86427\Desktop\patent\yzm"

with open(path+timestamp+'.jpg','wb') as f:
    f.write(valcode.content)

data = {
    "j_loginsuccess_url": "",
    "j_validation_code": "",
    "j_username": 'NTY5amlh',#NTY5amlh
    "j_password": 'ano1MjcxMA=='#ano1MjcxMA==
}

code = input('请输入验证码：')
data["j_validation_code"] = str(code)

Header = {
    "Host": "www.pss-system.gov.cn",
    "Referer": "http://www.pss-system.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml",
    "Origin": "http://www.pss-system.gov.cn",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # "Accept-Encoding:": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

Url = 'http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uiIndex.shtml'

resp = requests.post(Url, headers=Header, cookies=requests.utils.dict_from_cookiejar(valcode.cookies),data=data)

print(resp.status_code)
print(resp.text)
