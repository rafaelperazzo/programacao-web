# -*- coding: utf-8 -*-
n=int(input('digite n: '))
a=[ ]
for i in range(1,n+1,1):
    valor=int(input('digite z: '))
    a.append(valor)
def media(a):
    soma=0
    for i in range(1,n+1,1):
        soma=soma+a[i]
    media=soma/n
print(a[0])
print(a[len(a)+1])
print(media(a))
print(a)
