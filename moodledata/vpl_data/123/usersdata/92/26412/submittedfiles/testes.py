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

def nx(l,p):
    lt=[]
    for i in range(0, p+1, 1):
        if l[i]==0:
            lt.append(l[i])
        else:
            d= (p-i)
            if d<0:
                d= d*(-1)
            lt.append(d)
    return lt  
    
def xn(p,l):
    lt=[]
    for i in range(p, len(l), 1):
        if l[i]==0:
            lt.append(l[i])
        else:
            d= (p-i)
            if d<0:
                d= d*(-1)
            lt.append(d)
    return lt 
    

l= [0, -1, -1, -1, 0]
l1= [-1, -1, -1, 0]
l2= [0, -1, -1, -1]
lp=[]
for i in range(0, len(l2), 1):
    if l2[i]==0:
        lp.append(i)

print xn(lp[0],l2)


    
        
