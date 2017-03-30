from __future__ import division

def xnx(l,p1,p2):
    lt=[]
    for i in range(0, len(l), 1):
        if l[i]!=0:
            d1= (p1-i)
            if d1<0:
                d1= d1*(-1)
            d2= (p2-i)
            if d1<0:
                d2= d2*(-1)
            if d1<=d2:
                lt.append(d1)
            else:
                lt.append(d2)
    return lt

def nx(l,x):
    for i in range(0, x, 1):
        if 
    
    

l= [0, -1, -1, -1, 0]
lp=[]
for i in range(0, len(l), 1):
    if l[i]==0:
        lp.append(i)


    
        
