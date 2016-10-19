# answer: http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
import sys

p = "[a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+"
pat = "[A-Z]{1}[a-z]{1}"

with open("3.txt") as f:
    text = f.read()

regex = re.compile(p)
gg = re.compile(pat)

for match in regex.findall(text):
    #print 'found a match!'
    #print match
    sys.stdout.write(gg.findall(match)[0][1])

print ' '
    
