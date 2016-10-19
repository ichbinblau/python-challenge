# answer: http://www.pythonchallenge.com/pc/return/balloons.html

import re
import bz2
from urlparse import unquote
import requests
from requests import Session

URL="http://www.pythonchallenge.com/pc/def/linkedlist.php"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy)
r.raise_for_status()
#print r.text
print r.cookies['info']


pat = re.compile( 'and the next busynothing is (\d+)' ) 
url_template = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={0}' 
next_num = '12345' 
cookies = [] 

while True:
    r = requests.get(url_template.format(next_num), proxies=proxy)
    c = r.cookies['info']
    if c:
        cookies.append(c)
    grp = pat.search(r.text)
    if grp:
        next_num = grp.groups()[0]
        print c, next_num
    else:
        break

encoded = "".join(cookies)
#import urllib
#print urllib.unquote_plus(encoded)
#print encoded

print "Hint:" + str(bz2.decompress(unquote(encoded.replace('+', '%20'))))

import urllib2
import xmlrpclib

class Urllib2Transport(xmlrpclib.Transport):
    def __init__(self, opener=None, https=False, use_datetime=0):
        xmlrpclib.Transport.__init__(self, use_datetime)
        self.opener = opener or urllib2.build_opener()
        self.https = https

    def request(self, host, handler, request_body, verbose=0):
        proto = ('http', 'https')[bool(self.https)]
        req = urllib2.Request('%s://%s%s' % (proto, host, handler), request_body)
        req.add_header('User-agent', self.user_agent)
        self.verbose = verbose
        return self.parse_response(self.opener.open(req))


class HTTPProxyTransport(Urllib2Transport):
    def __init__(self, proxies, use_datetime=0):
        opener = urllib2.build_opener(urllib2.ProxyHandler(proxies))
        Urllib2Transport.__init__(self, opener, use_datetime)

p = HTTPProxyTransport({
    'http': 'child-prc.intel.com:913'
})

server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=p)
#print server.system.listMethods()
print server.phone("Leopold")    

msg = "the flowers are on their way"
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
import urllib
#print unquote(urllib.quote(msg))
r = requests.get(url, proxies=proxy, cookies={'info': unquote(urllib.quote(msg))})
r.raise_for_status()
print r.text
