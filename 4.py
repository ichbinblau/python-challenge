#answer: http://www.pythonchallenge.com/pc/def/peak.html

import requests

inital = '12345'
param = {"nothing" : inital}
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

while True:
    try:
        r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php', proxies=proxy, params=param)
        code = r.status_code
        #print code
        if code in (requests.codes.ok, 
                        requests.codes.created, 
                        requests.codes.no_content):
            print r.text
            code = [ s for s in r.text.split() if s.isdigit()]
            code = code[0] if code else None
            if "Divide by two" in r.text:
                print "in divide by two "
                code = str(int(param['nothing']) / 2)
            if not code:
                break
            param = { "nothing" : code }
        else:
            print "wrong request. "    
    except Exception as e:
        print str(e.message)
        exit(1) 
