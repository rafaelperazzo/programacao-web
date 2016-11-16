# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    lugar=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i-1]:
            lugar=i
            break
    
    contador=0
    for i in range(lugar,len(a)-1,1):
        if a[i]<=a[i-1]:
            contador=contador-1
    if contador==0 and lugar!=0:
        return True
    else:
        return False

a=[]
n = int(input('Digite a quantidade de elementos da lista: '))

for i in range(0,n,1):
    a.append(input('Adicione elementos a lista A:'))
    
if pico(a):
    print('S')
else:
    print('N')
