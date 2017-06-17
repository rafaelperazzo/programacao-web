# -*- coding: utf-8 -*-
n=int(input('digite o número de elementos:'))
a=[]
for i in range(0,n,1):
    v=int(input('digte um número para alista:'))
    a.append(v)
vat=0
for i in range(1,len(a),1):
    v=(a[i-1]-a[i])
    if v<vat:
        v=vat
    if v<0:
        v=v*(-1)
    vat=v
print(v)


