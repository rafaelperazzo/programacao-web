# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if i==0:
            if lista[i]>list[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
            else:
                if lista[i]>lista[i+1] andlista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return False
a=[]
b=[]
n=int(input('digite n:'))
for i in range(i,n+1,1):
    valor=float(input('digite valor:'))
    a.append(valor)
for i in range(i,n+1,1):
    valor=float(input('digite valor:'))
    b.append(valor)
if lecker(a):
    print('N')
else:
    print('S')
if lecker(b):
    print('N')
else:
    print('S')
    if lista[0]>lista[1]:
        m+=1
    for i in range(1,n-1):
        if lista[i-1]<lista[i] and lsta[i]<lista[i+1]:
            m+=1
        if lista[n-1]>lista[n-2]:
            m+=1
            return m==1
print(lecker(2,5,10,46,25,12,7))

