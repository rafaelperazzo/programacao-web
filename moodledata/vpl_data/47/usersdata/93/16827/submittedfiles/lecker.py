# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    if a[0]>a[1]:
        cont=cont+1
    if a[len(lista)-1]> a[len(lista)-2]:
        cont=cont+1
    for i in range(1,len(lista)-1,1):
        if a[i]>a[i+1] and a[i]>a[i-1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=input('tamanho das listas: ')
for i in range(0,n,1):
    a.append(input('elemento de a: '))
for i in range(0,n,1):
    b.append(input('elemento de b: '))
if (lecker(a)):
    print('S')
else:
    print('N')
if (lecker(b)):
    print('S')
else:
    print('N')
