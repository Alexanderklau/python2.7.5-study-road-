import urllib
import urllib2

url = 'http://www.cuit.edu.cn/'

user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.1.6)' #Gecko/20070914 Firefox/2.0.0.7
values = {'name': 'WHY',
          'location': 'SDU',
          'language': 'Python'}

headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()