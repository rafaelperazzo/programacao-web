# -*- coding: utf-8 -*-
n=int(input('digite n: '))
a=[ ]
for i in range(1,n+1,1):
    valor=int(input('digite z: '))
    a.append(valor)
def media(a):
    soma=0
    for i in range(0,n,1):
        soma=soma+a[i]
    media=soma/len(a)
    return media
print('%.2f'%a[0])
print('%.2f'%a[n-1])
print('%.2f'%media(a))
print(a)
