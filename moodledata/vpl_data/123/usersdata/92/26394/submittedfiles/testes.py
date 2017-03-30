from __future__ import division

def xex(l2,x1,x2):
    lt=[]
    for i in range(0, x2-x1, 1):
        if (x1-l[i])<=(x2-l[i]):
            d= x1-l[i]
            if d<0:
                d= d*(-1)
        if (x1-l[i])>(x2-l[i]):
            d= x2-l[i]
            if d<0:
                d= d*(-1)
        lt.append(d)
        
    return l1
    

l= [0, -1, -1, -1, 0]
l2=[]
for i in range(0, len(l), 1):
    l2=[]
    if l2[i]==0:
        l2.append(i)

print xex(l, l2[0], l2[1])
        
