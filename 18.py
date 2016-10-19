# answer: www.pythonchallenge.com/pc/hex/bin.html 
# username: butter
# password: fly

import requests
import gzip, difflib


URL="http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz"
proxy = {
    'http': 'child-prc.intel.com:913',
    'https': 'child-prc.intel.com:913',
}

r = requests.get(URL, proxies=proxy, stream=True)
with open("18.gz", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)


data = gzip.open("18.gz")
d1, d2 = [], []
for line in data:
    line = line.strip()
    d1.append(line[:53].decode())
    d2.append(line[56:].decode())
data.close()

compare = difflib.Differ().compare(d1, d2)

#f = open('18-0.png', 'wb')
#f1 = open('18-1.png', 'wb')
#f2 = open('18-2.png', 'wb')

#for line in list(compare):
#    print line
#    bs = bytearray([int(o, 16) for o in line[2:].split()])
#    if line[0] == '+':
#        f1.write(bs)
#    elif line[0] == '-':
#        f2.write(bs)
#    else:
#        f.write(bs)

#f.close()
#f1.close()
#f2.close()
out = ['', '', '']
for line in list(compare):
    string = [chr(int(c, 16)) for c in line[2:].split()]
    if line[0] == '-':
        out[0] += ''.join(string)
    elif line[0] == '+':
        out[1] += ''.join(string)
    else:
        out[2] += ''.join(string)

for i in range(3):
    with open('18-%d.png' % i, 'wb') as img:
        img.write(out[i])
