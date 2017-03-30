from __future__ import division

def xex(l,x1,x2):
    lt=[]
    for i in range(0, len(l), 1):
        if l[i]!=0:
            d1= (x1-i)
            if d1<0:
                d1= d1*(-1)
            d2= (x2-i)
            if d1<0:
                d2= d2*(-1)
            if d1<=d2:
                lt.append(d1)
            else:
                lt.append(d2)
        else:
            lt.append(l[i])
        
    return lt
    

l= [0, -1, -1, -1, 0]
l2=[]
for i in range(0, len(l), 1):
    if l[i]==0:
        l2.append(i)

print xex(l, l2[0], l2[1])
        
