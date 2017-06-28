# -*- coding: utf-8 -*-

def contador(c,d):
    cont=0
    for i in range(0,len(c),1):
        for g in range(0,len(c),1):
            if (c[i])==(d[g]):
                cont=cont+1
    return(cont)
c=[]
d=[]
m=int(input('Digite c:'))
l=int(input('Digite d:'))
for i in range(0,m,1):
    n=int(input('Digite n:'))
    c.append(n)
for i in range(0,1,1):
    j=int(input('Digite j:'))
    d.append(j)
print(contador(c,d))        
        