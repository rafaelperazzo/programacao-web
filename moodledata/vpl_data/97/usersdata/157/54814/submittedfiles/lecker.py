# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            ig lista[i]>lista[i-1]:
                cont=cont+1
            else:
                if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[a]
b=[]
n=int(input('Digite numero de elementos: '))
for i in range (1,n+1,1):
    valor=float(input('Lista 1/%d°Numero: '%i))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input'Lista 2/%d°Numero: '%i))
    b.append(valor)
if lecker(a):
    print('N')
else:
    print('S')
if lecker(b):
    print('N')
else:
    print('S')