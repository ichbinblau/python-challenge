# answer: http://www.pythonchallenge.com/pc/def/oxygen.html

import urllib2
import zipfile
import re

proxy = urllib2.ProxyHandler({'http': 'child-prc.intel.com:913'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

URL="http://www.pythonchallenge.com/pc/def/channel.zip"

with open(r'6.zip','wb') as f:
    f.write(urllib2.urlopen(URL).read())


zfile = zipfile.ZipFile(r'6.zip', 'r')
comments = []
pattern = "Next nothing is (\d+)"

index = "90052"

while True:
    data = zfile.read(index + '.txt')
    comments.append(zfile.getinfo(index + '.txt').comment)
    mat = re.search(pattern, data)
    if not mat:
        break
    index = ''.join(mat.group(1))
    if not index:
        break

print "".join(comments)

