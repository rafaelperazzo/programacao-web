# -*- coding: utf-8 -*-
n=int(input('digite o numero de elementos:'))
a=[]
b=[]
for i in range(0,n,1):
    v=int(input('digite um numero para a lista:'))
    a.append(v)
for i in range(1,len(a),1):
    va=(a[i-1]-a[i])
    if va<0:
        va=va*(-1)
    b.append(va)
n1=max(b)
print (n1)

