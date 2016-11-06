# -*- coding: utf-8 -*-
from __future__ import division

n=input("Insira a Quantidade de Valores: ")
l=[]

for i in range (0,n,1):
    l.append(input("Insira um Valor: "))
    
soma2=0
soma3=0
q2=0
q3=0

for a in range(0,n,1):
    if l[a]%2==0:
        soma2=soma2+l[a]
        q2=q2+1
    elif l[a]%2!=0:
        soma3=soma3+l[a]
        q3=q3+1

print soma3
print soma2
print q3
print q2
print l
