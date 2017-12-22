# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite n: '))
a=[]
for i in range(0,n,1):
    x=int(input('digite valor: '))
    a.append(x)
    
print('%.2f' %a[0])
print('%.2f' %a[len(a)-1)

soma=0
for e in range(0,len(a),1):
    soma=a[e]+soma
media=soma/len(a)
print('%.2f' %media)
print(a)