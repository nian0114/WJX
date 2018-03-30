# -*- coding: utf-8 -*-
import requests
import urllib
import urllib2
import random

"""
POST /joinnew/processjq.ashx?curid=21925942&starttime=2018%2F3%2F30%2011%3A36%3A52&source=directphone&submittype=1&rn=1919210476&lct=49&t=1522381021549 HTTP/1.1
Host: www.wjx.cn
Connection: close
Content-Length: 182
Accept: text/plain, */*; q=0.01
Origin: https://www.wjx.cn
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://www.wjx.cn/m/21925942.aspx
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
Cookie: .ASPXANONYMOUS=rlxUNs390wEkAAAAN2IwYzQ4OTItMDU3Ni00MWVmLTkwZmMtNTAyYzg2Y2UzN2E09r7saLW-Lb6Mk9WLgqd5LJIusak1; UM_distinctid=16270f60bc721c-085df866e7bfdc-33697b04-1fa400-16270f60bc82bc; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1522313596; ASP.NET_SessionId=s4cx5jw4shcauybrfgblnzle; WjxUser=UserName=nian0114&Type=1; lllogcook=1; jac21925942=86424843; SojumpSurvey=010220BA00DAEE95D508FE205A12611096D50800086E00690061006E00300031003100340000012F00FFAEA47129E2C1429839A694D5E132A2AE4716DDD8; LastCheckUpdateDate=1; LastCheckDesign=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1522380745090; ev_21964368=1; CNZZDATA4478442=cnzz_eid%3D2146117123-1522308971-%26ntime%3D1522379678; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1522381014

submitdata=1%241%7D2%241%7D3%241%7D4%241%7D5%241!1%2C2!1%2C3!1%2C4!1%7D6%241!1%2C2!1%2C3!1%2C4!1%7D7%241!1%2C2!1%2C3!1%2C4!1%7D8%241!1%2C2!1%2C3!1%2C4!1%2C5!1%2C6!1%2C7!1%2C8!1%2C9!1
"""

curid="21925942"

def post(url, data,proxy_handler):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    opener = urllib2.build_opener()
    #opener = urllib2.build_opener(proxy_handler)
    opener.addheaders= [ ('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36') ]
    opener.addheaders.append( ('Host','/joinnew/processjq.ashx?curid='+curid+'&starttime=2018%2F3%2F30%2011%3A36%3A52&source=directphone&submittype=1&rn=1919210476&lct=49&t=1522381021549') )
    opener.addheaders.append( ('Accept','text/plain, */*; q=0.01') )
    opener.addheaders.append( ('Accept-Language','zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7') )
    opener.addheaders.append( ('Accept-Encoding','gzip, deflate') )
    opener.addheaders.append( ('Referer','https://www.wjx.cn/m/'+curid+'.aspx') )
    opener.addheaders.append( ('Cookie',' .ASPXANONYMOUS=rlxUNs390wEkAAAAN2IwYzQ4OTItMDU3Ni00MWVmLTkwZmMtNTAyYzg2Y2UzN2E09r7saLW-Lb6Mk9WLgqd5LJIusak1; UM_distinctid=16270f60bc721c-085df866e7bfdc-33697b04-1fa400-16270f60bc82bc; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1522313596; ASP.NET_SessionId=s4cx5jw4shcauybrfgblnzle; WjxUser=UserName=nian0114&Type=1; lllogcook=1; jac21925942=86424843; SojumpSurvey=010220BA00DAEE95D508FE205A12611096D50800086E00690061006E00300031003100340000012F00FFAEA47129E2C1429839A694D5E132A2AE4716DDD8; LastCheckUpdateDate=1; LastCheckDesign=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1522380745090; ev_21964368=1; CNZZDATA4478442=cnzz_eid%3D2146117123-1522308971-%26ntime%3D1522379678; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1522381014') )
    opener.addheaders.append( ('Origin','https://www.wjx.cn') )
    opener.addheaders.append( ('X-Requested-With','XMLHttpRequest') )
    opener.addheaders.append( ('X-Forwarded-For',str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))) )
    opener.addheaders.append( ('Content-Type','application/x-www-form-urlencoded; charset=UTF-8') )
    urllib2.install_opener(opener)

    response = opener.open(req, data)
    return response.read()

def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    arr = ["1","2","3","4","5","6","7"]

    for index, item in enumerate(rate):
        start += item
        if randnum <= start:
            break

    return arr[index]

def main():

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

    posturl = "https://www.wjx.cn/joinnew/processjq.ashx?curid="+curid+"&starttime=2018%2F3%2F29%2018%3A04%3A31&source=directphone&submittype=1&rn=796663080&t=1522317881413"
    dict= [[random_index([1,1,0,0,0,0,0])],
           [random_index([1,3,1,0,0,0,0])],
           [random_index([0,5,3,0,0,0,0])],
           [random_index([2,3,3,2,1,0,0])],
           [random_index([0,0,0,0,3,3,2]),random_index([0,0,0,1,3,3,2]),random_index([0,0,0,2,3,3,2]),random_index([0,0,0,1,3,3,1])],
           [random_index([0,0,0,1,3,3,2]),random_index([0,0,0,2,3,3,2]),random_index([0,0,0,1,3,3,2]),random_index([0,0,1,1,3,3,1])],
           [random_index([0,0,0,0,2,3,3]),random_index([0,0,0,0,0,2,3]),random_index([0,0,0,1,3,3,1]),random_index([0,0,0,0,1,1,1])],
           [random_index([0,0,0,0,0,3,3]),random_index([0,0,0,0,0,3,3]),random_index([0,0,0,0,0,3,3]),random_index([0,0,0,0,0,2,3]),random_index([0,0,0,0,1,1,1]),random_index([0,0,0,1,3,3,1]),random_index([0,0,0,0,3,3,1]),random_index([0,0,0,0,0,1,1]),random_index([0,0,0,2,3,3,1])]]

    data_result=""

    for k in range(len(dict)):
        if len(dict[k])==1:
            data_result += str(k+1)+urllib.quote("$")+dict[k][0]+urllib.quote("}")
        else:
            data_result += str(k+1)+urllib.quote("$")
            for v in range(len(dict[k])):
                if v+1 ==len(dict[k]):
                    data_result += str(v+1)+"!"+dict[k][v]
                else:
                    data_result += str(v+1)+"!"+dict[k][v]+urllib.quote(",")
            data_result += urllib.quote("}")


    print data_result[:-3]

    proxy_handler = ""

    data = {'submitdata':data_result[:-3]}

    while 1:
        try:
            print post(posturl, data,proxy_handler)
        except:
            continue

if __name__ == '__main__':
    main()
