#!/usr/bin/python  
# coding=utf-8
from BeautifulSoup import BeautifulSoup
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re
import logging
import traceback
import re

#登录的主页面
hosturl = 'http://www.lofter.com' #//自己填写
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
posturl = 'https://reg.163.com/logins.jsp' #//从数据包中分析出，处理post请求的url

#设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

#打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）
h = urllib2.urlopen(hosturl)

#构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。
headers = {
    #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Encoding':'gzip,deflate',
    #'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    #'Cache-Control':'max-age=0',
    #'Connection':'keep-alive',
    #'Content-Length':'158',
    #'Content-Type':'application/x-www-form-urlencoded',
    #'Cookie':'_ntes_nuid=6df1d205baf5a8c60240be009e6f7c53; SID=8d664ab7-5d72-485b-8867-f1eae40553bc; JSESSIONID=adeNFouIl2x2_95sVRKLu; vjuids=1a6cae3bb.14964af2570.0.511d79e; vjlast=1414733440.1414733440.30; _ntes_nnid=4bdf630e8dd1d2ee865be1b985835395,1414733440382; ne_analysis_trace_id=1414733442305; pver_n_f_l_n3=a; PopPushData=1414726245; vinfo_n_f_l_n3=b072541d42cbf206.1.0.1414733442314.0.1414733450494; s_n_f_l_n3=b072541d42cbf2061414733442317; T_INFO=990A52703BFDA09B5C96530F747A8FD5; P_INFO=chen_yueling@163.com|1414733979|2|lofter|00&99|US&1414733949&lofter#US&null#10#0#0|137274&0|mail163&study&blog&lofter&note|chen_yueling@163.com',
    #'Host':'reg.163.com',
    'Origin':'http://www.lofter.com',
    'Referer':'http://www.lofter.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'
}
#构造Post数据，他也是从抓大的包里分析得出的。
postData = {
    'password':'xxxxxxxx',
    'type':'1',
    'url':'http://www.lofter.com/logingate.do',
    'product':'lofter',
    'savelogin':'1',
    #'username':'xxxx@xxx.com',
    'domains':'www.lofter.com'
}

#需要给Post数据编码
postData = urllib.urlencode(postData)

#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
request = urllib2.Request(posturl, postData, headers)
print request
try:
    response = urllib2.urlopen(request)
    print response.geturl()
    print response.getcode()
    text = response.read()
    #print text
    #response = urllib2.urlopen('http://www.lofter.com')
    #text = response.read()
    #f = file('test.html', 'w')
    #f.write(text)
    soup = BeautifulSoup(text)

    script = soup.find("a")

    print script['href']

    response = urllib2.urlopen(script['href'])

    html = response.read()

    print(html)
    f = file('html.html', 'w')
    f.write(html)
    f.close()

    #print text
except Exception,e:
    print traceback.format_exc()

#text = response.read()  
