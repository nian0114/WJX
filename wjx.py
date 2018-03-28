# -*- coding: utf-8 -*-
import requests
import urllib
import urllib2
from random import randint

"""
POST /joinnew/processjq.ashx?curid=21945553&starttime=2018%2F3%2F28%2022%3A42%3A05&source=directphone&submittype=1&rn=1919210476.53647438&t=1522248128032 HTTP/1.1
Host: www.wjx.cn
Connection: close
Content-Length: 24
Accept: text/plain, */*; q=0.01
Origin: https://www.wjx.cn
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.wjx.cn/m/21945553.aspx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
Cookie: .ASPXANONYMOUS=XZU9xTH90wEkAAAAMDI3OGRmNzgtMjc3OC00OGYyLWFlY2ItNTE4YWYzNTY4ODI4EBsgaau7rm0V6CFkK-ZvHmf6b_I1; jac21894007=78211911; ASP.NET_SessionId=tnctrzdnrydd5wr3dykybsa3; jac21930808=85440383; LastActivityJoin=21945553,101420916745; jac21945553=53647438

submitdata=1%241%7D2%242
"""

headers = {'Host': '/joinnew/processjq.ashx?curid=21945553&starttime=2018%2F3%2F28%2022%3A42%3A05&source=directphone&submittype=1&rn=1919210476.53647438&t=1522248128032',
           'Accept': 'text/plain, */*; q=0.01',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
           'Accept-Encoding': 'gzip, deflate',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Referer': 'https://www.wjx.cn/m/21945553.aspx',
           'Cookie': '.ASPXANONYMOUS=XZU9xTH90wEkAAAAMDI3OGRmNzgtMjc3OC00OGYyLWFlY2ItNTE4YWYzNTY4ODI4EBsgaau7rm0V6CFkK-ZvHmf6b_I1; jac21894007=78211911; ASP.NET_SessionId=tnctrzdnrydd5wr3dykybsa3; jac21930808=85440383; LastActivityJoin=21945553,101420916745; jac21945553=53647438',
           'Origin': 'https://www.wjx.cn',
           'X-Requested-With': 'XMLHttpRequest',
           'X-Forwarded-For': str(randint(1,255))+'.'+str(randint(1,255))+'.'+str(randint(1,255))+'.'+str(randint(1,255)),
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

s = requests.Session()
s.headers.update(headers)


def post(url, data,proxy_handler):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    #opener = urllib2.build_opener(proxy_handler)
    opener = urllib2.build_opener()
    urllib2.install_opener(opener)

    response = opener.open(req, data)
    return response.read()

def main():
    posturl = "https://www.wjx.cn/joinnew/processjq.ashx?curid=21945553&starttime=2018%2F3%2F28%2022%3A42%3A05&source=directphone&submittype=1&rn=1919210476.53647438&t=1522248128032"

    '''
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    proxyUser = "H1YM09D97F08206D"
    proxyPass = "A92F6C8282C65F71"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
        "user" : proxyUser,
        "pass" : proxyPass,
    }

    proxy_handler = urllib2.ProxyHandler({
        "http"  : proxyMeta,
        "https" : proxyMeta,
    })
    '''

    proxy_handler = ""
    data = {'submitdata':'1%241%7D2%242'}

    while 1:
        try:
            print post(posturl, data,proxy_handler)
        except:
            continue

if __name__ == '__main__':
    main()
