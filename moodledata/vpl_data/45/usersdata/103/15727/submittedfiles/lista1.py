# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantitade de elementos da lista:')
a=[]
for i in range (0,n,1):
    a.append(input('Digite um valor:')
si=0    
sp=0
qi=0
qp=0
for j in range (0,len(a),1):
    if (a[j]%2)==0:
        sp=sp+a[j]
        qp=qi+1
    else:
        si=si+a[i]
        q1=qi+1
print('Somatório dos ímpares:%f'%si)
print('Somatório dos pares:%f'%sp)
print('Quantidade de ímpares:%f'%qi)
print('SQuantidade de pares:%f'%qp)
print(a)