# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('tamanho da lista: '))
l=[]
soma=0
var=0
for i in range (1,n+1,1):
    a=float(input('elemento da lista: '))
    l.append(a)
for i in range (0,n,1):
    soma=soma+l[i]
media=soma/n
for i in range (0,n,1):
    var=var+(1/n-1)*(l[i]-media)**2
dp=var**0.5
print(var)