import httplib
import sys

def cut_url(url):
	return url[:url.index('/')], url[url.index('/'):]

url = sys.argv[-1]
host, path = cut_url(url)

http = httplib.HTTPConnection(host, 80)
http.request('INVALIDREQUEST', path)

response = http.getresponse()

print response.status, response.reason
print response.read()
