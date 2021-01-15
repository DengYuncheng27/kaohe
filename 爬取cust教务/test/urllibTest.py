
#coding=utf-8

import urllib.request
import urllib.parse
url = "http://httpbin.org/status/200"

# 基本访问页面
response=urllib.request.urlopen(url)
print(response.headers())

# post请求
# data=bytes(urllib.parse.urlencode({"url":"nihao"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data)
# print(response.read().decode("utf-8"))

# url="https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas"
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
# }
# req=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
