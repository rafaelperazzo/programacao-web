# -*- coding: utf-8 -*-
from __future__ import division

n=input("digite valor de n:")
a=[]

soma=0
soma_1=0
cont=0
cont_1=0

for i in range (0,n,1):
    a.append(input("digite valor do elemento de fogo:))
    if a[i]%2==1:
        soma=soma+a[i]
        cont=cont+1
    if a[i]%2==0:
        soma_1=soma_1+a[i]
        cont_1=cont_1+1

print(soma)
print(soma_1)
print(cont)
print(cont_1)
print(a)