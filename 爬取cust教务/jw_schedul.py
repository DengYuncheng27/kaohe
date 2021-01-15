# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
import re
import json
import urllib.parse
import base64

os.environ['NO_PROXY'] = 'stackoverflow.com'

'''
    目标： 获取教务上的课表
    分析： 
        从拿到课表信息的地址开始。
            1. QueryStudentScheduleData : 返回json文件包含所有的课程信息。 
                * url=https://jwgls2.cust.edu.cn/api/ClientStudent/Home/StudentHomeApi/QueryStudentScheduleData
                * 需要的cookie 两个  domain: jwgls2.cust.edu.cn	
                    * wengine_new_ticket=52605163d969cbb3; 
                    * ASP.NET_SessionId=nbpf5t30y3or32krwhgxkrjh
            2. ASP.NET_SessionId：
                请求url：https://jwgls2.cust.edu.cn/api/LoginApi/LGSSOLocalLogin
                需要的cookie ：wengine_new_ticket domain：jwgls2.cust.edu.cn
                需要的参数有个param：
                    param是通过ticket和固定的一段url拼接后再将字符转换成percent编码后再通过base64加密得到的。 
                    
            3. wengine_new_ticket  domain：jwgls2.cust.edu.cn
                请求url：https://jwgls2.cust.edu.cn/wengine-auth/token-login?wengine-ticket=2ce3fc7b-c230-47ef-936a-4028ca802b0a&from=https://jwgls2.cust.edu.cn/welcome
                名称: token-login?wengine-ticket=2ce3fc7b-c230-47ef-936a…8ca802b0a&from=https://jwgls2.cust.edu.cn/welcome
            4. 拿到第三点中的请求url
                第三点中的url是多个302重定向最终得到的，追踪重定向一直到开头，发现就是从potal那边跳转到教务这边的网址。 
                即：https://portal.cust.edu.cn/custp/x/to?siteId=d11c3e894ffa410ca9d4786287298714
                
        登录potal ：https://portal.cust.edu.cn/custp/index
             1. 获取到execution
                这个在登录的界面直接搜就行，用bs4可以直接得到这个的值。
             
             2. 登录
                url：https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas
                带上execution和账号密码post提交即可模拟登录成功。
                登录后拿到需要的cookie就可以去访问教务了。 
    
    问题：
        1. 在统一接口中拿到登录教务需要的cookie后，在访问教务的时候重定向的第四个链接访问状态码是200，预期是302继续重定向的。 
            url：https://mysso.cust.edu.cn/cas/login?service=http://wwwn.cust.edu.cn/wengine-auth/login?cas_login=true
            描述： 访问它的cookie都有，在浏览器中访问得到的是302,但是在这个请求中的得到的确是200。 
            该问题导致无法进行。
    
    

                
'''

def main():
    base_url = "https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas" # 账号密码提交的url
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    execution = get_execution(base_url)
    session = requests.Session()  # 构造Session
    get_js_pac(session=session) #得到登录界面的 两个cookie pac和jsessionid
    portal_first(session=session, user_agent=userAgent, execution=execution) #提交并跳转到教务

def get_js_pac(session):
    url = "http://mysso-cust-edu-cn-s.webvpn.cust.edu.cn:8118/"  # 得到 jsession
    session.get(url)
    url_2="https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas"
    session.get(url_2)

def get_execution(url):
    res = requests.get(url, verify=False)
    html = res.content.decode("utf-8")
    bs = BeautifulSoup(html, features="html.parser")
    execution = bs.find("input", {"name": "execution"}).attrs["value"]
    return execution


