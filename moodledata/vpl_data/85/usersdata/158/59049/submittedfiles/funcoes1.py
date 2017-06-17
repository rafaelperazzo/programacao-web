# -*- coding: utf-8 -*-
n=int(input('digite n:'))
a=[]
for i  in range(0,n,1):
    x=float(input('digite x:'))
    a.append(x)
for i  in range(0,n,1):
    y=float(input('digite y:'))
    b.append(y)
for i  in range(0,n,1):
    z=float(input('digite z:'))
    c.append(z)
def crescente (a):
    cont=0
    for i in range(1,len(a),1):
        if a[i]>a[i-1]:
            cont=cont+1
    if cont==len(a)-1:
        return True
    else:
        return False
def decrescente (a):
    cont=0
    for i in range(1,len(a),1):
        if a[i]<a[i-1]:
            cont=cont+1
    if cont==len(a)-1:
        return False
    else:
        return True
def consecutivos (a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a==a[i+1]:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True