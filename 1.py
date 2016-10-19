#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://www.pythonchallenge.com/pc/def/ocr.html

""" solution 1 """
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#text="map"


new = []

for i in text:
    if not i.isalpha() and i in ('(', ')', " ", ".", "'"):
        new.append(i)
        continue

    n = ord(i) + 2

    if n > 122: 
        n = ord('a') + n - 122 - 1

    new.append(chr(n)) 

print "".join(new)

"""Recommended way"""

import string

in_tab = string.lowercase[:26]
out_tab = in_tab[:]

count = 1
while count < 3: 
    out_tab = out_tab[-1] + out_tab[0:26-1]
    count = count + 1

#print in_tab, out_tab

trantab =  string.maketrans(out_tab, in_tab)
print text.translate(trantab)


