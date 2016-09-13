import urllib
import urllib2
url = 'http://www.cuit.edu.cn/'
values = {'name':'WHY',
          'location':'SDU',
          'language':'Python'
}
data = urllib.urlencode(values)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
the_page = response.read()