def portal_first(session, user_agent, execution):
    data = {
        "username": "2018002999",
        "password": "xq000812Mm.cn",
        "execution": execution,
        "_eventId": "submit",
        "geolocation": ""
    }
    url = "https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas" # 账号密码提交网址
    headers = {
        'User-agent': user_agent,
    }
    res = session.post(url=url, data=data, headers=headers, verify=False,
                       allow_redirects=False)  # allow_redirects 拒绝自动处理重定向
    redirect_url = res.headers["Location"]  # 带有ticket的重定向url
    session.get(redirect_url)
    print(session.cookies)


    #
    jw_url = "https://portal.cust.edu.cn/custp/x/to?siteId=d11c3e894ffa410ca9d4786287298714"  #统一接口跳转到教务的网址。 id是固定的

    status_code=302
    # 循环更新 cookie
    url = jw_url   #处理前几个302跳转的
    i = 1
    while status_code != 200 and i!=4 :  # 在前几个重定向中有一个网址浏览器中返回302 但是这里的代码返回的是200
        # 检查后发现所有需要的三个 cookie 都已获得，并且domain和path都没问题，确认为同一个cookie
        # 但是返回的还是200  拿不到location的值。
        temp_res = session.get(url,allow_redirects=False)
        status_code = temp_res.status_code
        url = temp_res.headers["Location"]
        print(url)
        print(status_code)
        print(session.cookies)
        print(i)
        i += 1

    '''
     这里缺少了一个处理后面几个重定向链接的，上面这个预期是302，结果返回的是200，拿不到原有的链接，进而得不到需要的cookie，再次终止。 
    '''


    # 获取含wengine-ticket这个请求参数的链接。
    wt_url = get_wengine_ticket(session=session)
    print(wt_url)
    get_wengine_new_ticket(session=session,url=wt_url) #更新 wengine_new_ticket
    LGSSO_url = "https://jwgls1.cust.edu.cn/api/LoginApi/LGSSOLocalLogin"  # 取ASP.NET_SessionId这个cookie
    param = get_param(session=session)  # 获取param
    data = {
        "param": param
    }
    res = session.post(url=LGSSO_url, data=data, headers=headers)
    print(session.cookies)

def get_wengine_ticket(session): # 这个拿到的是get请求后面的参数，实际是token的url

    url = "http://wwwn.cust.edu.cn/wengine-auth/login?id=59&path=/&from=https://jwgls1.cust.edu.cn/welcome"
    session.cookies['wengine_new_ticket'] = 'd3bafc471f08c1e5'  # 拿的浏览器的cookie,这里应该是我的    url中的 id 和什么东西没设置好的问题。
    temp_res = session.get(url, allow_redirects=False)
    str = temp_res.headers["Location"]
    print(temp_res.status_code)
    print(str)
    print(temp_res.content.decode("utf-8"))
    return str
def get_wengine_new_ticket(session,url):
    temp_res=session.get(url,allow_redirects=False)
    print(temp_res.status_code)
    for k, v in session.cookies.get_dict().items():
        print(k + ":" + v)
    print(temp_res.headers)





def get_param(session):
    url = "https://mysso.cust.edu.cn/cas/login?service=https://jwgl.cust.edu.cn/welcome"
    headers = {
        'content-type': 'application/json',
    }
    temp_res = session.get(url, headers=headers, allow_redirects=False)  # 禁止处理302
    print(temp_res.headers)
    print(temp_res.status_code)
    str = temp_res.headers["Location"]   # 返回值没有location
    ticket = re.match('ST.*', str)
    parm_dict = {
        'Ticket': ticket,
        'Url': "https://jwgl.cust.edu.cn/welcome"
    }
    temp_str = json.dumps(parm_dict)
    str = temp_str.replace(" ", "")
    print(str)
    replaceList = [  # 符号的percent编码
        '%7B',
        '%22',
        '%3A',
        '%2C',
        '%3A',
        '%2F',
        '%7D',
    ]
    for item in replaceList:
        replaceChar = urllib.parse.unquote(item)
        str = str.replace(replaceChar, item)
    print(str)
    encodestr = base64.b64encode(str.encode('utf-8'))
    param = bytes.decode(encodestr)
    return param


if __name__ == '__main__':
    main()
