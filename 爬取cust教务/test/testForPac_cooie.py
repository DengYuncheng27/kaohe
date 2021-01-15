import requests
import os
os.environ['NO_PROXY'] = 'stackoverflow.com'


url="http://mysso-cust-edu-cn-s.webvpn.cust.edu.cn:8118/" #得到 jsession
ses=requests.Session()
res=ses.get(url)
print(res.status_code)
print(ses.cookies)

url_2="https://mysso.cust.edu.cn/cas/?service=https://portal.cust.edu.cn/custp/shiro-cas"  #得到 pac
res=ses.get(url_2)
print(res.status_code)
print(ses.cookies)