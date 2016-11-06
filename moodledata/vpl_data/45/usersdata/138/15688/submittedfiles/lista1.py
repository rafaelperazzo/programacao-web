# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de números da lista:')
a=[]
soma=0
cont=0
soma2=0
cont2=0
for i in range (0,n+1,1):
    a.append(input('digite um número:'))
for i in range (0,len(a),1):
    if a[i]%2!=0:
        soma=soma+a[i]
        cont=cont+1
    elif a[i]%2==0:
        soma2=soma2+a[i]
        cont2=cont2+1
print soma
print soma2
print cont
print cont2
print (a)



