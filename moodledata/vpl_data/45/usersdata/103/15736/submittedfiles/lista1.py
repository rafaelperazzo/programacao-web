# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantitade de elementos da lista:')
a=[]
s=0
sp=0
qi=0
qp=0
for i in range (0,n,1):
    a.append(input('Digite um valor:'))
for j in range (0,len(a),1):
    if (a[j]%2)==0 or a[j]==0:
        sp=sp+a[j]
        qp=qi+1
    if (a[j]%2)==1 or a[j]==1:
        s=s+a[i]
        qi=qi+1
print('Somatório dos ímpares:%.f'%s)
print('Somatório dos pares:%.f'%sp)
print('Quantidade de ímpares:%.f'%qi)
print('Quantidade de pares:%.f'%qp)
print(a)