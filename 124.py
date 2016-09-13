import urllib2
req = urllib2.Request('http://jxgl.cuit.edu.cn/Jxgl/Xs/MainMenu.asp')
try:
    urllib2.urlopen(req)
except urllib2.URLError, e:
    print e.code
