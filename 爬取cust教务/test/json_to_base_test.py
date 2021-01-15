import json
import urllib.parse
import base64
ticket="ST-4030323-Uwsv5YgPZc9YJtIVaCNAqfZiDMwlocalhost"
parm_dict={
        'Ticket':ticket,
        'Url':"https://jwgl.cust.edu.cn/welcome"
    }
temp_str=json.dumps(parm_dict)
str=temp_str.replace(" ","")
print(str)
replaceList = [   #符号的percent编码
    '%7B',
    '%22',
    '%3A',
    '%2C',
    '%3A',
    '%2F',
    '%7D',
]
for item in replaceList:
    replaceChar=urllib.parse.unquote(item)
    str=str.replace(replaceChar,item)
print(str)
encodestr = base64.b64encode(str.encode('utf-8'))
param= bytes.decode(encodestr)
print(param)

