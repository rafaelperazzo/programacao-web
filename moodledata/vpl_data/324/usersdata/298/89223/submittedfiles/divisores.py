# -*- coding: utf-8 -*-
import math

n=int(input('Digite n: '))
a=int(input('Digite a: '))
b=int(input('Digite b: '))

lista=[]
for i in range (1, n+1, 1):
    k1=a*i
    k2=b*i
    lista=lista+[k1]
    lista=lista+[k2]
    
listafinal=[]
for k in listafinal:
    if k not in listafinal:
        listafinal.append(k)
listafinal.sort()

print(listafinal)