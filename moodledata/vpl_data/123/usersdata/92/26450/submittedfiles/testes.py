from __future__ import division

def xnx(l,p1,p2,li):
    
    for i in range(p1+1, p2+1, 1):
        d1= p1-i
        if d1<0:
            d1= d1*(-1)
        d2= p2-i
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
    
    for i in range(p+1, len(l), 1):
        d= (p-i)
        if d<0:
            d= d*(-1)
        li.append(d)
    return li


l= [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1]
li=[]

lp=[]
for i in range(0, len(l), 1):
    if l[i]==0:
        lp.append(i)

if len(lp)==1:
    nx(l,lp[0], li)
    xn(l,lp[0], li)

else:
    for j in range(0, len(lp), 1):
        if j==0:
            nx(l,lp[0], li)
        if lp[j]!=lp[len(lp)-1]:
            xnx(l,lp[j],lp[j+1],li)
        else:
            xn(l,lp[j], li)

print li