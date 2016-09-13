from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.cuit.edu.cn/'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()