# answer: http://www.pythonchallenge.com/pc/return/mozart.html
# Jan 27, 1756 birthday of Wolfgang Mozart

import datetime

l_years = [ y*10+6 for y in range(100, 200) if (y*10+6)%4 == 0 ]
#print l_years

year_c = []
for y in l_years:
    d = datetime.date(y, 1, 27)
    if d.weekday () == 1: 
        year_c.append(y)

print year_c[-2] 


