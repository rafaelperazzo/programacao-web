# -*- coding: utf-8 -*-
import math

n=int(input('digite a quantidade de elementos da lista:'))

a=[]
soma=0
soma1=0
s=0
m=0

for i in range(0,n,1):
    p=float(input('digite o valor.'))
    a.append(p)
    i=i+1
for i in range(0,len(a),1):
    soma=soma+a[i]
    i=i+1
m=soma/n
for i in range(0,len(a),1):
    soma1=soma1+(a[i]-m)**2
    i=i+1
s=(1/(n-1))*soma

print('%.2f' %a[0])
print('%.2f' %a[len(a)]-1)
print('%.2f' %m)
print(s)

