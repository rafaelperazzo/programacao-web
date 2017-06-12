# -*- coding: utf-8 -*-
from __future__ import division

def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return(media)
    
n=int(input('dgite aquantidade:'))
a=[]
for i in range(0,n,1):
    valor=float(input('digite o valor'))
    a.append(valor)
    
print('%.2f'%a[0]
print('%.2f'%a[i])
print('%.2f'%media(a))
print(a)
