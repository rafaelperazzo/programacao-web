# -*- coding: utf-8 -*-
from __future__ import division

n=input("Insira a Quantidade de Notas: ")
a=[]
for i in range(0,n,1):
    a.append(input("Insira a Nota: "))
    

#média
soma=0
for j in range(0,len(a),1):
    soma=soma+a[j]

print soma/len(a)

#maior
maior=0
for k in range(0,len(a),1):
    if a[k]>maior:
        maior=a[k]
print maior