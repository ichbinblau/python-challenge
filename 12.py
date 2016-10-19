# answer: http://www.pythonchallenge.com/pc/return/disproportional.html

import requests
from requests.auth import HTTPBasicAuth

URL="http://www.pythonchallenge.com/pc/return/evil4.jpg"
USERNAME='huge'
PASSWORD='file'
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy, auth=HTTPBasicAuth(USERNAME, PASSWORD))
r.raise_for_status()
print r.content

r = requests.get('http://www.pythonchallenge.com/pc/return/evil2.gfx', proxies=proxy, auth=HTTPBasicAuth(USERNAME, PASSWORD))
r.raise_for_status()
data = r.content


for i in xrange(5):
    open("12-%d.jpg" % i, 'w').write(data[i::5])
