# -*- coding: utf-8 -*-
n=int(input('digite o número de elementos:'))
a=[]
b=[]
for i in range(0,n,1):
    v=int(input('digte um número para alista:'))
    a.append(v)

for i in range(1,len(a),1):
    va=(a[i-1]-a[i])
    if v<0:
        va=va*(-1)
        b.append(va)
    b.append(va)
n1=max(b)
print (n1)
print (b)

