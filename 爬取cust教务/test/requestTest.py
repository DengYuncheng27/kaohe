# coding=utf-8
import requests
import urllib.request
from requests.cookies import RequestsCookieJar

url = "https://mysso.cust.edu.cn/cas/login?service=http://wwwn.cust.edu.cn/wengine-auth/login?cas_login=true"
userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"

cookie_str="Cookie: TGC=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5aZWswVmlldnlJelFDWWtWZldNMDRRLno4Y3FKTE5kcHhNenpLN3lselNITS15N0Y2S29HbzNIZ3h1bVFIUDFZc090WHRMTmFLSDRPSDY0LTk3enB0eHl0ZEdmMGZmejQ0QnVfZkpJazdhLUFFQ2VVbHEtYUkwZG9tUUVRTkhRUG1Ya0tlU2laVDlXYzdiMmdXWXZUc0g1R0M1QXFsU2JGZDlKLUx5UGxsMDJaTExuamRUU2ZRaUNEYXJBMkdka25JelB2SUlZQVBQNzhHTDZVZ291b3IyXzQxU3pXTkdYb3NVS3dJSlFyd3ZtZVpISjlnY19xVmJFdU5XS2JaSVBac0RVeVNTU2FuSG9yU2Vld2dvUjYtc1huVnBXNzYycFU3WTFOLXFTcGtBWGpBLktjSnU3d1hQWlpVTENMNTNtcENXOUE=.u6XZ8XL28JR9v8B2WcrIgYPsF0Y0eBbXS_H2cGpHtSTdI4vzBCROBvQjHDuX1pinkFZaSsLgSgesHJjfvzpJgQ; JSESSIONID=994A2F6344D419E57FA0737FF3A5C51F; PAC4JDELSESSION=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5rcW9FbGE3cTFZTE9MN04yM1NVbDBnLkFiVkNyNG55bUFGNUlCeWtvTkdNUlkzTVdyREFLbUxfeXAyT1NjVjJoRzNnVU1VWWV0RUtrbVNXU2VUR2w2WUNGaXQ1TGM2QVJDY0xVLUQwUUh1WFlnQThOMGRIbnFUemFoeEJ0UTF5bzVidEM1MWwtTmdvMEg0NHNEaWwxQVJwem04MlFpMnByallzN3Y5U1NtYllob0YzNk9veDZmRmlJdjJpRWswOE1CbzI0OGNRdm5WS1d3MXBMdl9FcXl2b1dHWnJkU1VWZE5qTUNjak52Skt6ZmRtSGlhR1JHU3l5dGNzWWRyUzZiMUtiWmFOWjVfTzZGVEpXVlVSNFVhWWU4RHZpZ2tvdDRFSDZ4aUpoRXhXREl1OWpqbmU4Znl4SlpBWVNjX0xfYzJOcGh0bGdlTlVFZWxPWXN0T3pkMWI1QktpMy13R0dubVltY1h1dDk0MEl4X0phUmV2Q0JWb3VnRDZxNjhpdjVERS5iVk1YZm43dEZVdmdieEhTQUktc2x3.AaZEz_tnt-ivJClqj7gASo7UvoCSjyAQwPKb2Gwnujzjj-vpuXXEx6l4c8OSl78xUiyKis7vC39_breWy7mBCA"
headers={
    "cookie":cookie_str,
    'User-Agent':userAgent,
}
req=urllib.request.Request(url,headers=headers)
context=urllib.request.urlopen(req)
print(context.getcode())
print(context.headers)