from urllib2 import Request,HTTPError,URLError,urlopen

old_html = 'http://weibo.com/a/bind/prepare?entry=taobao&status=fail'
req = Request(old_html)
response = urlopen(req)
print 'old_html :' + old_html
print 'Real_html :' + response.geturl()
