from __future__ import division

def xnx(l,p1,p2,li):
    
    for i in range(0, len(l), 1):
        if l[i]!=0:
            d1= (p1-i)
            if d1<0:
                d1= d1*(-1)
            d2= (p2-i)
            if d1<0:
                d2= d2*(-1)
            if d1<=d2:
                li.append(d1)
            else:
                li.append(d2)
    return li

def nx(l,p, li):
    
    for i in range(0, p+1, 1):
        if l[i]==0:
            li.append(l[i])
        else:
            d= (p-i)
            if d<0:
                d= d*(-1)
            li.append(d)
    return li
    
def xn(l,p, li):
    
    for i in range(p, len(l), 1):
        if l[i]==0:
            li.append(l[i])
        else:
            d= (p-i)
            if d<0:
                d= d*(-1)
            li.append(d)
    return li
    

l= [0, -1, -1, -1, 0]
l1= [-1, -1, -1, 0]
l2= [0, -1, -1, -1]
lp=[]
for i in range(0, len(l1), 1):
    if l1[i]==0:
        lp.append(i)
lp1=[]
for i in range(0, len(l2), 1):
    if l2[i]==0:
        lp1.append(i)

li=[]
nx(l1, lp[0], li)
xn(l2, lp1[0], li)

print li


    
        
