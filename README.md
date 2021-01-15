
# 目标： 获取教务上的课表
    ## 分析： 
        ### 从拿到课表信息的地址开始。
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
                
        ### 登录potal ：https://portal.cust.edu.cn/custp/index
             1. 获取到execution
                这个在登录的界面直接搜就行，用bs4可以直接得到这个的值。
             
             2. 登录
                url：https://mysso.cust.edu.cn/cas/login?service=https://portal.cust.edu.cn/custp/shiro-cas
                带上execution和账号密码post提交即可模拟登录成功。
                登录后拿到需要的cookie就可以去访问教务了。 
    
    ## 问题：
        1. 在统一接口中拿到登录教务需要的cookie后，在访问教务的时候重定向的第四个链接访问状态码是200，预期是302继续重定向的。 
            url：https://mysso.cust.edu.cn/cas/login?service=http://wwwn.cust.edu.cn/wengine-auth/login?cas_login=true
            描述： 访问它的cookie都有，在浏览器中访问得到的是302,但是在这个请求中的得到的确是200。 
            该问题导致无法进行。

