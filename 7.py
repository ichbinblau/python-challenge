# answer: http://www.pythonchallenge.com/pc/def/integrity.html

import urllib2
from PIL import Image
import re

proxy = urllib2.ProxyHandler({'http': 'child-prc.intel.com:913'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

URL="http://www.pythonchallenge.com/pc/def/oxygen.png"

with open(r'7.png','w') as f:
    f.write(urllib2.urlopen(URL).read())

img = Image.open(r'7.png')

width, height = img.size

row = [img.getpixel((x, height / 2)) for x in range(0, width, 7)]
ords = [chr(r) for r, g, b, a in row if r == g == b]
ans = "".join(ords)
ret = [chr(int(n)) for n in re.findall('\d+', ans)]
print "".join(ret)
