# http://www.pythonchallenge.com/pc/return/5808.html

""" the look and see sequence """

#a = [1, 11, 21, 1211, 111221] 

val = "1"

for i in range(30):
    cnt = 0 
    a = None
    tmp = ''
    for i in val: 
        if a:
            if a != i:
                tmp += str(cnt) + a
                a = i
                cnt = 0
        else:
            a = i
             
        cnt += 1
    val = tmp + str(cnt) + a
    print val

print len(val)
