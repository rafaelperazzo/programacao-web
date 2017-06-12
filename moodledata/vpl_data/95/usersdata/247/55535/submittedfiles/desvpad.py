# -*- coding: utf-8 -*-
import math
n=int(input('digite: '))
a=[ ]
for i in range(1,n+1,1):
    valor=float(input('digite: '))
    a.append(valor)
def media(b):
    soma=0
    for i in range(0,len(b),1):
        soma=soma+a[i]
    media=soma/len(b)
    return media
def desvio(b):
    soma=0
    for i in range(0,len(b),1):
        soma=soma+((a[i]-media(b)**2))
    desvio =((soma/len(b)-1)**0.5)
    return desvio
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media(a))
print('%.2f'%desvio(a))
print(a)
