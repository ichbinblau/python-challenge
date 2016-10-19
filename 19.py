# answer: http://www.pythonchallenge.com/pc/hex/idiot.html

import base64
import wave 
import requests
import email
import re
import StringIO

URL="http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy)
r.raise_for_status()

#print r.text

pattern = "<!--\n(.*)\n-->"

b64 = re.findall(pattern, r.text, re.DOTALL)

mail = "".join(b64)

msg = email.message_from_string(mail)

print "Number of attachments is " + str(len(msg.get_payload()))

data = msg.get_payload()[0].get_payload(decode=True)

wav = wave.open(StringIO.StringIO(data))

open('19.wav', 'wb').write(data) 

sort = wave.open('19-1.wav', 'wb')
sort.setparams(wav.getparams())
for frame in range(wav.getnframes()):
    # read pne frame from the audio 
    # reverse the frame bytes
    sort.writeframes(wav.readframes(1)[::-1])
sort.close()
#with open('19.base64', 'rb') as encode:
#     content = encode.readlines()

#wave.open('19.wav') base64.b64decode(content)
