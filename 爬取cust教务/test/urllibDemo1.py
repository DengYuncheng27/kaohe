# coding=utf-8

import urllib.request
import urllib.parse

url="https://jwgls2.cust.edu.cn/api/LoginApi/LGSSOLocalLogin"
cookie_str="wengine_new_ticket=1a0c5d29b5ad8e86; ASP.NET_SessionId=ag35bgks1moq2ujgrhpkod00"
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
data=bytes(urllib.parse.urlencode({"param":"JTdCJTIyVGlja2V0JTIyJTNBJTIyU1QtNDAyODYzMC1SSS1tbnAtTkQtcnhUVHZGMi1GLVRFRlNDajBsb2NhbGhvc3QlMjIlMkMlMjJVcmwlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmp3Z2wuY3VzdC5lZHUuY24lMkZ3ZWxjb21lJTIyJTdE"}),encoding="utf-8")
                                            JTdCJTIyVGlja2V0JTIyJTNBJTIyU1QtNDAyODc1Ni1teXRnTjJUT3MzV292NjlWeWF6LUYyUDdTSEFsb2NhbGhvc3QlMjIlMkMlMjJVcmwlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmp3Z2wuY3VzdC5lZHUuY24lMkZ3ZWxjb21lJTIyJTdE"
                                            JTdCJTIyVGlja2V0JTIyJTNBJTIyU1QtNDAyODgyOC00eWtac1RxdUNlbmlTc3FHdWplcmN4SzhLZVFsb2NhbGhvc3QlMjIlMkMlMjJVcmwlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmp3Z2wuY3VzdC5lZHUuY24lMkZ3ZWxjb21lJTIyJTdE
headers={
    "cookie":cookie_str,
    'User-Agent':userAgent,
}
req=urllib.request.Request(url=url,headers=headers,data=data) #构造request
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print(response.getcode())