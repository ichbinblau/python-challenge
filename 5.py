# answer: http://www.pythonchallenge.com/pc/def/channel.html

import requests
import pickle 

proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p', proxies=proxy)
if r.status_code in (requests.codes.ok,
                    requests.codes.created,
                    requests.codes.no_content):
    inp = r.text
    ret = pickle.loads(inp)
    for line in ret:
        print ''.join(elmt[0] * elmt[1] for elmt in line)
        
    
