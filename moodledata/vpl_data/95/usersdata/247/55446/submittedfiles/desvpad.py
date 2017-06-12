# -*- coding: utf-8 -*-
import math
n=int(input('digite: '))
a=[ ]
for i in range(1,n+1,1):
    valor=float(input('digite: '))
    a.append(valor)
def media(a):
    soma=0
    for i in range(0,n,1):
        soma=soma+a[i]
    media=soma/n
    return media
def desvio(a):
    soma=0
    for i in range(0,n,1):
        soma=soma+((a[i]-media(a)**2)
    desvio=((soma/len(a)-1)**0.5)
    return desvio
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media(a))
print('%.2f'%desvio(a))
print(a)
