# http://www.pythonchallenge.com/pc/def/equality.html

"""solution one"""


import sys

counter = {}

with open('2.txt') as f:
    for l in f:
        for i in l: 
            if i in counter.keys():
                counter[i] += 1
            else:
                counter[i] = 1    

print counter

mini = sys.maxint
v_list = []

for k, v in counter.items():
    if v < mini:
        mini = v
        v_list = []
        v_list.append(k)
    elif v == mini:
        v_list.append(k)

print mini, v_list
    
""" Better one """
import collections

c = collections.Counter()
with open('2.txt') as f:
    for line in f:
        c.update(line.rstrip())

print c
